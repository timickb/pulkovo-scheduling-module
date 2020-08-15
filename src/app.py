import logging
import sys
import xlrd

LOGGING_FORMAT = '[%(levelname)s] [%(asctime)-5s] %(message)s'

if __name__ == "__main__":
    logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
    logger = logging.getLogger()

    logger.info("Starting module")

    