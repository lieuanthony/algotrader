from portfolio import *

class Trader:
    __slots__ = ["portfolio", "stop_loss"]
    
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.stop_loss = 0.9