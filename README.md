# Decoradores

## Loguru
Biblioteca para salvar o *log* de uma aplicação. Para saber mais [acesse aqui](https://github.com/Delgan/loguru)!  
Para saber o *log* ao debugar um código, basta substituir o 'print()' - que é utilizado para entender o que está acontecendo dentro da função - por 'logger.info()'. Por exemplo:
```python
from loguru import logger

def soma(x: int, y: int):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

soma(2, 3)
```
Invés de:
```python
def soma(x: int, y: int):
    print(x)
    print(y)
    print(x + y)
    return x + y

print(soma(2, 3))
```
