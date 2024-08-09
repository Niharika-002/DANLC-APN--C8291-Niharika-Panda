# Wap to check login and password.

user_id = "niha@gmail.com"
pass_id = "niha@123"

uid = input("enter your email : ")
# upass = input("enter the password : ")

if uid == user_id:
    upass = input("enter the password : ")

    if upass != pass_id:
        print("invalid user")
    else:
        print("login successfully")

else:
    print("invalid user")



