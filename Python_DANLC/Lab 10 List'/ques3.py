# Write a Python program to find duplicate values from a list and display those.

def duplicate_val(li):
    item = {}
    d = []
    for item, ocurrences in li.items():
        if ocurrences > 1:
            d.append(item)

    print(d)


duplicate_val(li = [1,2,3,4,3,4])

