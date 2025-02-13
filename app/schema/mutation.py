from ariadne import MutationType
from app.database.db import add_user, delete_user, update_user


mutation = MutationType()


@mutation.field("createUser")
def resolve_create_user(_, info, name, age):
    return add_user(name, age)


@mutation.field("updateUser")
def resolve_update_user(_, info, id, name, age):
    user = update_user(id, name, age)
    if not user:
        raise ValueError(f"User with ID {id} not found")
    return user

@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    user = delete_user(id)
    if not user:
        raise ValueError(f"User with ID {id} not found")
    return user