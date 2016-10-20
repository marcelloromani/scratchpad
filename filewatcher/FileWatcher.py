#!/usr/bin/env python

import os
import logging

class FileWatcher(object):
    _logger = logging.getLogger("FileWatcher")

    def __init__(self, file_path, listener):
        self._file_path = file_path
        self._mtime = self.__get_mtime()
        self._listener = listener
        self.action()

    def __get_mtime(self):
        """
        Returns the last modification time of the file we're watching.
        """
        return os.stat(self._file_path).st_mtime

    def action(self):
        if not self._listener is None:
            self._logger.debug("action")
            self._listener.action(self._file_path)
        else:
            self._logger.debug("no listener, action not called")
        return

    def getFilePath(self):
        return self._file_path

    def poll(self):
        """
        To be run periodically.
        Checks if the file has been modified, and if so runs the action().
        """
        self._logger.debug("poll")
        mtime = self.__get_mtime()
        if mtime != self._mtime:
            self._logger.info("File has changed.")
            self._mtime = mtime
            self.action()
