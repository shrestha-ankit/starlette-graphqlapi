from ariadne import QueryType
from app.database.db import get_users, get_user_by_id


query = QueryType()

@query.field("users")
def resolve_user(_, info):
    return get_users()

@query.field("user")
def resolve_single_user(_, info, id):
    user =  get_user_by_id(id)
    if not user:
        raise ValueError(f"User with ID {id} not found")
    
    return user