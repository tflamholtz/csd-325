# Tzvi Flamholtz
# Assignment 7.2
# 07/26/2026
# This program takes in a city and country and returns a string formatted as "City, Country"

# create function that takes in a city and country and returns a string formatted as "City, Country"
def city_country(city, country, population=None, language=None):

    result = f"{city}, {country}"
    
    # if statements to check if population and language are provided, and if so, add them to the result string
    if population is not None:
        result =  result + f" - population {population}"
    if language is not None:
        result = result + f" - language {language}"
   # return the result string
    return result

# Example usage of the function
print(city_country("Miami", "USA"))
print(city_country("Paris", "France", 2050000))
print(city_country("Toronto", "Canada", 3300000, "English"))

# Title: city_functions.py
# Author: Tzvi Flamholtz
# date: 7/26/2026