from user_module import User

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f" - {privilege}")
        else:
            print("No privileges assigned.")


class Admin(User):
    def __init__(self, first_name, last_name, email="", age=None):
        super().__init__(first_name, last_name, email, age)
        self.priv = Privileges([
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users"
        ])
