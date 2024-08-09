# input bank login and password and check whether it is valid or not
# if login is successful, then give options to user for the following:-
# 1.Change password
# 2.Check Balance
# 3.Deposit Amount
# 4.Withdraw Amount

userid = "niharika@gmail.com"
password = "niha@453"
balance = 50000

userId = input("Enter User Id: ")

if (userid == userId):
    pswd = input("Enter Password: ")
    if (pswd == password):
        print("Login Successful")
        while True:
            # Present the menu options
            print("\nMenu:")
            print("1. Change Password")
            print("2. Check Balance")
            print("3. Deposit Amount")
            print("4. Withdraw Amount")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                old_pswd = input("Enter your old password for veriication: ")
                if old_pswd == password:
                    new_pswd = input("Enter a new password: ")
                    password = new_pswd
                    print("Password changed successfully.")
                else:
                    print("Incorrect Password")

            elif choice == "2":
                print(f"Your current balance is: {balance:.2f}")

            elif choice == "3":
                amount = float(input("Enter the amount to deposit: "))
                balance += amount
                print(f"{amount:.2f} has been deposited into your account.")
                print(f"Your current balance is: {balance:.2f}")

            elif choice == "4":
                amount = float(input("Enter the amount to withdraw: "))
                if amount > balance:
                    print("Not sufficient balance")
                else:
                    balance -= amount
                    print(f"{amount:.2f} has been withdrawn from your account.")
                    print(f"Your current balance is: {balance:.2f}")

            elif choice == "5":
                print("Thanks ! ")
                break

            else:
                print("Invalid choice.")
    else:
        print("Invalid Password")
else:
    print("Invalid userid")