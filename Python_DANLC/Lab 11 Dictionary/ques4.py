# Write a Python program to get the key, value and item in a dictionary.
# Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
resultDict = {}
for key, value in input_dict.items():
    if value != None:
        resultDict[key]=value
print(resultDict)
