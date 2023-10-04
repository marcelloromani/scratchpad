import logging

import pytest

from src.logging_utils import log_setup


class TestLogSetup:
    log_level = None

    @classmethod
    def setup_class(cls):
        # save current log level
        logger = logging.getLogger()
        cls.log_level = logger.getEffectiveLevel()

    @classmethod
    def teardown_class(cls):
        # restore log level before tests
        log_setup(cls.log_level)

    def test_should_accept_uppercase(self):
        log_setup("DEBUG")

    def test_should_accept_lowercase(self):
        log_setup("debug")

    def test_should_accept_mixedcase(self):
        log_setup("dEBUg")

    def test_should_reject_invalid(self):
        with pytest.raises(ValueError):
            log_setup("FOO")
