# Write a function convert_to_float that takes a list of strings and
# attempts to convert each string to a float. Use exception handling to manage:
#
# Value errors (e.g., strings that cannot be converted to float).
#
# Any other unexpected errors.

# The function should return a list of successfully converted floats and
# a list of errors (with the original string and the error message).

def convert_to_float(li):
    f = []

    for s in li:
        try:
            f.append(float(s))
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
    return f


li = ["hgy", 89, 54, 8, "tyg"]
print(f"Successfully converted to floats - ", convert_to_float(li))






