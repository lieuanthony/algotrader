from stock import *
from portfolio import *
import random
import time

class Market:
    __slots__ = ["stocks", "time"]

    def __init__(self, stocks: dict[Stock, float]): # Stock : performance
        self.stocks = stocks
        self.time = 9   # 9 instead of 9:30 for convenience
    
    def update_prices(self) -> None:
        for stock in self.stocks:
            performance: float = self.stocks[stock]
            price_change: float = 0.0
            chance: int = random.randint(1, 3)

            if (performance >= 0.75 and chance > 1) or (performance <= 0.25 and chance < 2):
                price_change = random.uniform(-0.01, 0.02)
            elif (performance >= 0.75 and chance < 2) or (performance <= 0.25 and chance > 1):
                price_change = random.uniform(-0.02, 0.01)
            else:
                price_change = random.uniform(-0.02, 0.02)

            stock.update_prices(stock.get_current_price() * (1 + price_change))
            self.stocks[stock] *= (1 + price_change)

            chance = random.randint(1, 10)
            if chance == 1:
                self.stocks[stock] *= 0.95
            elif chance == 10:
                self.stocks[stock] *= 1.05

            if self.stocks[stock] > 1.0:
                self.stocks[stock] = 1.0
            elif self.stocks[stock] < 0.0:
                self.stocks[stock] = 0.0

    def update_time(self) -> None:
        if self.time == 16:
            for stock in self.stocks:
                stock.set_open_price(stock.get_current_price())

            self.time = 9
        else:
            self.time += 1

    def crash(self) -> None:
        for stock in self.stocks:
            change: float = random.uniform(0.75, 0.85)
            stock.update_prices(stock.get_current_price() * change)
            stock.set_open_price(stock.get_current_price())
            self.stocks[stock] = (self.stocks[stock] * change)

    def get_stocks(self) -> dict[Stock, float]:
        return self.stocks
    
    def get_time(self) -> int:
        return self.time
    
def generate_random_stocks(num_stocks: int) -> dict[Stock, float]:
    stocks: dict[Stock,float] = dict()

    while len(stocks.keys()) < num_stocks:
        name: str = ""
        num_letters: int = random.randint(2, 4)
        
        for _ in range(num_letters):
            name += chr(random.randint(ord('A'), ord('Z')))

        if name in stocks.keys():
            continue
        else:
            stock: Stock = Stock(name, random.uniform(1.0, 100.0))
            stocks[stock] = 0.5

    return stocks

def simulate_market(market: Market, num_days: int) -> None:
    for day in range(num_days):
        chance: int = random.randint(1, 100)
        if chance == 1:
            print("\nMarket is crashing!!!")
            market.crash()

        print("\nDay " + str(day + 1) + " - Market is now open!")

        for hour in range(8):
            print(str(market.get_time()) + ":00 - " + str(market.get_stocks()))
            market.update_time()

            if hour < 7:
                market.update_prices()

        print("Market is now closed...")


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

    stocks: list[Stock] = generate_random_stocks(num_stocks)
    market: Market = Market(stocks)

    simulate_market(market, num_days)

if __name__ == "__main__":
    main()