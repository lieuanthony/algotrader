from portfolio import *
from market import *
from stock import *

class Trader:
    __slots__ = ["portfolio", "market", "stop_loss"]
    
    def __init__(self, portfolio: Portfolio, market: Market): # type: ignore
        self.portfolio = portfolio
        self.market = market
        self.stop_loss = 0.9

    def trade(self) -> None:
        stocks: list[Stock] = self.market.get_market_stocks