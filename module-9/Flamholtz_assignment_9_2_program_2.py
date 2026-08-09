# Tzvi Flamholtz
# Assignment 9.2
# 08/09/2026
# This program gets data from an API and prints the JSON response in a readable format.


# Import neccesary libraries
import requests
import json

# Make a GET request to the API
response = requests.get('http://anapioficeandfire.com/api/houses/1')

# Print the status code to verify connection
print(response.status_code)

# Print the JSON response from the API
print(response.json())

# Define a function to print JSON data in a formatted way
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

# Call the function to print the JSON response in a readable format
jprint(response.json())

# Title: Assignment 9.2
# Author: Charlie Custer
# Modified and commented by: Tzvi Flamholtz
# Date: 08/09/2026