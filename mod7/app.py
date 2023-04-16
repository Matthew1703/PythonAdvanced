# import logging
import logging.config

import logging_tree
from flask import Flask
from mod7 import utils
# from multilevel_handler_task3 import MultiLevelHandler
from dict_loggers_task_4 import dict_config
from logging_tree import printout

app = Flask(__name__)

logging.config.dictConfig(dict_config)

logger = logging.getLogger("app")

@app.route("/summation/<float:a>/<float:b>")
def summation(a, b):
    logger.info("^&(**&^&&*( я пвавв")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.summation(a, b))
@app.route("/multiplication/<float:a>/<float:b>")
def multiplication(a, b):
    logger.info("^&(**&^&&*( я пвавв")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.multiplication(a, b))
@app.route("/subtraction/<float:a>/<float:b>")
def subtraction(a, b):
    logger.info("^&(**&^&&*( я пвавв")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.subtraction(a, b))
@app.route("/division/<float:a>/<float:b>")
def division(a, b):
    logger.info("^&(**&^&&*( я пвавв")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.division(a, b))

if __name__ == "__main__":
    with open("logging_tree.txt", "w") as f:
        f.write(logging_tree.format.build_description())
    logger.info(f"Started")
    app.run(debug=True)