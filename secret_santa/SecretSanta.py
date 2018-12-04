#!/usr/bin/env python

"""
Secret Santa script.
"""

import sys
import logging
import yaml
import random
import smtplib
from argparse import ArgumentParser
from email.mime.text import MIMEText


def opt_setup():
    parser = ArgumentParser()

    parser.add_argument("file",
            type=str,
            help="List of friends' e-mails (yaml format)")

    parser.add_argument("--log-level",
            type=str,
            choices=["DEBUG", "INFO", "ERROR"],
            default="INFO",
            help="Set log level")

    parser.add_argument("--really-send",
            action = "store_true",
            help = "Send e-mail for real")

    parser.add_argument("--smtp-cfg",
            type = str,
            default = "smtp.yml",
            help = "SMTP credentials (yaml format)")

    return parser


def log_setup(logLevel):
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logLevel)

    logHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logHandler.setFormatter(formatter)
    rootLogger.addHandler(logHandler)


def yaml_loadfile(filename):
    with open(filename, 'r')  as stream:
        conf = yaml.load(stream)

    return conf


def email_login(smtp_auth_file):
    global smtp

    conf = yaml_loadfile(smtp_auth_file)

    smtp_user     = conf['smtp_user']
    smtp_pass     = conf['smtp_pass']
    smtp_ssl_host = conf['smtp_ssl_host']

    smtp = smtplib.SMTP_SSL(smtp_ssl_host)
    smtp.login(smtp_user, smtp_pass)


def email_logout():
    global smtp

    smtp.quit()


def send_email(friend_from, friend_to):
    global conf

    logger = logging.getLogger("notify_match")

    msg = MIMEText("Ho ho ho!\nThis is a Secret (Soup) Santa announcement!\n\n%s, your lucky one is %s!\n\nHo ho ho!\nSanta" % (friend_from['name'], friend_to['name']))
    msg['Subject'] = 'Secret Santa announcement'
    msg['From'] = 'Santa'
    msg['To'] = friend_from['name']

    logger.debug("From: {0} To: {1}".format(friend_from['name'], friend_to['name']))
    #logger.debug("msg = " + msg.as_string())

    logger.info("Sending...")
    smtp.sendmail(friend_to['email'], friend_from['email'], msg.as_string())


def main():
    parser = opt_setup()
    args = parser.parse_args()
    log_setup(logging.getLevelName(args.log_level))

    logger = logging.getLogger("main")

    # load list of friends
    logger.info("Loading friends list from: {0}".format(args.file))
    try:
        friends = yaml_loadfile(args.file)
    except Exception as e:
        logger.error("Couldn't load list of friends: {0}".format(e))
        return

    logger.debug("{0}".format(friends))

    # match friends
    random.shuffle(friends)
    for k in range(0, len(friends) - 1):
        friends[k]['send_to'] = friends[k + 1]
    friends[len(friends) - 1]['send_to'] = friends[0]

    for friend in friends:
        logger.debug("{0} ==> {1}".format(friend['name'], friend['send_to']['name']))

    # for real or not?
    logger.info("Send emails? {0}".format(args.really_send))

    if args.really_send:
        # load smtp configuration
        logger.debug("Smtp config file: {0}".format(args.smtp_cfg))
        try:
            smtp_cfg = yaml_loadfile(args.smtp_cfg)
        except Exception as e:
            logger.error("Couldn't load smtp configuration: {0}".format(e))
            return

        logger.info("SMTP login")
        email_login(args.smtp_cfg)

        for friend in friends:
            send_email(friend, friend['send_to'])

        logger.info("SMTP logout")
        email_logout()


if __name__ == "__main__":
    main()
