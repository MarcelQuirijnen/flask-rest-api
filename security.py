# safer way to handle strings in older systems/python versions
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    # Payload is JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
