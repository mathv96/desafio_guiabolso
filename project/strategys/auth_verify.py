from model.user import User
from DAO.return_user import return_user


user_data = return_user()

def verify(username, password):
    if not (username and password):
        return False
    if user_data.get(username) == password:
        return User(id=123)