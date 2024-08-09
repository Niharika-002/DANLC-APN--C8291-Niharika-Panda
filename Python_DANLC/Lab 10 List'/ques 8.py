# Given the list `numbers = [15, 3, 7, 20, 13, 9, 25, 1, 10]`, write a list comprehension to
# create a new list containing only the even numbers.

numbers = [15, 3, 7, 20, 13, 9, 25, 1, 10]
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)