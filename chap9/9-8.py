#Privileges

class Privileges():
    """stores privileges for a user"""
    def __init__(self, privileges):
        """initialize"""
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin():
    """Builds an admin user"""
    def __init__(self, first_name, last_name, age='',gender=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.privileges = Privileges(['can add post'])

    def describe_user(self):
        """Describe the user"""
        print('first name: ' + self.first_name.title())
        print('last name: ' + self.last_name.title())
        print('age: ' + str(self.age))
        print('gender: ' + self.gender.title())
        print('privileges: ' + str(self.privileges.privileges))

me = Admin('mitchell', 'atlas')
me.describe_user()
me.privileges.show_privileges()