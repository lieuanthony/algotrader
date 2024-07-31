from stock import *
from portfolio import *
from trader import *
import random

class Market:
    __slots__ = ["market_stocks", "time"]

    def __init__(self, market_stocks: dict[Stock, list[float, float]]): # dict[Stock, list[daily_performance, overall_performance]]
        self.market_stocks = market_stocks
        self.time = 9   # 9 instead of 9:30 for convenience
    
    def update_prices(self) -> None:
        for stock in self.market_stocks:
            daily_performance: float = self.market_stocks[stock][0]
            overall_performance: float = self.market_stocks[stock][1]
            price_change: float = 0.0
            chance: int = random.randint(1, 3)
            is_volatile: bool = self.time < 11

            if is_volatile and ((overall_performance >= 0.5 and chance > 1) or overall_performance < 0.5 and chance < 2):
                price_change = random.uniform(-0.025, 0.05)
            elif is_volatile and ((overall_performance >= 0.5 and chance < 2) or overall_performance < 0.5 and chance > 1):
                price_change = random.uniform(-0.05, 0.025)
            elif is_volatile:
                price_change = random.uniform(-0.05, 0.05)
            elif (daily_performance >= 0.5 and chance > 1) or (daily_performance < 0.5 and chance < 2):
                price_change = random.uniform(-0.0075, 0.015)
            elif (daily_performance >= 0.5 and chance < 2) or (daily_performance < 0.5 and chance > 1):
                price_change = random.uniform(-0.015, 0.0075)
            else:
                price_change = random.uniform(-0.015, 0.015)

            stock.update_prices(stock.get_current_price() * (1 + price_change))
            self.market_stocks[stock][0] *= (1 + price_change)
            self.market_stocks[stock][1] *= (1 + price_change)

            if self.market_stocks[stock][1] > 1.0:
                self.market_stocks[stock][1] = 1.0
            elif self.market_stocks[stock][1] < 0.0:
                self.market_stocks[stock][1] = 0.0

    def update_time(self) -> None:
        self.time += 1

    def reset_time(self) -> None:
        self.time = 9

    def reset_daily_performances(self) -> None:
        for stock in self.market_stocks:
            self.market_stocks[stock][0] = 0.5

    def crash(self) -> None:
        for stock in self.market_stocks:
            change: float = random.uniform(0.5, 0.9)
            stock.update_prices(stock.get_current_price() * change)
            stock.set_open_price(stock.get_current_price())
            self.market_stocks[stock][0] = (self.market_stocks[stock][0] * change)
            self.market_stocks[stock][1] = (self.market_stocks[stock][1] * change)

    def get_market_stocks_with_performance(self) -> dict[Stock, list[float, float]]:
        return self.market_stocks
    
    def get_market_stocks(self) -> list[Stock]:
        stocks: list[Stock] = []
        
        for stock in self.market_stocks:
            stocks.append(stock)

        return stocks
    
    def get_time(self) -> int:
        return self.time
    
def generate_random_market_stocks(num_market_stocks: int) -> dict[Stock, list[float, float]]:
    market_stocks: dict[Stock, list[float, float]] = dict()

    while len(market_stocks.keys()) < num_market_stocks:
        name: str = ""
        num_letters: int = random.randint(2, 4)
        
        for _ in range(num_letters):
            name += chr(random.randint(ord('A'), ord('Z')))

        if name in market_stocks.keys():
            continue
        else:
            stock: Stock = Stock(name, random.uniform(1.0, 100.0))
            market_stocks[stock] = [0.5, 0.5]

    return market_stocks

def simulate_market(market: Market, num_days: int, trader) -> None:
    for day in range(num_days):
        chance: int = random.randint(1, 100)

        if chance == 1:
            print("\nMarket is crashing!!!")
            market.crash()

        print("\nDay " + str(day + 1))

        for stock in market.get_market_stocks():
            stock.set_open_price(stock.get_current_price())

        for _ in range(7):
            executed_trade: tuple[int, int, list[Stock]] = trader.trade() # tuple[action, num_shares, stock]

            if executed_trade[0] == 1:
                for stock in executed_trade[1]:
                    print(str(market.get_time()) + ":00 - Trader bought " + str(executed_trade[1][stock]) + " " + str(stock))
                for stock in executed_trade[2]:
                    print(str(market.get_time()) + ":00 - Trader sold " + str(executed_trade[2][stock]) + " " + str(stock))

            market.update_prices()
            market.update_time()

        market.reset_daily_performances()
        market.reset_time()

        owned_stocks: list[tuple[str, int]] = []
        for stock in trader.get_trader_portfolio().get_portfolio_stocks():
            if trader.get_trader_portfolio().get_portfolio_stocks()[stock][2] > 0:
                owned_stocks.append((stock, trader.get_trader_portfolio().get_portfolio_stocks()[stock][2]))
        print("Portfolio: " + str(owned_stocks))
        print("Available Funds: $" + str(round(trader.get_trader_portfolio().get_cash(), 2)))
        print("Total Value: $" + str(round(trader.get_trader_portfolio().get_total_value(), 2)))
        print("Total Returns: $" + str(round(trader.get_trader_portfolio().get_returns(), 2)) + " (" + str(round((trader.get_trader_portfolio().get_returns()/trader.get_trader_portfolio().get_principal() * 100), 2)) + "%)")

def main():
    print(           
    " _____ _         _____           _         \n"
    "|  _  | |___ ___|_   _|___ ___ _| |___ ___ \n"
    "|     | | . | . | | | |  _| .'| . | -_|  _|\n"
    "|__|__|_|_  |___| |_| |_| |__,|___|___|_|  \n"
    "        |___|                                "                 
    )
    print("_" * 42)

    num_market_stocks: int = int(input("Enter the number of stocks you would like"
                                 "\nto have in the market: "))
    num_days: int = int(input("Enter the number of days you would like to"
                              "\nrun the simulation: "))
    principal: float = float(input("Enter the amount of money you would like"
                                   "\nthe trading bot to start with: $"))

    market_stocks: dict[Stock, list[float, float]] = generate_random_market_stocks(num_market_stocks)
    market: Market = Market(market_stocks)

    portfolio: Portfolio = Portfolio(principal)
    trader: Trader = Trader(portfolio, market)

    simulate_market(market, num_days, trader)

if __name__ == "__main__":
    main()