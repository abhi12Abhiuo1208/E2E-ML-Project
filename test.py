from src.logger import logger
from src.exception import CustomException

logger.info("Application started")

try:
    x = 10 / 2
    logger.info(f"Result: {x}")
except Exception as e:
    logger.error(e)

try:
    y = 10 / 0
except Exception as e:
    logger.error(CustomException(e))

logger.warning("This is a warning")

logger.info("Application finished")