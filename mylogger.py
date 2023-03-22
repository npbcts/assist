import os
import logging
import logging.handlers


this_folder = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(this_folder, "logs")
if os.path.exists(log_folder) is False:
    os.mkdir(log_folder)

__all__ = ["get_logger"]


def get_logger(filename: str) -> logging.Logger:
    """
    get_logger 输入文件名获取一个日志记录器
    Args:
        filename (str): _description_

    Returns:
        logging.Logger: _description_
    """
    log_file_path = os.path.join(log_folder, f"{filename}.log")
    logger = logging.getLogger("logger")

    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler(filename=log_file_path)

    logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.WARNING)
    handler2.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s -->> %(message)s")
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger.addHandler(handler1)
    logger.addHandler(handler2)

    # 分别为 10、30、30
    # print(handler1.level)
    # print(handler2.level)
    # print(logger.level)

    # logger.debug('This is a customer debug message')
    # logger.info('This is an customer info message')
    # logger.warning('This is a customer warning message')
    # logger.error('This is an customer error message')
    # logger.critical('This is a customer critical message')

    return logger
