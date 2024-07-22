from stock import *

class Portfolio:
    __slots__ = ["stocks", "principal", "total_value", "cash", "returns"]

    def __init__(self, principal: float):
        self.stocks = dict[Stock, (float, int)] # stock : (price bought at, num_shares)
        self.principal = principal
        self.total_value = 0.0
        self.cash = principal
        self.returns = 0.0

    def buy_shares(self, stock: Stock, num_shares: int) -> None:
        current_price: float = stock.get_current_price

        if self.cash < current_price * num_shares:
            return

        self.cash -= current_price
        self.total_value += current_price * num_shares

        if stock in self.stocks.keys and self.stocks[stock][0] == current_price:
            self.stocks[stock][1] += num_shares
        else:
            self.stocks[stock][0] = current_price
            self.stocks[stock][1] = num_shares

    def sell_shares(self, stock: Stock, num_shares: int) -> None:
        if stock not in self.stocks or self.stocks[stock][1] < num_shares:
            return

        current_price: float = stock.get_current_price
        self.cash += current_price * num_shares
        self.total_value -= current_price * num_shares
        self.stocks[stock][1] -= num_shares

        if self.stocks[stock][1] == 0:
            self.stocks.pop(stock)

    def update_returns(self) -> None:
        returns: float = 0.0

        for stock in self.stocks:
            current_price: float = stock.get_current_price
            num_shares: int = self.stocks[stock][1]
            if current_price > self.stocks[stock][0]:
                returns += current_price * num_shares
            else:
                returns -= current_price * num_shares

        self.returns = returns

    def get_stocks(self) -> dict[Stock, (float, int)]: # type: ignore
        return self.stocks
    
    def get_total_value(self) -> float:
        return self.total_value
    
    def get_cash(self) -> float:
        return self.cash
    
    def get_returns(self) -> float:
        return self.returns