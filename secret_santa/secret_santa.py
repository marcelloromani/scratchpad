#!/usr/bin/env python

"""
Secret Santa script.
"""

import logging
import os
import random
from argparse import ArgumentParser
from email.mime.text import MIMEText

import yaml_utils
from log_utils import log_setup
from smtp_conn import SmtpConn


def opt_setup():
    parser = ArgumentParser()

    parser.add_argument(
        "friends_file",
        type=str,
        help="List of friends' names and e-mail addresses (yaml format)"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "ERROR"],
        default="INFO",
        help="Set log level"
    )

    parser.add_argument(
        "--really-send",
        action="store_true",
        help="Send e-mail for real"
    )

    parser.add_argument(
        "--smtp-host",
        type=str,
        default="smtp.gmail.com:465",
        help="SSL SMTP host"
    )

    parser.add_argument(
        "--smtp-user",
        type=str,
        help="SMTP account name. Takes precedence over SMTP_USER"
    )

    parser.add_argument(
        "--smtp-pass",
        type=str,
        help="SMTP password. Takes precedence over SMTP_PASS"
    )

    return parser


def send_santa(smtp, friend, lucky_one, really_send=False):
    """
    Notify a friend who he/she'll have to give a present to
    :param smtp: SmtpConn object
    :param friend: the person who'll receive the Secret Santa email
    :param lucky_one: recipient of the friend's present
    :param really_send: if True, actually send the email message, defaults to False
    """
    logger = logging.getLogger("send_santa")
    logger.debug("{} ({} will be notified that his/her lucky one is {}".format(friend["name"], friend["email"], lucky_one["name"]))

    msg = MIMEText(
        "Ho ho ho!\nThis is a Secret (Soup) Santa announcement!\n\n{friend}, your lucky one is {lucky_one}!\n\nHo ho ho!\nSanta".format(
            friend=friend['name'],
            lucky_one=lucky_one['name'],
        )
    )

    from_email = "noreply@santaclaus.pole.north"
    to_email = friend["email"]
    body = msg.as_string()

    if not really_send:
        logger.info("Dry run:")
        logger.info("From: {}".format(from_email))
        logger.info("To:   {}".format(to_email))
        logger.info("Body: {}".format(body))
    else:
        logger.info("Sending annoucement to {} ({})".format(friend["name"], to_email))
        result = smtp.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=msg.as_string()
        )
        logger.debug(f"Sendmail result: {result}")


def get_option(value, env_var):
    if value is not None:
        value = value.strip()
    if not value:
        value = os.getenv(env_var)
        if value is not None:
            value = value.strip()
        return value


def main():
    parser = opt_setup()
    args = parser.parse_args()
    log_setup(logging.getLevelName(args.log_level))
    really_send = args.really_send

    logger = logging.getLogger("main")

    logger.info("Randomising dice...")
    random.seed()

    # load list of friendsWhe
    friends_file = args.friends_file
    logger.info(f"Loading friends list from: {friends_file}")
    try:
        friends = yaml_utils.loadfile(friends_file)
    except Exception as e:
        logger.error(f"Couldn't load list of friends: {e}")
        return
    logger.debug(f"Friends:\n{friends}")

    # match friends
    logger.info("Matching friends...")
    random.shuffle(friends)
    for k in range(0, len(friends) - 1):
        friends[k]['send_to'] = friends[k + 1]
    friends[len(friends) - 1]['send_to'] = friends[0]
    # log matches
    for friend in friends:
        logger.debug("{0} ==> {1}".format(friend['name'], friend['send_to']['name']))

    # initialise SMTP connection if requested
    smtp = None
    if really_send:
        logger.info("Initialising SMTP connection...")
        smtp = SmtpConn(args.smtp_host)

        smtp_user = get_option(args.smtp_user, "SMTP_USER")
        if not smtp_user:
            logger.error("No SMTP username specified. Use --smtp-user or SMTP_USER env var")

        smtp_pass = get_option(args.smtp_pass, "SMTP_PASS")
        if not smtp_pass:
            logger.error("No SMTP password specified. Use --smtp-pass or SMTP_PASS env var")

        if not smtp_user or not smtp_pass:
            exit(1)

        smtp.login(smtp_user, smtp_pass)

    # send or simulate the emails
    for friend in friends:
        send_santa(smtp, friend, friend['send_to'], really_send)


if __name__ == "__main__":
    main()
