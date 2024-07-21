from stock import *

class Portfolio:
    __slots__ = ["stocks", "total_assets", "available_funds", "total_gains", "total_losses"]

    def __init__(self, available_funds: float):
        self.stocks = dict(Stock)
        self.total_assets = 0.0
        self.available_funds = available_funds
        self.total_assets = 0.0
        self.total_losses = 0.0

    def buy_stock(self, stock: Stock):
        self.available_funds -= stock.get_current_price

        if stock in self.stocks.keys:
            self.stocks[stock] += 1
        else:
            self.stocks[stock] = 1

    def sell_stock(self, stock: Stock):
        self.available_funds += stock.get_current_price
        self.stocks[stock] -= 1
        
        if self.stocks[stock] == 0:
            self.stocks.pop(stock)