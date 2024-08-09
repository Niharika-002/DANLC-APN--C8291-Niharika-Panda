# Write a Python program to remove duplicate characters of a given string.
# Input = “String and String Function”
# Output: String and Function

str = "String and String Function"

words = str.split()
print(words)

str = ""
for word in words:
    if word not in str:        # if the word does not exist in words add it to str otherwise not
        str += (word + " ")

print(str)



