import logging
import sys


def log_setup(logLevel):
    """
    Initialises the logging system to print to stdout, with a reasonable log format.
    :param logLevel: log level to use. Optional: default = INFO
    """

    if logLevel is None:
        logLevel = logging.INFO

    rootLogger = logging.getLogger()
    rootLogger.setLevel(logLevel)

    logHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logHandler.setFormatter(formatter)

    if len(rootLogger.handlers) == 0:
        rootLogger.addHandler(logHandler)
