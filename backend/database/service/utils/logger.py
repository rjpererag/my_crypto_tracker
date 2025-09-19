import logging
import time

logger = logging.getLogger("MY_DB_HANDLER_LOGGER")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(f'logs/{time.strftime("%Y%m%d-%H%M%S")}.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
