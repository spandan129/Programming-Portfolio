
from passwordManager import login

filename = 'password.txt'

username = input("User: ")
password = input("Password: ")

login(username, password, filename)
