from loguru import logger


def soma(x: int, y: int):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y


soma(2, 3)
