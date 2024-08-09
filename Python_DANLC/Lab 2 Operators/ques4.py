
# Wap to check whether a character is alphabet or not.

ch = input("enter a character : ")
print("Character : ", ch)
print("ascii number : ",ord(ch))

result = "Is a character" if 65<=ord(ch)<=90 or 97<=ord(ch)<=122 else "Not a alphabet"
print(result)