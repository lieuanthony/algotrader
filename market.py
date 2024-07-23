from stock import *
from portfolio import *
import random
import time

class Market:
    __slots__ = ["stocks", "status", "time"]

    def __init__(self, stocks: dict[Stock, float]): # Stock : performance
        self.stocks = stocks
        self.status = True # True = open; False = closed
        self.time = 9   # 9 instead of 9:30 for convenience
    
    def update_prices(self, other_price) -> None:
        for stock in self.stocks:
            stock.update_prices(other_price)

    def update_time(self) -> None:
        if time == 16:
            self.status = False
        else:
            time += 1

    def get_stocks(self) -> dict[Stock, float]:
        return self.stocks
    
    def set_status_open(self) -> None:
        self.time = 9
        self.status = True
    
    def is_open(self) -> bool:
        return self.status == True

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

def simulate_market(market: Market, num_days: int):
    for i in range(num_days):
        market.update_prices(5)
        print(market.get_stocks())

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
    time.sleep(3)
    print("Lets begin!")
    time.sleep(3)

    num_stocks: int = int(input("Enter the number of stocks you would like"
                                 "\nto have in the market: "))
    num_days: int = int(input("Enter the number of days you would like to"
                              "\nrun the simulation: "))

    stocks: list[Stock] = generate_random_stocks(num_stocks)
    market: Market = Market(stocks)

    simulate_market(market, num_days)

if __name__ == "__main__":
    main()