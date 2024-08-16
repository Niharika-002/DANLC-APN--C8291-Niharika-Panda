# Determine which products in a store are out of stock (quantity is 0).
import numpy as np

inventory = np.array([10, 0, 5, 0, 20, 0])
out_of_stock = inventory[np.where(inventory==0)]

print(out_of_stock)