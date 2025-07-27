class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_pass, new_pass):
        if old_pass == self.__password:
            self.__password = new_pass