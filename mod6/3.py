import getpass
import hashlib
import json
import logging

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        if msg == '"' or msg == "'":
            msg = None
        return msg, kwargs

logger = JsonAdapter(logging.getLogger("divider"))
def input_and_check_password():
    password: str = getpass.getpass()
    if not password:
        logger.warning('Вы ввели пустой пароль!')
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.error('Вы ввели некорректный символ')
        pass
    return False

if __name__ == "__main__":
    count_number: int = 3
    strin = "%(asctime)s - %(levelname)s - %(message)s".split(' - ')
    dct = dict()
    dct["time"] = strin[0]
    dct["level"] = strin[1]
    dct["message"] = strin[2]
    logging.basicConfig(level=logging.INFO, filename="skillbox_json_messages.log",
                        format=json.dumps(dct), datefmt='%I:%M:%S')
    json.dumps(logger.info("Вы пытаетесь аутентифицироваться"))
    logger.info(f'У вас {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error('Вы трижды ввели неправильный пароль!')
    exit(1)
