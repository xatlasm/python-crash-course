#Employee

class Employee():
    def __init__(self,first_name,last_name,salary):
        """Stores first name, last name, and salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self,raise_amount=5000):
        """Gives a raise"""
        self.salary = self.salary + raise_amount

mitch = Employee('mitch','atlas',100000)
print(mitch.salary)
mitch.give_raise()
print(mitch.salary)
print()
mitch.give_raise(10000)
print(mitch.salary)