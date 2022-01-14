import logging

NAME = __name__
FMT = '%(asctime)s : %(filename)s : %(name)s : %(message)s'
DATEFMT = '%d-%b-%y %H:%M:%S'
LEVEL = logging.DEBUG
FILENAME = 'logs.log'


def log(name = NAME, filename = FILENAME, level = LEVEL, fmt = FMT, datefmt = DATEFMT) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():

        log_formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

        log_file_handler = logging.FileHandler(filename)
        log_file_handler.setLevel(level)
        log_file_handler.setFormatter(log_formatter)

        logger.addHandler(log_file_handler)

    logger.propagate = False

    return logger


if __name__ == '__main__':
    logger = log(name=__name__)
    logger.info('Logging...')

