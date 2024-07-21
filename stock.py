class Stock:
    __slots__ = ["open_price", "current_price", "high_price", "low_price"]

    def __init__(self, inital_public_offering: float):
        self.open_price = inital_public_offering
        self.current_price = inital_public_offering
        self.high_price = inital_public_offering
        self.low_price = inital_public_offering

    def update_open_price(self, other_price: float):
        self.open_price = other_price

    def update_current_high_low_prices(self, other_price: float):
        self.current_price = other_price

        if other_price > self.high_price:
            self.high_price = other_price
        elif other_price < self.low_price:
            self.low_price = other_price