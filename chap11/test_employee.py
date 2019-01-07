import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class"""

    def setUp(self):
        """Defines test case"""

        first_name = 'John'
        last_name = 'Doe'
        salary = 100000
        
        self.employee = Employee(first_name,last_name,salary)

    def test_give_default_raise(self):
        """Tests giving default raise"""
        oldsalary = self.employee.salary
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,oldsalary+5000)

    def test_give_custom_raise(self):
        """Tests giving custom raise"""
        oldsalary = self.employee.salary
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,oldsalary+10000)

unittest.main()