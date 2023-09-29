#! python3
# Demonstration of If/Else statements
#
# An If else statement not only executes a block of code if the condition is true,
# but presents an alternative statement to do if the statement is false


# How to do an IF...else statement Example 1:
# Demonstrates how an if statement makes decisions
# Note the : at the end of the if statement and
# the indenting to indicate the block of code that is
# in the if statement
print("=============================")
print(" Ex1: If...Else statement    ")
print("=============================")
if True:
  print("the condition is True")
  print("Any code in this block is executed")
else:
  print("the condition is false")
print("=============================\n\n\n")




# How to do an IF statement Example 2:
# In this example, a condition is checked and the boolean value of True or False
# is stored into the variable value
print("=============================")
print(" Ex2: If else statement      ")
print("=============================")
a = 10
b = 5
value = a==b
print(value)
if value:
  print("The if statement is executed because")
  print("the condition is true")
else:
  print("This is the alternate message")
  print("Because the statement was false")
print("=============================\n\n\n")

 
  

# How to do an IF statement Example 3:
# In this example, the conditional statement is checked right 
# in the if statement itself
print("=============================")
print("     Ex2: If statement       ")
print("=============================")
a = 10
b = 5
if a == b:
  print("The if statement is executed because")
  print("the condition is true")
else:
  print("False")
print("=============================\n\n\n")
