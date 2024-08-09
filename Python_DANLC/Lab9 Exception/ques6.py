
# File Parsing with Detailed Error Handling
# Write a function `parse_file` that reads a file containing numerical data (one number per line) and
# returns a list of these numbers. Use exception handling to manage:

# File not found.
# Permission denied.
# Value errors (e.g., non-numeric data).
# Provide detailed error messages indicating the line number and nature of the error.

def parse_file(filename):
    plist = []
    try:
        with open(filename,'r') as file:
            for line in file:
                plist.append(int(line))
                print("number list : ", plist)
                file.close()

    except FileNotFoundError as fe:
        print("Exception1 : ", fe)
    except PermissionError as pe:
        print("Exception2 : ", pe)
    except ValueError as ve:
        print("Exception3 : ", ve)


filename = input("enter file name : ")
parse_file(filename)
