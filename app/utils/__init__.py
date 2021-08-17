import logging
import time

def set_config_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-10s %(levelname)-20s %(message)s",
        datefmt="%H:%M",
    )

def get_actual_time() -> str:
    return str(time.time())