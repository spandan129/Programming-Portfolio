from passwordManager import add_user

filename = 'password.txt'

username = input("Enter new username: ")
real_name = input("Enter real name: ")
password = input("Enter password: ")

add_user(username, real_name, password, filename)
