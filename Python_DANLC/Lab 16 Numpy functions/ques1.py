# Suppose you have a dataset containing daily temperature readings for a city, and you
# want to identify days with extreme temperature conditions. Find days where the
# temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees
# Celsius (cold day).
# Input:
# temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

import numpy as np
temp = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4.0, 4.0, -12.0])

days = np.arange(len(temp))
hot_day = np.where(temp > 35)
cold_day = np.where(temp < 5)

a1 = temp[hot_day]
a1_days = days[hot_day]

a2 = temp[cold_day]
a2_days = days[hot_day]

df = dict((i, j) for i, j in zip(a1_days, a1))
print("Hot Days: ")
print(f"Day  Temperature({chr(176)}C)")
for key, value in df.items():
    print(f"{key}   {value}")

df = dict((i, j) for i, j in zip(a2_days, a2))
print("Cold Days: ")
print(f"Day  Temperature({chr(176)}C)")
for key, value in df.items():
    print(f"{key}   {value}")

