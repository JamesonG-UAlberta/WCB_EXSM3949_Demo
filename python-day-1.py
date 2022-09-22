#Python is a whitespace delimited language, this means it relies on indentation to indicate
#the beginning or end of a statement.
#Python's interpretor will determine a variable type, so no type declaration is needed
#This is an example of a single line comment
"""
this is an example
of a multiline comment
"""
"""
Variable Names in Python
1. Variable names should describe the data they contain
2. Variable names can only be one word (no spaces)
3. You can only use letters, numbers, and underscores
4. Variables cannot begin with a number
The Python style guide recommends that you use snake-case variable names (words are separated
by underscores)
"""

#Print Statements
from xmlrpc.client import Boolean


print("This is an example of a simple print statement")
myText = "a multiple value print statement"
print("This is an example of", myText)
print()

#Escape Sequences
print('Bob\'s lunch')

myText2 = """this is a multiline
variable
assignment
"""
print(myText2)

#String Concatenation
myName = "Bo"
print("Hello, my name is " + myName)

#Format Strings
fruit = "Banana"
print(f"My favorite fruit is a {fruit}")

#Finding Words in Strings
myText3 = " This is my line of text. "
print("something" in myText3)
print("something" not in myText3)

#Removing Whitespace
print(myText3.strip()) #strips whitespace from both ends
print(myText3.lstrip()) #strips whitespace from the left
print(myText3.rstrip()) #strips whitespace from the right

#String Length
print(len(myText3))

#Upper and Lower
print(myText3.upper())
print(myText3.lower())

#Replacing Characters
print(myText3.replace("i", "o"))

#Split
breakfast_menu = "eggs bacon ham toast"
print(breakfast_menu.split(" "))

#Decisions
if 5 > 6:
    print("True")
elif 5 < 6:
    print("Error!")
else:
    print("False")
    
#Loops
counter = 0
while counter < 5:
    print(counter)
    counter += 1
    
pets = ["cat", "dog", "hamster"]
for pet in pets:
    print(pet)

#Ranges
for number in range(3,6): #first number is included in count, last number is not
    print(number)

for number in range(3): #number in brackets is last number, count starts and includes 0
    print(number)

#Get
occurences = {} #this is tuple
for word in myText3:
    occurences[word] = occurences.get(word, 0) + 1
print(occurences)

#Handling Exceptions
#try, except, else, finally
def division(num1, num2):
    try:
        result = float(num1) / float(num2)
        return result
    except ZeroDivisionError:
        print("You cannot divide by zero!")
division(5,0)
my_float = division(5,3)
format_float = "{:.5f}".format(my_float)
print(format_float)

#Functions
def adder(num1, num2):
    """_summary_
        Adds and multiplies two numbers together and prints them.
    Args:
        num1 (integer): Any positive or negative integer
        num2 (integer): Any positive or negative integer
    """
    print(num1 + num2)
    print(num1 * num2)
adder(2,3)

#Docstrings
#Docstrings are triple-quoted strings that come right after the def of a function
#Docstrings describes what the function does 

#Scope
"""
def add_numbers(num1, num2):
    num_sum = num1 + num2
    return num_sum
"""
#print(num_sum) num_sum cannot be accessed here, because it is out of scope
#num_sum can only be accessed WITHIN add_numbers()

num1 = 5
def add_numbers(num1, num2):
    global num_sum 
    num_sum = num1 + num2
    return num_sum
#print(num_sum)

#Lists
grocery_list = [["Budweiser", "Corona"], ["bacon", "porkchops"], ["bread", "pita"], [2,1], [True, False]] 
print(grocery_list[0][1])
print(grocery_list[0:3])

color_list = list(("red", "blue", "green"))
print(color_list)

#Append and Insert
color_list.append("grey") #adds a value to the back of list
print(color_list)

color_list.insert(1, "black")
print(color_list)

#Extend concatenates lists
color_list2 = ["pink", "orange"]
color_list.extend(color_list2)
print(color_list)

print(color_list + color_list2)

#Remove
color_list.remove("pink")
print(color_list)

#Clear
#color_list.clear()
print("red" in color_list)
print("pink" in color_list)

#Index Keyword

print(color_list.index("grey"))

#Sort and Reverse
my_list = [1, 3, 2]
sorted_list = my_list.sort()
print(sorted_list)
#Sort will order a list in ascending value
#Reverse will order a list in descending value

#Imports - python users can import modules made by the community for various functionalities
import random
print(random.randrange(0,100))

#Numbers in Python
#int, float, complex

my_long_float = 4.123456789
print(round(my_long_float, 5))

#Min/Max
print(min(0,1,2))
print(max(0,1,2))

#Advanced Math Functions
import math
print(math.pow(2,10))
print(math.factorial(5)) #5 * 4 * 3 * 2 * 1

#math.ceil - rounds number up to the nearest integer
#math.floor - rounds a number down to the nearest integer
#math.sqrt - finds the square root of a number
#math.e - Euler's number
#math.inf - positive infinity
#math.pi - returns the value pi
#math.nan - returns a "not a number" value

my_letter = "a"
if my_letter == math.nan:
    print("Not a number")
    
#Unit Testing
#Unit testing is like testing over a component of an airplane
#Integration testing is like testing all components of an airplane
"""
Why Write Good Unit Tests?
1. When we refactor code, it is difficult to pinpoint the origin of a bug. Unit tests tell us
the precise location of where our functionality fails. 
2. Quickly test a variety of test cases.
3. Unit tests are a good form of documentation. Another programmer can figure out what your code
is supposed to do, based off the unit test.
4. Good unit tests can be reused in future projects.
"""

"""
Good Unit Tests Should Be:
1. Easy to write, but comprehensive
2. Easy to read
3. Reliable - tests should only fail if there is a bug, not due to the environment
4. Fast to run
5. Unit test - it should only test a single unit, it should not be a integration test
"""




















