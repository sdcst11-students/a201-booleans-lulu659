#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

x = input("Enter a number: ")
if x[0] in ["+", "-"]:
   if x[1:].isdigit():
      print("The number is an integer.")
   else:
      print("The number is not an integer.")
else:
   if x.isdigit():
      print("The number is an integer.")
   else:
      print("The number is not an integer.")