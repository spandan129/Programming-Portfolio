"""For better or worse, most access to computer systems is still reliant on passwords.
 Various mechanisms exist to manage keeping records of users, their passwords, and the 
 associated permissions. On traditional Unix systems the basic information (username, real name, password, etc)
   is stored in a plain text file usually  called ``/etc/passwd``. 

Three command-line programs are used in the Unix world to maintain password information.

* ``adduser`` creates a new user, in the form of a new entry in the password file.
* ``deluser`` does the opposite, by removing the entry from the password file.
* ``passwd`` allows a user to change their password.

When a user attempts to access a system, the username and password they provide are checked against
 this file. This is done with a program called ``login``.

This task involves developing implementations of each of these programs."""

import codecs

def encrypt_password(password):
    return codecs.encode(password, 'rot_13')

def read_password_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(':') for line in file]

def write_password_file(filename, data):
    with open(filename, 'w') as file:
        for entry in data:
            file.write(':'.join(entry) + '\n')

def add_user(username, real_name, password, filename):
    data = read_password_file(filename)
    for entry in data:
        if entry[0] == username:
            print("Cannot add. Most likely username already exists.")
            return
    encrypted_password = encrypt_password(password)
    data.append([username, real_name, encrypted_password])
    write_password_file(filename, data)
    print("User Created")

def del_user(username, filename):
    data = read_password_file(filename)
    for entry in data:
        if entry[0] == username:
            data.remove(entry)
            write_password_file(filename, data)
            print("User Deleted ")
            return
    print("User not found")

def change_password(username, current_password, new_password, filename):
    data = read_password_file(filename)
    for entry in data:
        if entry[0] == username:
            if encrypt_password(current_password) == entry[2]:
                entry[2] = encrypt_password(new_password)
                write_password_file(filename, data)
                print("Password changed.....")
                return
            else:
                print("Invalid current password. Nothing changed.")
                return
    print("User not found. Nothing changed.")

def login(username, password, filename):
    data = read_password_file(filename)
    for entry in data:
        if entry[0] == username and encrypt_password(password) == entry[2]:
            print("Access granted.")
            return
    print("Access denied.")
