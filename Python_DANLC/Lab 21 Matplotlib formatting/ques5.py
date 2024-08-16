# Using ChatGPT generate the python code to solve the same problem Scenario:
# Analyzing Sales Data Suppose you work for a retail company, and you have
# dummy data containing sales data for the past year. The data includes information such as
# SalesDate,product names,regions, sales quantities, prices, and dates. You have to generate
# a bar chart ,pie plot on region and prices and line chart on SalesDate and prices columns.
# Further, you need to get some inference out of the chart. Create a ChatGPT prompt to generate the code
# for this scenario. Based on the code generated, ask ChatGPT to give the conclusion/inference.
# Note. You can provide the data to ChatGPT or ask it to use sample data.

import pandas as pd
import matplotlib.pyplot as plt
data = {
    'SalesDate': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'ProductName': ['Product A'] * 3 + ['Product B'] * 3 + ['Product C'] * 3 + ['Product D'] * 3,
    'Region': ['North', 'South', 'East', 'West'] * 3,
    'SalesQuantity': [150, 120, 130, 160, 140, 155, 180, 170, 165, 175, 160, 150],
    'Price': [250, 270, 260, 255, 240, 245, 250, 265, 275, 280, 290, 300] }

df = pd.DataFrame(data)

region_sales = df.groupby('Region')['SalesQuantity'].sum()
plt.figure(figsize=(8, 6))
region_sales.plot(kind='bar', color='green')
plt.title('Total Sales Quantities by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Quantity')
plt.show()

# Pie Chart: Proportion of Sales Revenue by Region
df['Revenue'] = df['SalesQuantity'] * df['Price']
region_revenue = df.groupby('Region')['Revenue'].sum()
plt.figure(figsize=(8, 6))
region_revenue.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['green', 'blue', 'yellow', 'red'])
plt.title('Proportion of Sales Revenue by Region')
plt.ylabel('')  #
plt.show()

# Line Chart: Price Trend Over Time
plt.figure(figsize=(10, 6))
plt.plot(df['SalesDate'], df['Price'], marker='o', color='purple')
plt.title('Price Trend Over Time')
plt.xlabel('Sales Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()