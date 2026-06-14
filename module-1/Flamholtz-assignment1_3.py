# Tzvi Flamholtz, 6/14/2026, assignment 1.3

# Python program for beer song count down

# Try/except to handle invalid input
while True:
    try:
        # Get number of bottles and set it as the count
        bottles = int(input("How many bottles of beer on the wall?"))
        break
    except ValueError:
        print("Please enter a valid number")

#while loop to itterate as long as there are still bottles
while bottles > 0:

    #if else statement for correct wording when only one bottle left
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall,{bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles-1} bottle(s) of beer on the wall.")
        print()
    else:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("take one down pass it around, 0 bottles of beer on the wall.")

    # update count
    bottles -= 1

print()
print("Time to buy more bottles of beer.")
    
