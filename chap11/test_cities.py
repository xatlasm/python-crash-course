import unittest
from city_functions import city_country

class TestCities(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Tests country-city pairs"""
        formatted_pair = city_country('santiago','chile')
        self.assertEqual(formatted_pair,'Santiago, Chile')
    
    def test_city_country_population(self):
        """Tests country-city-population"""
        formatted_triple = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_triple,'Santiago, Chile - population 5000000')

unittest.main()