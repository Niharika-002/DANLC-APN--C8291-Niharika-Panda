# Visualize the daily temperature changes over time in a city and give your
# conclusion

import matplotlib.pyplot as plt
temperature_data = [22.5, 18.7, 20.1, 25.3, 19.8, 23.2, 21.6, 24.0, 22.0, 18.5]

plt.plot(temperature_data, marker="o", ms=10)
plt.show()