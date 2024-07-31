from portfolio import *
from market import *
from stock import *
import random

class Trader:
    __slots__ = ["portfolio", "market", "stop_loss"]
    
    def __init__(self, portfolio: Portfolio, market: Market): # type: ignore
        self.portfolio = portfolio
        self.market = market
        self.stop_loss = 0.96

    def trade(self) -> list[int, dict[Stock, int], dict[Stock, int]]:
        portfolio_stocks: dict[str, list[Stock, float, int]] = self.portfolio.get_portfolio_stocks()
        market_stocks: list[Stock] = self.market.get_market_stocks()

        bought_stocks: dict[Stock, int] = dict()
        sold_stocks: dict[Stock, int] = dict()

        executed_trade: list[int, dict[Stock, int], dict[Stock, int]] = [0, bought_stocks, sold_stocks]

        for stock in portfolio_stocks:
            price_bought_at: float = portfolio_stocks[stock][1]
            num_shares: int = portfolio_stocks[stock][2]
            stop_loss_price: float = price_bought_at * self.stop_loss

            if stop_loss_price <= price_bought_at and num_shares > 0:
                self.portfolio.sell_shares(stock, num_shares)
                sold_stocks[stock] = num_shares
                executed_trade[0] = 1

        for stock in market_stocks:
            open_price: float = stock.get_open_price()
            current_price: float = stock.get_current_price()
            high_price: float = stock.get_high_price()

            can_buy: bool = False
            can_sell: bool = False

            if self.portfolio.get_cash() // current_price > 0:
                can_buy = True
                max_num_buy_shares: int = self.portfolio.get_cash() // current_price

            if stock.get_name() in portfolio_stocks and portfolio_stocks[stock.get_name()][2] > 0:
                can_sell = True;
                max_num_sell_shares: int = portfolio_stocks[stock.get_name()][2]

            if (current_price >= open_price * 1.04 or current_price == high_price) and can_sell:
                num_shares = portfolio_stocks[stock.get_name()][2]
                self.portfolio.sell_shares(stock, num_shares)
                sold_stocks[stock] = num_shares
                executed_trade[0] = 1
            elif current_price >= open_price * 1.02 and can_buy:
                num_shares = random.randint(1, max_num_buy_shares)
                self.portfolio.buy_shares(stock, num_shares)
                bought_stocks[stock] = num_shares
                executed_trade[0] = 1
            elif current_price <= open_price * 0.98 and can_sell:
                num_shares = random.randint(1, max_num_sell_shares)
                self.portfolio.sell_shares(1, max_num_sell_shares)
                sold_stocks[stock] = num_shares
                executed_trade[0] = 1
            else:
                continue

        self.portfolio.update_total_value() 
        self.portfolio.update_returns()
        return executed_trade

    def get_trader_portfolio(self) -> Portfolio:
        return self.portfolio