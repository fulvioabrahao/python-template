import logging
import sys


class Logger:
    def __init__(self, name: str, log_level: int = logging.DEBUG) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        # Create a console handler and set the level
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.logger.level)

        # Create a formatter and set it to the handler
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def exception(self, exception: Exception, log_stacktrace: bool = True) -> None:
        self.logger.exception(exception, exc_info=log_stacktrace)


# Usage example
# logger = Logger(__name__)

# logger.info("This is an info message.")
# logger.debug("This is a debug message.")
# logger.warning("This is a warning.")
# logger.error("This is an error.")
# logger.exception("This is an exception.")
