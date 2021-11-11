#!/usr/bin/env python

"""
Script skeleton.
"""

import logging
import sys
from argparse import ArgumentParser


def optSetup():
    parser = ArgumentParser()

    parser.add_argument(
        "file",
        type=str,
        help="File to process"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "ERROR"],
        default="INFO",
        help="Set log level"
    )

    return parser


def logSetup(logLevel):
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logLevel)

    logHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logHandler.setFormatter(formatter)
    rootLogger.addHandler(logHandler)


def main():
    parser = optSetup()
    args = parser.parse_args()
    logSetup(logging.getLevelName(args.log_level))

    logger = logging.getLogger("main")
    logger.info("argument: {0}".format(args.file))


if __name__ == "__main__":
    main()
