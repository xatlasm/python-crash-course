#Users

class User():
    """Builds a user profile"""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize names"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

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

mitch = User('mitchell','atlas',28,'male')
yuka = User('yuka', 'mantani', 30, 'female')

mitch.describe_user()
mitch.greet_user()
yuka.describe_user()
yuka.greet_user()