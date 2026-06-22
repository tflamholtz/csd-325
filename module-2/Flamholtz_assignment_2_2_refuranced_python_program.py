#Program that converts gallons to liters


def main():
    #Display intro screen
    intro()

    try:
        #Get the number of gallons
        gallons = float(input("Enter the number of gallons :"))

        #Convert the gallons to liters
        gallons_to_liters(gallons)
    except ValueError:
        print("An exception occurred, try again by entering only a number")
        print()
        main()


    except:
        print("An exception occured, try again by entering only a number")
        print()
        main()


    #The intro function displays an introductory screen
def intro():
    print("This program converts measurments")
    print("in gallons to liters")
    print("For referance the formula is")
    print("1 gallon =  3.785412 liters")
    print()


    #The gallons_to_liters function accepts a number of gallons
    #and displays the equivalent number of liters

def gallons_to_liters(gallons):
    liters = gallons *  3.785412
    print(f"That converts to {liters} liters")


    #Call the main function
main()
