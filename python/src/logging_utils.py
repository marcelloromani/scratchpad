import logging
import sys


def log_setup(log_level):
    if type(log_level) == str:
        log_level = log_level.upper()

    log_level = logging.getLevelName(log_level)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    log_handler = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s - %(message)s')
    log_handler.setFormatter(formatter)
    root_logger.addHandler(log_handler)
