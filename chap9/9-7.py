# Admin
class User():
    """Builds a user profile"""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize names"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Describe the user"""
        print('first name: ' + self.first_name.title())
        print('last name: ' + self.last_name.title())
        print('age: ' + str(self.age))
        print('gender: ' + self.gender.title())

    def greet_user(self):
        """Greet the user"""
        print('Greetings, '+ self.first_name.title() + ' ' + 
        self.last_name.title() + '.')

    def increment_login_attempts(self):
        """Increment login attempt counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempt counter"""
        self.login_attempts = 0

class Admin(User):
    """Builds an admin user"""
    def __init__(self, first_name, last_name, age='',gender=''):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = []

    def show_privileges(self):
        print(self.privileges)
    
    def add_privileges(self,privilege):
        self.privileges.append(privilege)

adminme = Admin('mitchell','atlas')
adminme.add_privileges('can add post')
adminme.add_privileges('can delete post')
adminme.describe_user()
adminme.show_privileges()