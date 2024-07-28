from decorator.log import log_decorator


@log_decorator
def soma(x: int, y: int):
    return x + y


soma(2, 3)
