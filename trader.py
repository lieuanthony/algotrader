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

    def trade(self) -> list[int, dict[Stock, int], dict[Stock, int]]:
        portfolio_stocks: dict[Stock, list[Stock, float, int]] = self.portfolio.get_portfolio_stocks()
        market_stocks: list[Stock] = self.market.get_market_stocks()

        for stock in portfolio_stocks:
            price_bought_at: float = portfolio_stocks[stock][1]
            num_shares: int = portfolio_stocks[stock][2]
            stop_loss_price: float = price_bought_at * self.stop_loss

            if price_bought_at <= stop_loss_price:
                self.portfolio.sell_shares(stock, num_shares)

        bought_stocks: dict[Stock, int] = dict()
        sold_stocks: dict[Stock, int] = dict()

        for stock in market_stocks:
            open_price: float = stock.get_open_price()
            current_price: float = stock.get_current_price()
            high_price: float = stock.get_high_price()
            low_price: float = stock.get_low_price()

            num_shares: int = 0
            executed_trade: list[int, dict[Stock, int], dict[Stock, int]] = [0, bought_stocks, sold_stocks]

            if current_price > open_price:
                max_num_shares: int = self.portfolio.get_cash() // current_price
                
                if current_price > open_price * 1.03:
                    num_shares = random.randint(max_num_shares//4, max_num_shares//2)
                elif current_price == high_price:
                    num_shares = max_num_shares // 2
                else:
                    num_shares = random.randint(1, max_num_shares//4)

                self.portfolio.buy_shares(stock, num_shares)
                bought_stocks[stock] = num_shares
                executed_trade[0] = 1
            elif current_price < open_price and stock.get_name() in portfolio_stocks:
                max_num_shares: int = portfolio_stocks[stock.get_name()][2]
                
                if current_price < open_price * 0.97:
                    num_shares = random.randint(max_num_shares//4, max_num_shares//2)
                elif current_price == low_price:
                    num_shares = max_num_shares
                else:
                    num_shares = random.randint(1, max_num_shares//4)

                self.portfolio.sell_shares(stock, num_shares)
                sold_stocks[stock] = num_shares
                executed_trade[0] = 1
            
        self.portfolio.update_returns()
        return executed_trade

    def get_trader_portfolio(self) -> Portfolio:
        return self.portfolio