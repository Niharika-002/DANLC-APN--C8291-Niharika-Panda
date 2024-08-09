# Exception Handling with Logging
# Write a function `read_and_log` that reads a file and logs any exceptions that occur to a separate log file.
# Use exception handling to manage:

# File not found
# Permission denied.
# Any other error.
# Ensure the function writes detailed error messages to the log file and test it with various scenarios.


import logging

logging.basicConfig(filename='result.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_and_log(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


read_and_log("bjbjdc.txt")
