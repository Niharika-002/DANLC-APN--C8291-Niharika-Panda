# dictionary operations

class DictDemo:
    # single dictionary
    emp_list = {"id": 101, "Name": "Kiran Singh", "Age": 25}

    # dictionary as list
    emp_list1 = [
        {"id": 101, "Name": "Kiran Singh", "Age": 25},
        {"id": 102, "Name": "K Singh", "Age": 23},
        {"id": 103, "Name": "Jai kumar", "Age": 21},
        {"id": 104, "Name": "Rashi Sejwal", "Age": 22},

    ]

    # nested dictionary
    emp_list2 = {
        "1": {"id": 101, "Name": "Kiran Singh", "Age": 25},
        "2": {"id": 102, "Name": "K Singh", "Age": 21}
    }

    def print_dictionary(self):
        print(self.emp_list)

    def add_elements(self):
        key1 = input("Enter the key : ")
        value1 = input("Enter the value : ")
        self.emp_list.update({key1: value1})
        self.emp_list[key1] = value1
        self.print_dictionary()


# cc = DictDemo()
# cc.add_elements()


class Customer:
    dd = DictDemo()

    def display(self):
        print("Employee records")
        for e in self.dd.emp_list1:
            print(e)
        print("-----------------------------------------")

    def add_employee(self):
        emp = {}
        id = int(input("Enter the new id : "))
        name = input("Enter new name : ")
        age = int(input("Enter his/her Age : "))

        emp.update({"id": id, "name": name, "age": age})
        self.dd.emp_list1.append(emp)

        self.display()

    def search_records(self):
        id = int(input("enter employee id to search : "))
        flag = False
        for r in self.dd.emp_list1:
            print(r)
            if r["id"] == id:
                print("record found !! ")
                print(r)
                flag = True
                break
        if not flag:
            print("record not found !! ")

    def delete_record(self):
        id = int(input("enter employee id to delete : "))
        self.dd.emp_list1 = [r for r in self.dd.emp_list1 if r["id"] != id]
        self.display()

    def update_record(self):
        id = int(input("enter employee id to update : "))
        print("Select option - ")

        while True:
            print("1. Update name")
            print("2. Update age")
            print("3. Exit")
            choice = input("Enter your choice : ")

            if choice == 1:
                n = input("enter updated name - ")
                for empName in self.dd.emp_list1:
                    if empName["id"] == id:
                        empName["Name"] = n
                        break

            if choice == 2:
                n = input("enter updated age : ")
                for empName in self.dd.emp_list1:
                    if empName["id"] == id:
                        empName["Name"] = n
                        break

    def merge_sort(self, emp_list1, key):
        if len(emp_list1) <= 1:
            return emp_list1

        mid = len(emp_list1) // 2
        left_half = self.merge_sort(emp_list1[:mid], key)
        right_half = self.merge_sort(emp_list1[mid:], key)

        return self.merge(left_half, right_half, key)

    def merge(self, left, right, key):
        sorted_list = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index][key] <= right[right_index][key]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])

        return sorted_list

    def sort_records_by_name(self):
        self.dd.emp_list1 = self.merge_sort(self.dd.emp_list1, "Name")
        print("Records sorted by Name:")
        self.display()

    def menu(self):
        while True:
            print("1. Add New Employee")
            print("2. Update an Employee")
            print("3. Delete an Employee")
            print("4. Search an Employee Record")
            print("5. sort records according to Name")
            print("6. Exit")
            print("Enter your choice : ", end="")

            choice = int(input())
            print("==========================================")
            if choice == 1:
                self.add_employee()
            elif choice == 2:
                self.update_record()
            elif choice == 3:
                self.delete_record()
            elif choice == 4:
                self.search_records()
            elif choice == 5:
                self.sort_records_by_name()
            elif choice == 6:
                print("Good Bye!!")
                break
            else:
                print("Wrong choice!!")


cc = Customer()
cc.menu()
