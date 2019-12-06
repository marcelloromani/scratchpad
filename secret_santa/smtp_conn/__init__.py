import logging
import smtplib


class SmtpConn:
    logger = logging.getLogger("SmtpConn")

    def __init__(self, smtp_ssl_host):
        """
        A connection is not attempted until the login() method is called
        :param smtp_ssl_host: host:port to connect to
        """

        self._logged_in = False

        # leading spaces would raise a weird exception, so trim them
        initial_len = len(smtp_ssl_host)
        smtp_ssl_host = smtp_ssl_host.strip()
        trimmed_len = len(smtp_ssl_host)
        if trimmed_len == 0:
            raise ValueError("smtp_ssl_host cannot be an empty string")
        if trimmed_len < initial_len:
            self.logger.warning("There were leading or trailing spaces in smtp_ssl_host")

        self.logger.debug(f"Initialising connection object to host '{smtp_ssl_host}'")
        self._smtp = smtplib.SMTP_SSL(smtp_ssl_host)

    def login(self, username, password):
        """
        Attempts to login to the smpt host with the provided credentials.
        The credentials are not stored in this object.
        :param username: smtp username
        :param password: smtp password
        """
        self._smtp.login(username, password)
        self._logged_in = True

    def logout(self):
        """
        Logs out of the smtp service
        :return: the result of smtp.quit() call
        """
        self._smtp.quit()
        self._logged_in = False

    def sendmail(self, from_addr, to_addrs, msg):
        if not self._logged_in:
            raise RuntimeError("Please login() first")
        return self._smtp.sendmail(from_addr, to_addrs, msg)
