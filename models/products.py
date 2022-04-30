from utils.helpper import float_to_str_coin


class Product:
    counter: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__code: int = Product.counter
        self.__name: str = name
        self.__price: float = price
        Product.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Code: {self.code}' \
               f'\nName: {self.name}' \
               f'\nPrice: {float_to_str_coin(self.price)}'