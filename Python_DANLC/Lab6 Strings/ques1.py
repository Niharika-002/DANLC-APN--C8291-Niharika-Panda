# Write a Python program to count the occurrences of each word in a given sentence

# string = “To change the overall look of your document. To change the look available in the gallery”

str = 'To change the overall look of your document. To change the look available in the gallery'
searchstring = input("enter the word/character to find : ")

# to count the occurrences of each word
words = str.split()
count = 0
for word in words:
    if word == searchstring:
        count += 1

print(f"Number of occurrences of the word {searchstring} is", count)


# to count occurrences of each character
count = 0
for i in str:
    if i == searchstring:
        count += 1

print(f"Number of occurrences of the character {searchstring} is", count)
