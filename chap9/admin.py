from user import User

class Privileges():
    """stores privileges for a user"""
    def __init__(self, privileges):
        """initialize"""
        self.privileges = privileges

    def add_privileges(self,privilege):
        self.privileges.append(privilege)

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    """Builds an admin user"""
    def __init__(self, first_name, last_name, age='',gender='', privileges=[]):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = Privileges(privileges)