# Exception Handling in List Operations
#
# Write a function `safe_list_access` that takes a list and an index as arguments and returns the element at that index.
# Use exception handling to manage:

# Index out of range.
# Any other error (provide a generic error message).
# Test the function with various lists and indices, including valid, negative, and out-of-range indices.

def safe_list_access(lt, indices):
    try:
        if not (-len(lt) <= indices <= len(lt)):
            raise IndexError
        print(lt[indices])

    except IndexError:
        print(f"Error: Index {indices} is out of range for list of length {len(lt)}.")
    except Exception as e:
        print(f"Error: {e}")


lst = [34,45,23,56,"hgb","cud", 65, True]
# indices = lst[14]


safe_list_access(lst, -4)


