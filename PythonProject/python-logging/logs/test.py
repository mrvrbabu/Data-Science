from logger import logging


def sum(a, b):
    logging.debug("Adding two numbers")
    return a + b


logging.debug("Calling addition function")
sum(3, 4)
logging.info("Addition complete")


def sub(b, a):
    logging.warn("Subtraction in action")
    return b - a


logging.warn("Subtraction complete successfully")
sub(4, 7)
