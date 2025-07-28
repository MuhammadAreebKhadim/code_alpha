stock_price = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2750,
    "MSFT": 300,
    "AMZN": 135,
    "NVDA": 450,
    "META": 330,
    "NFLX": 420,
    "INTC": 35,
    "IBM": 140,
    "ADBE": 560,
    "ORCL": 120,
    "UBER": 65,
    "DIS": 90,
    "BABA": 85
}
total = 0
print("💹 Stock Portfolio Tracker")
print("📥 Enter stock name and quantity (type 'done' to finish):")
while True:
    stock = input("🔎 Stock Symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_price:
        print("⚠️ Stock not found. Try again.")
        continue
    quantity = int(input("🔢 Quantity: "))
    subtotal = stock_price[stock] * quantity
    print(f"💰 Added: {stock} * {quantity} = ${subtotal}")
    total += subtotal
print(f"\n✅ Total Investment Value: ${total}")

# Summary of investments
# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: ${total}\n")
print("📁 Saved summary to portfolio.txt")
