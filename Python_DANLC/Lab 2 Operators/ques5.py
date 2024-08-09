
# Wap to check a character and print whether it is an alphabet, number or Special character.
# Number 0- 9  : 48 to 57

char = input("Enter a character: ")
ascii_value = ord(char)

# Use ternary operators to determine the category
category = "alphabet" if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122) else "number" if (48 <= ascii_value <= 57) else "special character"

print(f"The character '{char}' is a {category}.")