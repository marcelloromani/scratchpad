#!/usr/bin/env python

"""
Python CLI template
"""

import logging
from argparse import ArgumentParser

from src.logging_utils import log_setup


def get_cli_args():
    parser = ArgumentParser()

    parser.add_argument(
        "file",
        type=str,
        help="File to process",
    )

    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "ERROR"],
        default="INFO",
        help="Set log level",
    )

    return parser.parse_args()


def main():
    args = get_cli_args()
    log_setup(logging.getLevelName(args.log_level))

    logger = logging.getLogger()
    logger.info(f"argument: {args.file}")


if __name__ == "__main__":
    main()
