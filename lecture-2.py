# Hello! This line is a comment, meaning it not treated as code by Python.
# Our code editor also changes the color letting us know these lines are different.
''' 
We can also have comments that 
span several lines that are 
surrounded by these triple 
single quotes.
'''


# this is what our hello world looked like from last class
print("hello world")

# A variable is associated with a value, which is the information associated with that variable
# here, we are associating the variable named message with the "Hello Python world!" text
message = "Hello Python world!"

#now we can use the variable in our print statement
print(message)

# Reserved words in Python. Try uncommenting some and see what color they are
#return
#False
#None
#True
#and
#assert
#as
#break
#class
#continue
#def
#del
#elif
#else
#except
#finally
#for
#from
#global
#if
#import
#in
#is
#lambda
#nonlocal
#not
#or
#pass
#raise
#return
#try
#while
#with
#yield

# Variables

#integer
student_count = 19

#float
average_gpa = 3.5

#string
class_name = 'CYB 2004 - Secure Software Development I'

#boolean
is_spring_semester = True



#now with variable type hints
#integer
student_count: int = 19

#float
average_gpa: float = 3.5

#string
class_name: str = 'CYB 2004 - Secure Software Development I'

#boolean
is_spring_semester: bool = True


# How big can the floating point go?
'''
import sys
max_f = sys.float_info.max
print(max_f)
max_f += 1
print(max_f)
'''

#some string examples
my_string = "This is a simple string"
my_string2 = 'this is also a string'
my_string3 = '          this string has a "quote inside" of a quote            '
my_string4 = "This 'really' \"mixes\" '\''things'\'' up."

#Uncommend the following to see how they look when printed.  Can you guess?
'''
print(my_string4)
print(my_string2.title())
print(my_string.upper())
print(my_string3.lstrip() + ":") #adding the ":" demonstrates the white space that is still left on the right of the string
print(my_string3.rstrip())
print(my_string3.strip())
'''

#different ways of doing the same thing, printing the average GPA
'''
print("The average GPA is " + str(average_gpa))
print("The average GPA is %.1f" % (average_gpa))
print("The average GPA is {}".format(average_gpa))
print(f"The average GPA is {average_gpa}")
'''


# NAME CASES
# Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.


# FILE EXTENSIONS
#Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

# Do some math
'''
print(4 + 5)
print(4 * 5)
print(4 / 5)
print(4 // 5)
print(4 % 5)
'''


#explicit casting 
i = int(3.0) 
assert(i == 3)

i = int(3.9)
assert(i == 3)

#some strings
'''
string_a = "This is my favorite string. "
string_b = "Oh, ok. wow. I didn't know we were playing favorites."
print(string_a + string_b)

string_blah = "blah "
print(string_blah * 5)
'''


'''
Definition of savings and total_savings
savings = 100
total_savings = 150
Fix the printout
print("I started with $" + savings + " and now have $" + total_savings + ". Awesome!")
Definition of pi_string
i_string = "3.1415926"

Convert pi_string into float: pi_float
'''

