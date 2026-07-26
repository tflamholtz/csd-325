# Tzvi Flamholtz
# Assignment 7.2
# 07/26/2026
# This program tests the city_country function from city_functions.py




# Import the unittest module and the city_country function from city_functions.py
import unittest
from city_functions import city_country

# Create a test case class that inherits from unittest.TestCase
class TestCityCountry(unittest.TestCase):

    # Create a test method to test the city_country function
    def test_city_country(self):

        # Test the city_country function with a city and country
        formated_city = city_country("Miami", "USA")
        self.assertEqual(formated_city, "Miami, USA")

if __name__ == '__main__':
    unittest.main()

# Title: test_cities.py
# Author: Tzvi Flamholtz
# date: 7/26/2026
    