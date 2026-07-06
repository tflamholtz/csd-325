# Tzvi Flamholtz
# Assignment 4-2
# 07/05/2026
# This program reads a data file
# and displays a plot of the highs or lows



import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Added system exit
import sys

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    # Added list for lows
    dates, highs , lows = [], [], []
    for row in reader:

        # Added try except clause to deal with bad data
        try:
            
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

            # Added code to gather the lows
            low = int(row[6])
            lows.append(low)

        except ValueError:
            print(f"Missing or invalid data for row: {row}")
            continue
            

# Created a function to display the highs if selected
def plot_highs():

    # Plot the high temperatures.
    # plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Created a function to display the lows if selected
def plot_lows():

    # Plot the low temperatures.
    # plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue', linewidth=2)

    # Format plot.
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel("")
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()

# Created a main function to display options and call the proper data selected
def main():
    while True:
        print("\n=== Weather Menu ===")
        print("Please select the number for which option you would like.")
        print("1. High Temperatures")
        print("2. Low Temperatures")
        print("3. Exit")

        choice = input("select an option (1-3): ").strip()

        # If elif statement to display choice
        if choice == '1':
            plot_highs()
        elif choice == '2':
            plot_lows()
        elif choice == '3':
            print("\nExiting program. Have a great day!")
            sys.exit()
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

main()

# Assignment 4-2
# Author: Unknown (presented by course)
# Modified by: Tzvi Flamholtz
# 07/05/2026
