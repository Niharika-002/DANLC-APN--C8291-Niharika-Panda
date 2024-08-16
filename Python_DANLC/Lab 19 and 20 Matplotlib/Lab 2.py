# Create a line plot to visualize the daily closing prices of a stock over a year and give your conclusion

import matplotlib.pyplot as plt

stock_prices = [134.56, 128.34, 139.21, 142.77, 137.89, 145.12, 130.56, 138.44, 141.89, 136.75]

days=list(range(1,len(stock_prices)+1))

plt.figure(figsize=(3,3))
plt.plot(days,stock_prices)
plt.xlabel('Day of the Year')
plt.ylabel('Stock Price (USD)')
plt.title("Stock Prices over a year")
plt.show()