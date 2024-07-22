from stock import *

class Portfolio:
    __slots__ = ["stocks", "principal_investment", "total_assets", "available_funds", "returns"]

    def __init__(self, principal_investment: float):
        self.stocks = dict[Stock, (float, int)] # stock : (price bought at, quantity)
        self.principal_investment = principal_investment
        self.total_assets = 0.0
        self.available_funds = principal_investment
        self.total_assets = 0.0
        self.total_losses = 0.0

    def buy_stocks(self, stock: Stock, quantitiy: int) -> None:
        current_price = stock.get_current_price
        self.available_funds -= current_price

        if stock in self.stocks.keys and self.stocks[stock][0] == current_price:
            self.stocks[stock][1] += quantitiy
        else:
            self.stocks[stock][0] = current_price
            self.stocks[stock][1] = quantitiy

    def sell_stocks(self, stock: Stock, quantity: int) -> None:
        self.available_funds += stock.get_current_price * quantity
        self.stocks[stock][1] -= quantity

        if self.stocks[stock][1] == 0:
            self.stocks.pop(stock)

    def update_returns(self) -> None:
        principal = self.principal_investment

        for stock in self.stocks:
            stock.get_current_price * self.stocks[stock]

    def get_stocks(self) -> dict(Stock): # type: ignore
        return self.stocks
    
    def get_total_assets(self) -> float:
        return self.total_assets
    
    def get_available_funds(self) -> float:
        return self.available_funds
    
    def get_net_change(self) -> float:
        return self.net_change