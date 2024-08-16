# Create a bar chart to represent monthly expenses in different spending
# categories and give your conclusion.

import matplotlib.pyplot as plt

categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1400, 700, 400, 170, 350]

plt.figure(figsize=(8,3))
plt.bar(categories, expenses)
plt.xlabel("Expense categories")
plt.ylabel("Monthly Expenses (USD)")
plt.title("Monthly Expenses Breakdown")

plt.show()