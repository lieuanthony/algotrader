from portfolio import *
from market import *
from stock import *
import random

class Trader:
    __slots__ = ["portfolio", "market", "stop_loss"]
    
    def __init__(self, portfolio: Portfolio, market: Market): # type: ignore
        self.portfolio = portfolio
        self.market = market
        self.stop_loss = 0.9

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

            num_shares: int = 0

            if current_price > open_price:
                max_num_shares: int = self.portfolio.get_cash // current_price
                
                if current_price > open_price * 1.03:
                    num_shares = random.randint(max_num_shares//4, max_num_shares//2)
                elif current_price == high_price:
                    num_shares = max_num_shares // 2
                else:
                    num_shares = random.randint(1, max_num_shares//4)

                self.portfolio.buy_shares(stock, num_shares)
            elif current_price < open_price:
                max_num_shares: int = self.portfolio.get_portfolio_stocks[stock][1]
                
                if current_price < open_price * 0.97:
                    num_shares = random.randint(max_num_shares//4, max_num_shares//2)
                elif current_price == low_price:
                    num_shares = max_num_shares
                else:
                    num_shares = random.randint(1, max_num_shares//4)

                self.portfolio.sell_shares(stock, num_shares)



