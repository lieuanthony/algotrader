from stock import *
from portfolio import *
import random
import time

class Market:
    __slots__ = ["stocks", "time", "hourly_prices_enabled"]

    def __init__(self, stocks: dict[Stock, list[float, float]]): # Stock : [daily_performance, overall_performance]
        self.stocks = stocks
        self.time = 9   # 9 instead of 9:30 for convenience
        self.hourly_prices_enabled = False
    
    def update_prices(self) -> None:
        for stock in self.stocks:
            daily_performance: float = self.stocks[stock][0]
            overall_performance: float = self.stocks[stock][1]
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
            self.stocks[stock][0] *= (1 + price_change)
            self.stocks[stock][1] *= (1 + price_change)

            if self.stocks[stock][1] > 1.0:
                self.stocks[stock][1] = 1.0
            elif self.stocks[stock][1] < 0.0:
                self.stocks[stock][1] = 0.0

    def update_time(self) -> None:
        if self.time == 16:
            for stock in self.stocks:
                stock.set_open_price(stock.get_current_price())

            self.time = 9
        else:
            self.time += 1

    def reset_daily_performances(self) -> None:
        for stock in self.stocks:
            self.stocks[stock][0] = 0.5

    def crash(self) -> None:
        for stock in self.stocks:
            change: float = random.uniform(0.5, 0.9)
            stock.update_prices(stock.get_current_price() * change)
            stock.set_open_price(stock.get_current_price())
            self.stocks[stock][0] = (self.stocks[stock][0] * change)
            self.stocks[stock][1] = (self.stocks[stock][1] * change)

    def get_stocks(self) -> dict[Stock, float]:
        return self.stocks
    
    def get_time(self) -> int:
        return self.time
    
    def enable_hourly_prices(self) -> None:
        self.hourly_prices_enabled = True

    def is_hourly_prices_enabled(self) -> bool:
        return self.hourly_prices_enabled
    
def generate_random_stocks(num_stocks: int) -> dict[Stock, list[float, float]]:
    stocks: dict[Stock, list[float, float]] = dict()

    while len(stocks.keys()) < num_stocks:
        name: str = ""
        num_letters: int = random.randint(2, 4)
        
        for _ in range(num_letters):
            name += chr(random.randint(ord('A'), ord('Z')))

        if name in stocks.keys():
            continue
        else:
            stock: Stock = Stock(name, random.uniform(1.0, 100.0))
            stocks[stock] = [0.5, 0.5]

    return stocks

def simulate_market(market: Market, num_days: int) -> None:
    for day in range(num_days):
        chance: int = random.randint(1, 100)

        if chance == 1:
            print("\nMarket is crashing!!!")
            market.crash()

        if market.is_hourly_prices_enabled():
            print("\nDay " + str(day + 1) + " - Market is now open!")

            for hour in range(8):
                print(str(market.get_time()) + ":00 - " + str(list(market.get_stocks().keys())))
                market.update_time()

                if hour < 7:
                    market.update_prices()

            print("Market is now closed...")
        else:
            for hour in range(8):
                market.update_time()

                if hour < 7:
                    market.update_prices()

        market.reset_daily_performances()

def main():
    print(           
    " _____ _         _____           _         \n"
    "|  _  | |___ ___|_   _|___ ___ _| |___ ___ \n"
    "|     | | . | . | | | |  _| .'| . | -_|  _|\n"
    "|__|__|_|_  |___| |_| |_| |__,|___|___|_|  \n"
    "        |___|                                "                 
    )
    print("_" * 42
          + "\nWelcome to AlgoTrader! AlgoTrader uses a"
          "\nsimulated market created from made-up data"
          "\nto test the performance of the trading bot.")
    time.sleep(2)
    print("Lets begin!")
    time.sleep(2)

    num_stocks: int = int(input("Enter the number of stocks you would like"
                                 "\nto have in the market: "))
    num_days: int = int(input("Enter the number of days you would like to"
                              "\nrun the simulation: "))
    principal: float = float(input("Enter the amount of money you would like"
                                   "the trading bot to start with (float): "))
    response: str = input("Would you like to enable hourly prices (y or n): ")

    stocks: dict[Stock, list[float, float]] = generate_random_stocks(num_stocks)
    market: Market = Market(stocks)

    if response.lower() == "y":
        market.enable_hourly_prices()

    simulate_market(market, num_days)

if __name__ == "__main__":
    main()