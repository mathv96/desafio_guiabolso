class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='{}')".format(self.id)