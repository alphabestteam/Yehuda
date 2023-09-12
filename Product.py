class Product:
    def __init__(
        self, name_product: str, price_for_unit: float, amount_unit: int
    ) -> None:
        self._name_product = name_product
        self._price_for_unit = price_for_unit
        self._amount_unit = amount_unit
        self._total_price = amount_unit * price_for_unit

    @property
    def name_product(self):
        return self._name_product

    @name_product.setter
    def name_product(self, x: str):
        self._name_product = x

    @property
    def price_for_unit(self):
        return self._price_for_unit

    @price_for_unit.setter
    def price_for_unit(self, x: float):
        self._price_for_unit = x

    @property
    def amount_unit(self):
        return self._amount_unit

    @amount_unit.setter
    def amount_unit(self, x: int):
        self._amount_unit = x

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, x: float):
        self._total_price = x
