from stock import *

class Portfolio:
    __slots__ = ["stocks", "principal", "total_value", "cash", "returns"]

    def __init__(self, principal: float):
        self.stocks = dict[Stock, (float, int)] # stock : (price bought at, quantity)
        self.principal = principal
        self.total_value = 0.0
        self.cash = principal
        self.total_value = 0.0
        self.total_losses = 0.0

    def buy_stocks(self, stock: Stock, quantitiy: int) -> None:
        current_price: float = stock.get_current_price

        if self.cash < current_price * quantitiy:
            return

        self.cash -= current_price
        self.total_value += current_price * quantitiy

        if stock in self.stocks.keys and self.stocks[stock][0] == current_price:
            self.stocks[stock][1] += quantitiy
        else:
            self.stocks[stock][0] = current_price
            self.stocks[stock][1] = quantitiy

    def sell_stocks(self, stock: Stock, quantity: int) -> None:
        if stock not in self.stocks or self.stocks[stock][1] < quantity:
            return

        current_price: float = stock.get_current_price
        self.cash += current_price * quantity
        self.total_value -= current_price * quantity
        self.stocks[stock][1] -= quantity

        if self.stocks[stock][1] == 0:
            self.stocks.pop(stock)

    def update_returns(self) -> None:
        returns: float = 0.0

        for stock in self.stocks:
            current_price: float = stock.get_current_price
            quantity: int = self.stocks[stock][1]
            if current_price > self.stocks[stock][0]:
                returns += current_price * quantity
            else:
                returns -= current_price * quantity

        self.returns = returns

    def get_stocks(self) -> dict[Stock, (float, int)]: # type: ignore
        return self.stocks
    
    def get_total_value(self) -> float:
        return self.total_value
    
    def get_cash(self) -> float:
        return self.cash
    
    def get_net_change(self) -> float:
        return self.net_change