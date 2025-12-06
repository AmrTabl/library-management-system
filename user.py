import csv

class User:
    file = "data/users.csv"

    def __init__(self, userid, name, email, password, role):
        self.userid = userid
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    @staticmethod
    def get_all():
        users = []
        with open(User.file, "r") as f:
            for row in csv.reader(f):
                if row:  # ignore empty lines
                    users.append(User(*row))
        return users

    @staticmethod
    def register(name, email, password, role="student"):
        all_users = User.get_all()
        userid = len(all_users) + 1

        with open(User.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([userid, name, email, password, role])

    @staticmethod
    def validate(email, password):
        with open(User.file, "r") as f:
            for row in csv.reader(f):
                if row and row[2] == email and row[3] == password:
                    return User(*row)
        return None

