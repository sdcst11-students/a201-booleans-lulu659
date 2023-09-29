## SDSS Computing Studies Python Assignment
### Assignment #004a Introduction to Boolean Variables (Total Marks 15)

Objectives:
* Differentiate boolean variables from int, float and str
* Identify Uses for Boolean type Variables
* Evaluate Boolean Expressions

Imagine you open up your phone settings.  There are a lot of different buttons or "toggles" that 
you might be see.  For example:
![toggle image](https://cdn.dribbble.com/users/6179/screenshots/726313/toggle-switches.jpg)

This is a great example of a Boolean variable.  A boolean stores only 2 possible values, unlike
a str, float or int that can store almost an infinite number of different possible values. There
are many different ways to think of these 2 states:

on or off \
yes or no \
1 or 0 \
Enabled or Disabled \
True or False \

Python uses the values **True** or **False** as the values that a boolean can store
```
#Example
hasKey = True
doorLocked = False
```
Note the absence of quotation marks around the values being stored into the variables
*hasKey* and *doorLocked*.  Also, the capitalization is important - the first character
must be upper case.

There are many different ways that you might see a Boolean used or how you might use them:
* To see if a setting has been enabled or disabled. This is sometimes called a toggle or flag
* To answer a simple Yes/No question and decide what to do next.  Many of you included something like this in your Peanut Butter Sandwich assignment.  If you have 2 pieces of bread, you can proceed with making the sandwich. If no, then you need to consider acquiring some bread
* To keep track of a single state that could be either a Yes or No
* To check a *conditional statement*

### Conditional Statements ###
A conditional statement is one that is evaluated as True or False. You can kind of think of it as a question.
There are several different conditional operators

Consider 2 variables or values: \
```
a == b    Checks to see if the 2 values are equal
a > b     Checks to see if a is greater than b
a < b     Checks to see if a is less than b
a >= b    Checks to see if a is greater than or equal to b
a <= b    Checks to see if a is less than or equal to b
a != b    Checks to see if a and b are not equal
a < b < c Python also supports multiple comparisons using the less than and greater than symbols.  Not many other languages can do this
```
These all work for both numerical values (int and float) as well as for strings

"in" is a special conditional operator that compares a number or string with a number of possible values.  It can be used to see if one string
can be found somewhere in the other string. These 2 strings are sometimes referred to as the
"needle" and the "haystack" \
It can also be used to see if a number is within a specified range, equal to or greater than the first value,
but less than the second value.
```
examples:

Strings
"needle" in "haystack"
"i" in "team" is evaluated as False
"fun" in "funeral" is evaluated as True

Numbers
10 in range(1,100) is True
1 in range(1,100) is True
100 in range(1,100) is False
```

### IF and IF/ELSE statements ###
One important use for conditional statements is the "if" statement, or the "if else" statement.  These control the flow of the program, and introduce to our first use of indenting in Python to identify blocks of code. 
* Open up example1.py to see how an if statement works.
* Open up example2.py to see how an if..else statement works
* Open up example3.py to see how an if...else...if statement works

### 4 Tasks
### 5 Problems
### Total mark available: 15
All tasks should be completed.
Problems are optional.

##### Task 1
Open the file called task1.py \
Have the user input a number. \
Determine if the number is larger than 100 \
If it is, the output should read "The number is larger than 100" \
(2 points) 

##### Task 2
Open the file called task2.py \
Have the user input a number \
Determine if the number is positive, negative or 0 \
Check the code for a list of valid output results \
(2 points)

##### Task 3
Open the file called task3.py
Have the user enter a number.
Use an if...elif statement to determine if the number is
a) larger than 1000
b) larger than 100
c) larger than 10
d) larger than 0
Output must match one of the valid output statements listed in the program
(2 points)

##### Task 4
Open the file task4.py
Have the user enter in a sentence.
Check to see if the word "password" is located in the sentence.
(2 mark)


##### Problem 1
Open the file problem1.py
Have the user enter a number
Determine if the number is an even number.
Hint: Use the modulus, which determines the remainder when two numbers are divided
(1 mark)

##### Problem 2
Open the file problem2.py
Have the user enter a number
Determine if the number is an integer value.
(1 mark)

##### Problem 3
Open the file called problem3.py
Have the user enter a username
If the username is not "admin" then tell them it is an invalid user,
but if it is, then ask them for a password
If they get the password correct (password is 12345password) then display
the message "Access granted")
(1 marks)

##### Problem 4
Open the file called problem4.py
Have the user enter in 3 numerical values, representing the side lengths of a triangle.
Determine if the values are close enough to make a right triangle.
(It is close enough if the percent difference between the actual and the calculated 
measurement is less than 2%
(2 marks)

##### Problem 5
Open the file called problem5.py
In math, if a quadratic equation is in the format
ax^2 + bx + c = 0, the discriminant can be calculated as
b^2 - 4 * a * c
If the discriminant is a perfect square, the equation can
be factored.  Furthermore, if the discriminant is negative,
then the equation has no solutions.
Have the user enter in values for a, b and c and then 
tell them if there are solutions as well as if the equation can
be factored.
(2 marks)
