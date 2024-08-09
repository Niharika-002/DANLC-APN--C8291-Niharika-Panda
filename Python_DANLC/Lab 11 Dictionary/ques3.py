# Write a Python program to get the key, value and item in a dictionary.
# input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


import pandas as pd
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Data = {"Key": dict_num.keys(),"Value": dict_num.values()}
df = pd.DataFrame(Data)

print(df.to_string(index=False))