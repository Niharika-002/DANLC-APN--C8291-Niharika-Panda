
# Wap to check whether a character is alphabet, number or special character.

character = input("Enter a character: ")
if (65<=ord(character)<=90) or (97<=ord(character)<=122):
    print("Character is a alphabet")
elif (48<=ord(character)<=57):
    print("Character is a Number")
else:
    print("Special Character")