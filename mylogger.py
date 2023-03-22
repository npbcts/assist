import os
import logging
import logging.handlers


__all__ = ["get_logger"]


def get_logger(filename: str, log_save_folder: str) -> logging.Logger:
    """
    get_logger 输入文件名和日志记录文件路径(在此路径下建立logs文件夹),获取一个日志记录器\n
        日志文件全部保存为: log_save_folder/logs/xxx.log

    Args:
        filename (str): 日志文件名\n
        log_save_folder(str): 保存logs文件夹的位置

    Returns:
        logging.Logger: 日志记录器

        日志记录器的记录级别:\n
        logger.debug('This is a customer debug message')\n
        logger.info('This is an customer info message')\n
        logger.warning('This is a customer warning message')\n
        logger.error('This is an customer error message')\n
        logger.critical('This is a customer critical message')
    """
    # 在给定的路径下建立logs文件夹
    log_folder = os.path.join(log_save_folder, "logs")
    if os.path.exists(log_folder) is False:
        os.mkdir(log_folder)

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

    return logger
