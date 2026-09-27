# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print("Stock:", stock)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Investment:", investment)

print("\n=== Portfolio Summary ===")
print("Total Investment:", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("-----------------------\n")
    file.write(f"Total Investment: {total_investment}\n")

print("Result saved to portfolio.txt")