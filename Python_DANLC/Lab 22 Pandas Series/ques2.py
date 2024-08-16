# Suppose you want to track and analyze your household expenses for a month.
# You have recorded the expenses for various categories, such as groceries, utilities, rent,
# transportation, and entertainment. You can represent this expense data using a Pandas Series.
# Input:

import pandas as pd

categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

df = pd.Series(expenses, index = categories, name = "Monthly Expenses")

print(df)