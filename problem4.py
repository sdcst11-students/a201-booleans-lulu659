#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""

def triangleType(a, b, c):
    sa = pow(a, 2)
    sb = pow(b, 2)
    sc = pow(c, 2)
    if (sa == sc + sb or sb == sa + sc or sc == sa + sb):
        print("That is a right triangle.")
    elif (sa > sc + sb or sb > sa + sc or sc > sa + sb):
        print("That is a obtuse triangle.")
    else:
        print("That is a acute triangle.")

a = float(input("Enter a number: "))
b = float(input("Enter a second number: "))
c = float(input("Enter a third number: "))
triangleType(a, b, c)