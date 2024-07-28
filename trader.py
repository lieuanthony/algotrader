from portfolio import *
from market import *
from stock import *

class Trader:
    __slots__ = ["portfolio", "market", "stop_loss"]
    
    def __init__(self, portfolio: Portfolio, market: Market): # type: ignore
        self.portfolio = portfolio
        self.market = market
        self.stop_loss = 0.93

    def trade(self) -> None:
        portfolio_stocks: dict[Stock, (float, int)] = self.portfolio.get_portfolio_stocks
        market_stocks: list[Stock] = self.market.get_market_stocks

        for stock in portfolio_stocks:
            price_bought_at: float = portfolio_stocks[stock][0]
            num_shares: int = portfolio_stocks[stock][1]
            stop_loss_price: float = price_bought_at * stop_loss_price

            if price_bought_at <= stop_loss_price:
                self.portfolio.sell_shares(stock, num_shares)

        for stock in market_stocks:
            open_price: float = stock.get_open_price
            current_price: float = stock.get_current_price
            high_price: float = stock.get_high_price
            low_price: float = stock.get_low_price


