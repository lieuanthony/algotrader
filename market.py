from stock import *
from portfolio import *
import random

class Market:
    __slots__ = ["stocks", "status", "volatility"]

    def __init__(self, stocks: list[Stock], volatility: float):
        self.stocks = stocks
        self.status = True # True = open; False = closed
        self.volatility = volatility

    def switch_status(self):
        self.status = not self.status

    def is_open(self) -> bool:
        return self.status == True

def generate_random_stocks(num_stocks: int) -> list[Stock]:
    stocks: list[Stock] = []

    for _ in range(num_stocks):
        name: str = ""
        num_letters: int = random.randint(2, 4)
        
        for _ in range(num_letters):
            name += chr(random.randint(ord('A'), ord('Z')))

        stock: Stock = Stock(name, random.uniform(1.0, 100.0))
        stocks.append(stock)

    return stocks

def main():
    print(           
    " _____ _         _____           _         \n"
    "|  _  | |___ ___|_   _|___ ___ _| |___ ___ \n"
    "|     | | . | . | | | |  _| .'| . | -_|  _|\n"
    "|__|__|_|_  |___| |_| |_| |__,|___|___|_|  \n"
    "        |___|                              \n"                 
    )

    stocks: list[Stock] = generate_random_stocks(10)
    print(stocks)

if __name__ == "__main__":
    main()