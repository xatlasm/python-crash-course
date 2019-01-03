#Number served

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
        
restaurant = Restaurant('chipotle','mexican')
print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)
restaurant.increment_number_served(100)
print(restaurant.number_served)