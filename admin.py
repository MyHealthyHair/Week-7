class User():
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


eric = Admin('eric', 'matthes', 'e_matthes')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()
