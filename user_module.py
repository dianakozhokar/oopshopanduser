class User:
    def __init__(self, first_name, last_name, email="", age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        if self.email:
            print(f"Email: {self.email}")
        if self.age:
            print(f"Age: {self.age}")

    def greeting_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
