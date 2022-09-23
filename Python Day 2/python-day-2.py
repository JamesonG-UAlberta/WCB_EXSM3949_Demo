#Data Structures

#Tuples
#A tuple is an ordered collection of data
#Unchangeable and allows for duplicate values
#Like a list, a tuple index starts at 0
#A tuple can contain mixed data types
#Tuples can be nested
#Tuples cannot be sorted

my_tuple = ("cat", "dog", "cat", "turtle", 5, True)
print(my_tuple)

#In a tuple with one item, be sure to include a comma after the item
my_tuple2 = ("cat",)

a_tuple = (("Nickelback", "Curb", "May 16, 1996"), ("Nickelback", "The State", "September 1, 1998"))

print(a_tuple[1][0])

#A way to edit a tuple is to convert the tuple into a list, make the changes, and then convert it back to a tuple

#Tuple Unpacking
a_tuple3 = ("Nickelback", "Curb", "May 16, 1996", 100000)
(band_name, album_name, *my_list) = a_tuple3
print(band_name)
print(my_list)

#Sets
#A set is an immutable set of data, with unique values
#You cannot create an empty set with {}, because it creates a dictionary
#Instead, you can use set() to declare an empty set
#Since a set is immutable, you cannot have mutable data-types inside it
#Sets are unordered, so you cannot use index values to access data
#To access data in a set, you would need to use a loop

my_set = { 0, 1, 2, 3, 0, 0, 0 }
print(my_set)

#Adding and Removing Set Items
my_set.add(4)
print(my_set)

my_set.remove(0)
print(my_set)

#Updating Sets
my_set2 = { 99, 999 }
my_set.update(my_set2)
print(my_set)

#Union Sets
my_set3 = my_set.union(my_set2)
print(my_set3)

#Discarding Set Values
my_set.discard(4)
print(my_set)

#Discard will not throw an error, if the value does not exist. Remove will have an error if the value does not exist.

#Set Popping
print(my_set.pop())

#Del and Clear in Sets
#Del deletes a set entirely
#Clear makes the set empty

#Dictionary
#Dictionaries are unordered and changeable
#Dictionaries work off a key-value pair
my_dictionary = { "Cat":"A small domestic feline mammal."}
print(my_dictionary.get("Cat"))
#For the get() method, you provide a key, and if it exists, a value is returned
print(my_dictionary["Cat"])

#The get() method will not throw an error if a key does not exist, it will instead return None

#The get() method can be given a default value if we don't want None to be returned

print(my_dictionary.get("Dog", "No key exists of Dog"))
    
#Updating Values in Dictionaries
my_dictionary.update({"Cat":"Something else"})
print(my_dictionary["Cat"])

my_dictionary.update({"Dog":"Woof woof"})
print(my_dictionary["Dog"])

#Removing Items From a Dictionary
my_dictionary.pop("Cat")
print(my_dictionary.get("Cat"))

del my_dictionary["Dog"]
print(my_dictionary.get("Dog"))
#Be careful when using del, as del can delete your entire dictionary

#Other Dictionary Methods
#Clear: makes your dictionary empty
#Copy: copies your dictionary to another dictionary
#Keys: fetches all the keys in a dictionary
#Values: fetches all the values in a dictionary
#Items: fetches all key-value pairs in a dictionary

#Enum
#Enums is short for enumerations. A set of symbolic names are bound to unique, constant values.
#Example: Python Fundamentals is bound to the course code 3949
#Enums are not built in to Python, we need import it

import enum

class Menu(enum.Enum):
    burger = 1
    fries = 2
    soft_drink = 3
    milkshake = 4
print(repr(Menu.fries))

class Course(enum.Enum):
    HTML_fundamentals = 3932
    python_fundamentals = 3949
    react_fundamentals = 3939
 
#Accessing enum members
#We can access by value, or by name
print(Course["HTML_fundamentals"]) 
print(Course(3932))  

#Comparing enum members
#By identity (is, is not)
#By equality (==, !=)

print(Course.react_fundamentals is not Course.python_fundamentals)
print(Course.HTML_fundamentals == Course.react_fundamentals)

#Datetime
import datetime

print(datetime.datetime.now())

my_date = datetime.datetime(2023, 5, 24, 15, 30, 25, 123456)
#year, month, day, hours, minutes, seconds, microseconds, timezone
#year, month and day are required, all other fields are optional 
print(my_date)  

#File I/O
#Syntax: file_object = open(file_name, access_mode)
#Access modes:
#1. Read: Read the contents of the file, but cannot make changes. Read will throw an error if file does not exist.
#2 Append: Opens a file to add information to it. If the file does not exist, it will create the file.
#3 Write: Opens a file for writing, will overwrite file existing content. Will create a file if it does not exist.
#4 Create: Creates a file, will throw an error if file does exist.

#File Reading
my_file = open("example.txt", "r")
for line in my_file:
    print(line)
    
#file_object.read() returns the entire document
#file_object.read(x) returns the first x characters in a document
#file_object.readline() returns the first line of a document

#File Writing
my_file2 = open("example2.txt", "w")
my_file2.write("This is an example of me writing to a file!")

#Closing a File
my_file.close()
my_file2.close()
#It is important to close a file because changes to a file may not necessarily appear until it is properly closed. 

#JSON in Python
import json

#Converting JSON to Python
json_string = '{"name":"Bob", "profession":"dentist"}'
changed_to_python = json.loads(json_string)
#json.loads will convert our JSON string into a dictionary
print(changed_to_python["profession"])

#Converting Python to JSON
py_dict = {"name":"John", "profession":"Engineer"}
changed_to_json = json.dumps(py_dict)
print(changed_to_json)

