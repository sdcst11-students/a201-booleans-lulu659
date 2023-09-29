#! python3
# this file demonstrates an if...elif statement

# An if...elif is short for if...else...if
# It offers an alternative condition to be checked only if the
# first condition is not met.
# Consider the examples:


# Using separate if statements:
print("=============================")
print(" Ex1: Separate if statements ")
print("=============================")
bobLikesHockey = True
bobLikesSoccer = True
bobLikesFootball = False

if bobLikesHockey:
  print("Bob likes Hockey")

if bobLikesSoccer:
  print("Bob likes Soccer")

if bobLikesFootball:
  print("Bob likes Football")
  
print("=============================\n\n\n")




# How to do an If...elif statement Example 2:
# Note that the elif conditions are only checked if every
# condition above it is False
print("=============================")
print(" Ex2: If..Elif statement     ")
print("=============================")
bobLikesHockey = True
bobLikesSoccer = True
bobLikesFootball = False
if bobLikesHockey:
  print("Bob likes hockey")
elif bobLikesSoccer:
  print("Bob does not like hockey, but likes Soccer")
elif bobLikesFootball:
  print("Bob does not like hockey or soccer, but likes football")
else:
  print("Bob doesn't like any of the conditions that we checked")
print("=============================\n\n\n")

 
