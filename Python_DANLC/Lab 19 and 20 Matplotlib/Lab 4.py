# Create a histogram to represent the distribution of product prices in a retail
# store and give your conclusion.

import matplotlib.pyplot as plt

product_prices = [24.99, 34.99, 49.99, 64.99, 39.99, 54.99, 79.99, 99.99, 29.99, 44.99,
59.99, 69.99, 84.99, 109.99, 119.99, 89.99, 74.99, 124.99, 69.99, 54.99]

plt.figure(figsize=(8,7))
plt.hist(product_prices, edgecolor="black")
plt.xlabel("Product Prices (USD)")
plt.ylabel("Number of Products")
plt.title("Distribution of product prices in a Retail Store")

plt.show()