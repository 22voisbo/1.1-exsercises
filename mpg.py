#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program yeet")
print()

# get input from the user
miles_driven= float(input("Enter miles driven in a day:\t\t"))
gallons_used = float(input("Enter gallons of gas used in a day:\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 3)
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
str(mpg)
print()
print("Bye")


