# Wap to check whether a character is alphabet or not.

ch = input("enter a character : ")

if 65<=ord(ch)<=90 or 97<=ord(ch)<=122:
    print("character in alphabet")

else:
    print("character is not alphabet")
