import json as js

def authLogin(name, password):
    with open('users.json', 'r') as file:
     users = js.load(file)

    for user in users:
        if user['username'] == name and user['password'] == password:
            return True
    return False
            