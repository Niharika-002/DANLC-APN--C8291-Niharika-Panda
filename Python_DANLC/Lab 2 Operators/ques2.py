
# Wap to check whether a character is  in lower case or upper case.
# A-Z    :     65 to 90
# a-z   :       97 to 122

ch = input("enter a character : ")
result = "upper case" if 65<=ord(ch)<=90 else "lower case"
print(result)