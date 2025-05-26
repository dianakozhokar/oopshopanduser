from user_module import User
from admin_module import Admin

user1 = User("Alice", "Brown", "alice@example.com", 25)
user2 = User("Bob", "Smith", "bob@example.com", 30)
user3 = User("Charlie", "Johnson")

user1.describe_user()
user1.greeting_user()
print()

user2.describe_user()
user2.greeting_user()
print()

user3.describe_user()
user3.greeting_user()
print()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
print()

admin_user = Admin("Admin", "User", "admin@example.com", 40)
admin_user.describe_user()
admin_user.priv.show_privileges()
