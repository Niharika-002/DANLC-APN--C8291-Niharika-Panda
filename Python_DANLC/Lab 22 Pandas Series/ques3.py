# Suppose you want to track and analyze the monthly energy consumption in your
# home. You have recorded the monthly energy usage for electricity and gas over a year,
# and you want to represent this data using Pandas Series.

import pandas as pd

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]

print("Electricity Usage:")
df = pd.Series(electricity_usage, index = months, name = "Electricity Usage(kwh)")
print(df)

print("Gas Usage:")
df1 = pd.Series(gas_usage, index = months, name = "Electricity Usage(therms)")
print(df1)

