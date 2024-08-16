import pandas as pd
import matplotlib.pyplot as plt

# Create dummy data
data = {
    'Date': pd.date_range(start='2024-08-01', end='2024-08-10'),
    'Opening Price': [210, 212, 215, 217, 214, 219, 220, 225, 223, 228],
    'Closing Price': [212, 214, 218, 220, 217, 221, 223, 227, 225, 230]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set Date as the index
df.set_index('Date', inplace=True)

# Plotting the data
plt.figure(figsize=(10, 6))
df['Opening Price'].plot(label='Opening Price', marker='o')
df['Closing Price'].plot(label='Closing Price', marker='o')

# Adding title and labels
plt.title('SBI Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (in INR)')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
