


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            r = file.read()
            print(r)

    except FileNotFoundError:
        print("the file does not exist")

    except Exception as e:
        print("Invalid filename")


filename = input("give the path of the file : ")
read_file(filename)