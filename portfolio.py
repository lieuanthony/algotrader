from stock import *

class Portfolio:
    __slots__ = ["portfolio_stocks", "principal", "total_value", "cash", "returns"]

    def __init__(self, principal: float):
        self.portfolio_stocks = dict[Stock, (float, int)] # stock : (price bought at, num_shares)
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

        if stock in self.portfolio_stocks.keys and self.portfolio_stocks[stock][0] == current_price:
            self.portfolio_stocks[stock][1] += num_shares
        else:
            self.portfolio_stocks[stock][0] = current_price
            self.portfolio_stocks[stock][1] = num_shares

    def sell_shares(self, stock: Stock, num_shares: int) -> None:
        if stock not in self.portfolio_stocks or self.portfolio_stocks[stock][1] < num_shares:
            return

        current_price: float = stock.get_current_price
        self.cash += current_price * num_shares
        self.total_value -= current_price * num_shares
        self.portfolio_stocks[stock][1] -= num_shares

        if self.portfolio_stocks[stock][1] == 0:
            self.portfolio_stocks.pop(stock)

    def update_returns(self) -> None:
        returns: float = 0.0

        for stock in self.portfolio_stocks:
            current_price: float = stock.get_current_price
            num_shares: int = self.portfolio_stocks[stock][1]
            if current_price > self.portfolio_stocks[stock][0]:
                returns += current_price * num_shares
            else:
                returns -= current_price * num_shares

        self.returns = returns

    def get_portfolio_stocks(self) -> dict[Stock, (float, int)]: # type: ignore
        return self.portfolio_stocks
    
    def get_total_value(self) -> float:
        return self.total_value
    
    def get_cash(self) -> float:
        return self.cash
    
    def get_returns(self) -> float:
        return self.returns