from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    Function that gets called when a user calls the /auth endpoint
    with their username and password.
    :param username: User's username in string format.
    :param password: User's un-encrypted password in string format.
    :return: A UserModel object if authentication was successful, None otherwise.
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """
    Function that gets called when user has already authenticated, and Flask-JWT
    verified their authorization header is correct.
    :param payload: A dictionary with 'identity' key, which is the user id.
    :return: A UserModel object.
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
