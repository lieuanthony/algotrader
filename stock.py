class Stock:
    __slots__ = ["name","open_price", "current_price", "high_price", "low_price"]

    def __init__(self, name, inital_public_offering: float):
        self.name = name
        self.open_price = inital_public_offering
        self.current_price = inital_public_offering
        self.high_price = inital_public_offering
        self.low_price = inital_public_offering

    def set_open_price(self, other_price: float) -> None:
        self.open_price = other_price

    def update_prices(self, other_price: float) -> None:
        self.current_price = other_price

        if other_price > self.high_price:
            self.high_price = other_price
        elif other_price < self.low_price:
            self.low_price = other_price

    def get_name(self) -> str:
        return self.name

    def get_open_price(self) -> float:
        return self.open_price
    
    def get_current_price(self) -> float:
        return self.current_price
    
    def get_high_price(self) -> float:
        return self.high_price
    
    def get_low_price(self) -> float:
        return self.low_price