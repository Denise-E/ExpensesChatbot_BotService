import logging


def setup_logger():
    logger_instance = logging.getLogger("ExpenseBot")
    if not logger_instance.hasHandlers():  # To avoid duplicates
        logger_instance.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger_instance.addHandler(console_handler)
    return logger_instance


# Logger config
logger = setup_logger()
