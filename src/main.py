from utils.logger import Logger

logger = Logger(__name__)

logger.info("This is an info message.")
logger.debug("This is a debug message.")
logger.warning("This is a warning.")
logger.error("This is an error.")
try:
    raise Exception("This is an exception. Please check the traceback.")
except Exception as e:
    logger.exception(e)