from portfolio import *

class Trader:
    __slots__ = ["portfolio"]
    
    def __init__(self, principal):
        self.portfolio = Portfolio(principal)