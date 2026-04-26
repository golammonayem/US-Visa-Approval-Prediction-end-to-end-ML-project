from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


try:
    a = 1 / 0
    print(a)
except Exception as e:
    logging.info("Starting the exception handling")
    raise USvisaException(e, sys)
