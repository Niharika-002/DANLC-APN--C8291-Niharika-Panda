# Suppose you have a dataset containing monthly sales data for a company, and you
# want to split this data into quarterly reports for analysis and reporting purposes.

import numpy as np
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

s1 = np.split(monthly_sales, 4)

count = 1
for i in s1:
    print(f"Quarter {count} Sales (in thousand of dollar):")
    print(i)
    count += 1
