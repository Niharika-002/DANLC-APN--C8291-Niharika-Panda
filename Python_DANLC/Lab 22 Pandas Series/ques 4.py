# Suppose you are managing a website and want to analyze the monthly revenue
# generated from advertising. You have recorded the monthly revenue for the past year,
# and you want to represent this data using a Pandas Series.

import pandas as pd

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]

df = pd.Series(revenue, index=months, name = "Monthly advertising revenue(USD)")

print(df)