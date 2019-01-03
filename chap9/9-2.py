#Three restaurants

class Restaurant():
    """Model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(self.restaurant_name.title() + ' is a ' + self.cuisine_type.title() + ' restaurant.')

    def open_restaurant(self):
        """Open the restuarant"""
        print(self.restaurant_name.title() + ' is now open!')

mcd = Restaurant('mcdonalds', 'hamburger')
il = Restaurant('illini lounge', 'wing')
yoshi = Restaurant('yoshinoya', 'japanese')

mcd.describe_restaurant()
il.describe_restaurant()
yoshi.describe_restaurant()