class User:
    userDatabase = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if username not in self.userDatabase:
            self.userDatabase[username] = password
    
    def StoreUsers(self):
        with open("users.txt", "a") as database:
            for user in self.userDatabase.items():
                database.write(f"{user}:{user.password}")
