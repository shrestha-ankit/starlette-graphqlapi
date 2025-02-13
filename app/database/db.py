USERS = [
    {"id": "1", "name": "Alice", "age": 25},
    {"id": "2", "name": "Bob", "age": 30},
]



def get_users():
    return USERS


def add_user(name: str, age: int):
    new_id = str(len(USERS) + 1)
    new_user = {
        "id": new_id,
        "name": name,
        "age": age
    }
    USERS.append(new_user)
    return new_user


def get_user_by_id(id: str):
    for user in USERS:
        if user["id"] == id:
            return user
    return

def update_user(id: str, name: str, age: int):
    for user in USERS:
        if user.get("id") == id:
            if name:
                user["name"] = name
            if age:
                user["age"] = age
            return user
    return

def delete_user(id: str):
    for index, user in enumerate(USERS):
        if user.get("id") == id:
            return  USERS.pop(index)
    
    return
