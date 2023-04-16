import logging
#import logging.handlers
#import sys
import logging.config
import logging_tree
from multilevel_handler_task3 import MultiLevelHandler
from dict_loggers_task_4 import dict_config

logging.config.dictConfig(dict_config)

logger = logging.getLogger("utils")

with open("logging_tree.txt", "a") as f:
    f.write(logging_tree.format.build_description())
logger.info("Started divider server")

def summation(a: float, b: float):
    logger.info("Function: summation")
    logger.debug(f"Args: {a} , {b}")
    res = a + b
    logger.debug(f"Result: {res}")
    return res
def multiplication(a: float, b: float):
    logger.info("Function: multiplication")
    logger.debug(f"Args: {a} , {b}")
    res = a * b
    logger.debug(f"Result: {res}")
    return res
def subtraction(a: float, b: float):
    logger.info("Function: subtraction")
    logger.debug(f"Args: {a} , {b}")
    res = a - b
    logger.debug(f"Result: {res}")
    return res
def division(a: float, b: float):
    logger.info("Function: division")
    logger.debug(f"Args: {a} , {b}")
    res = a / b
    logger.debug(f"Result: {res}")
    return res

