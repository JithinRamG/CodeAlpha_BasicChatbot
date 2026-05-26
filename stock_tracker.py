stocks = {
    "TSLA" : 250,
    "GOOGL": 170,
    "AAPL" : 180,
    "MSFT": 300,
    "NVDA" : 450
}

def stock_portfolio():
    total = 0
    print("Welcome to Stock Portfolio Tracker📈 !")

    while True:
        stock = input("Enter stock name: ").upper()

        if stock == "DONE":
            break
        elif stock in stocks:
            quantity = int(input("Enter quantity: "))
            total += stocks[stock] * quantity
            print(f"Added {stock} * {quantity}")
        else:
            print("Stock not found! Try TSLA, AAPL, MSFT, GOOGL or NVDA")

    print(f"Total investment: ${total}")

stock_portfolio()