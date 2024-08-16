# Analyze the relationship between the size of houses (measured in square
# footage) and their selling prices in a particular neighborhood. You have collected
# data on various houses in that neighborhood.Create a scatter plot using the
# below data and share your conclusion/analysis.

import numpy as np
import matplotlib.pyplot as plt

square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

plt.figure(figsize = (6,6))
plt.scatter(square_footage, selling_prices, color = 'r')
plt.title("Housing prices vs square footage")
plt.xlabel("Square footage (sq.ft.)")
plt.ylabel("Housing prices ($000s)")
plt.grid(True)

plt.show()
