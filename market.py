from stock import *
from portfolio import *
import random

def create_random_stocks(num_stocks: int) -> list[Stock]:
    stocks = []

    for i in range(num_stocks):
        name = ""
        num_letters = random.randint(2, 4)
        
        for j in range(num_letters):
            name += chr(random.randint(ord('A'), ord('Z')))

        stock = Stock(name, random.uniform(5.0, 50.0))
        stocks.append(stock)

    return stocks

def main():
    ...

if __name__ == "__main__":
    main()