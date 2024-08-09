# Write a Python program to traverse a given list in reverse
# order, and print the elements with the original index.

# Original list: ['red', 'green', 'white', 'black']

def rev_list(li):
    a = li[::-1]
    print(f"Reversed list is - {a}")
    for i, item in enumerate(reversed(li)):
        original_index = len(li) - 1 - i
        print(f"Original index: {original_index}, Element: {item}")


rev_list(li=['red', 'green', 'white', 'black'])
