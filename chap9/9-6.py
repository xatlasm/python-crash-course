# Ice Cream Stand

class Restaurant():
    """Model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(self.restaurant_name.title() + ' is a ' + self.cuisine_type.title() + ' restaurant.')

    def open_restaurant(self):
        """Open the restuarant"""
        print(self.restaurant_name.title() + ' is now open!')

    def increment_number_served(self, serve):
        """Increment number served"""
        self.number_served += serve

class IceCreamStand(Restaurant):
    """Model an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Init from parent"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def display_flavors(self):
        """print flavors"""
        for flavor in self.flavors:
            print(flavor)
        
    
    def add_flavor(self, flavor):
        self.flavors.append(flavor)

bj = IceCreamStand('ben and jerrys', 'ice cream')
bj.add_flavor('rocky road')
bj.display_flavors()