import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate realistic data for a year
np.random.seed(0)  # For reproducibility
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Simulate stock prices with realistic daily changes
initial_price = 100
daily_returns = np.random.normal(loc=0.0005, scale=0.01, size=len(date_range))  # Small daily returns with some volatility
price_series = initial_price * (1 + daily_returns).cumprod()

closing_prices = pd.Series(price_series, index=date_range)

# Calculate the average daily return
daily_return = closing_prices.pct_change().dropna()  # Drop NaN values from the first day
average_daily_return = daily_return.mean()

# Find the date with the highest closing price
max_closing_price_date = closing_prices.idxmax()
max_closing_price = closing_prices.max()

# Generate a line chart
plt.figure(figsize=(12, 6))
closing_prices.plot(label='Closing Price', color='blue')
plt.title('Daily Closing Prices of the Company')
plt.xlabel('Date')
plt.ylabel('Price (in USD)')
plt.legend()
plt.grid(True)
plt.show()

# Print results
print(f"Average Daily Return: {average_daily_return:.4f}")
print(f"Date with the Highest Closing Price: {max_closing_price_date.date()}")
print(f"Highest Closing Price: {max_closing_price:.2f}")
