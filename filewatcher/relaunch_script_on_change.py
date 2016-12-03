#!/usr/bin/env python

import time
import sys
from subprocess import call
import logging
from argparse import ArgumentParser
from FileWatcher import FileWatcher


class RerunOnChange(object):
    _logger = logging.getLogger("RerunOnChange")

    def action(self, file_path):
        self._logger.debug("We need to (re)run the file!")
        call(["python", file_path])


def optSetup():
    parser = ArgumentParser()

    parser.add_argument("file",
            type=str,
            help="File to process")

    parser.add_argument("--log-level",
            type=str,
            choices=["DEBUG", "INFO", "ERROR"],
            default="INFO",
            help="Set log level")

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

    listener = RerunOnChange()
    obj = FileWatcher(args.file, listener)

    while True:
        obj.poll()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
