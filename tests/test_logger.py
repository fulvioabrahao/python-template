import logging
import sys
import unittest
from unittest.mock import MagicMock, patch

from utils.logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.logger: Logger = Logger("test_logger")

    @patch("logging.getLogger")
    def test_init(self, mock_get_logger: MagicMock) -> None:
        mock_get_logger.return_value.level = logging.INFO
        Logger("test_logger")
        mock_get_logger.assert_called_once_with("test_logger")

    @patch("logging.StreamHandler")
    @patch("logging.Formatter")
    def test_setup_handler(
        self, mock_formatter: MagicMock, mock_stream_handler: MagicMock
    ) -> None:
        # Ignore linting error for accessing protected method
        self.logger._setup_handler()  # type: ignore
        mock_stream_handler.assert_called_once_with(sys.stdout)
        mock_formatter.assert_called_once_with(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    @patch("logging.Logger.debug")
    def test_debug(self, mock_debug: MagicMock) -> None:
        self.logger.debug("debug message")
        mock_debug.assert_called_once_with("debug message")

    @patch("logging.Logger.info")
    def test_info(self, mock_info: MagicMock) -> None:
        self.logger.info("info message")
        mock_info.assert_called_once_with("info message")

    @patch("logging.Logger.warning")
    def test_warning(self, mock_warning: MagicMock) -> None:
        self.logger.warning("warning message")
        mock_warning.assert_called_once_with("warning message")

    @patch("logging.Logger.error")
    def test_error(self, mock_error: MagicMock) -> None:
        self.logger.error("error message")
        mock_error.assert_called_once_with("error message")

    @patch("logging.Logger.exception")
    def test_exception(self, mock_exception: MagicMock) -> None:
        e = Exception("exception message")
        try:
            raise e
        except Exception as ex:
            e = ex
            self.logger.exception(e)
        mock_exception.assert_called_once_with(e, exc_info=True)
