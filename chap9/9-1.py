#Restaurant
class Restaurant():
    """Model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(self.restaurant_name.title() + ' is a ' + self.cuisine_type.title() + ' restaurant.')

    def open_restaurant(self):
        """Opens the restuarant"""
        print(self.restaurant_name.title() + ' is now open!')

restaurant = Restaurant('chipotle','mexican')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()