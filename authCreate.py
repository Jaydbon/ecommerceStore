import json as js

def authCreate(name, password):
    with open('users.json', 'r') as file:
     users = js.load(file)

    for user in users:
        if user['username'] == name:
            return False
    user = {"username":name, "password":password}
    users.append(user)
    with open('users.json', 'w') as file:
        js.dump(users, file, indent=4)


    return True
