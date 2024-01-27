
from passwordManager import del_user

filename = 'password.txt'

username = input("Enter username: ")

del_user(username, filename)
