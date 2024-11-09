"""Write a program which asks the user a string
and prints out the length of the string."""

"""len() -> calculates the length of the string"""

#text = str(input("Please enter your string: "))

#print("Your value is: ", len(text))

"""Ask the user two string (string_a, string_b) and
then print out their concatanation (i.e., string_a is hello and 
string_b is bye the output must ne hellobye"""

#string_a = str(input("Please enter string a: "))
#string_b = str(input("Please enter string b: "))

#print("Result is: ", string_a + string_b)

"""BYTES AND BTYE ARRAYS"""

"""Hello -> 01011010101..."""

#print(b"Espa\xc3\xb1a".decode("utf-8"))

"""Bytes can convert numbers to characters"""
#print(bytes([65, 66, 67, 97, 98, 99]))

"""65 -> A
   97 -> a"""

"""BOOLEANS"""

"""Booleans are ONLY come in two (2):
- True
- False
"""

#print(type(True))
#print(type(False))

#print(False + False)

#print(issubclass(bool, int))

"""* LISTS"""

""" This is annoying and time consuming"""
#int_a = 45
#int_b = 34
#inc_c = 44

# To define a list do the following
int_list = [45, 34, 44]

# This prints out the entire list
#print(int_list)

# To print out 45, we access the index value
# index of 0 -> 45
# index of 1 -> 34
# index of 2 -> 44

#print(int_list[0])
#print(int_list[1])
#print(int_list[2])

# This would be an IndexError
#print(int_list[45])

# Lists can contain a variety of data types
block = [42, "Apple", True, {"name": "Daniel"}, [1, 3.14, 1e8]]

#print(block)

"""** Building Lists"""

# Literal definition
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List of strings
fruits = ["Apple",
          "Banana",
          "Kiwi",
          "Grape"]

# A matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# A list of functions
function = [print, len, range, type, enumerate]

# empty list
empty_list = []

#print(empty_list)

# Add value 5 to the END OF THE LIST
empty_list.append(5)

#print(empty_list)

# Using list() constructor
# int(5), float(3.14)

#print(list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))

# This would generate a LIST OF CHARACTERS
#print(list("Innsbruck"))

# Generate lists in a pythonic fashion
# f(x) = x ** 2


#print([x ** 2 for x in range(1, 11)])

# Where:
# x ** 2: is my function
# for: its the for loop in disguise
# x: we define the loop variable
# in: which values to loop
# range(1,11) : values from 1 to 10

# If we define range(a, b) this means
# min value -> a
# max value -> b - 1

"""* Indexing"""

# Indexing is accessing an array value
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# To access list from L -> R, start counting from 0
# To access list from R -> L, start counting from -1 and subtract -1 everytime
# you want to move

# print(digits[-1])
# print(digits[-2])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(matrix[1][1])

# Getting more than one value at a time

# This basically prints first 3 values
# index values of 0, 1, and 2
#print(digits[0:3])

# prints last three values
#print(digits[-3:])

# digits[start:end:step]
# start: the index to start
# end: is the last index value [NOTE: only index values
# up to end-1 will be operated upon]
# step: how big my jumps should be with each index

#print(digits[::3])

#EXERCISE: Please write me the digits in the digits array
#a) Which are EVEN (digit % 2 == 0)
#b) Which are ODD  (digit % 2 == 1)

# Prints out only EVEN values
#print(digits[::2])
#print(digits[0:-1:2])
#print(digits[0:len(digits):2])

#print(digits[1::2])

letter = ["A", "a", "B", "b", "C", "c", "D", "d"]

# EXERCISE: please create two arrays where one contains ALL uppercase and one
# contains ALL lowercase

#print(letter[::2])
#print(letter[1:None:2])

"""** Growing and Shrinking List"""

number = [1, 2, 3, 4, 7, 6, 4, 5, 6, "banana", 7, 5,  2, 1, 2, 3, 7, 8]
#print(number)
number[0] = "one"

#print(number[len(number)-1])

#number.append("end")

number[number.index("banana")] = 9999

#print(number)

num = [1, 2, 3, 4, 5, 6, 7]

num[1:3] = [22, 33, 44]

#print(num)

"""DICTIONARY"""

Languages = {
    'Cplusplus' : '.cpp',
    'Python'    : '.py',
    'Text File' : '.txt',
    'Document'  : '.docx',
    'Excel'     : ".xlsx"
}

#print(Languages["Excel"])

#print(type(Languages))

Pause = dict([
    ("Lunch Break", "Now")
])

#print(Pause["Lunch Break"])

d = {
    False:"a",
    False:"b",
    False:"c"
}

#print(d[False])

# Dictionaries DON'T HAVE INDEX, THEY HAVE KEYS

# Building Dictionaries Incrementally

person = {}
#print(type(person))

person["fname"] = "John"
person["lname"] = "Doe"

#print(person["fname"])

person["pets"] = {
    "dog" : "Fido",
    "cat": "Sox"}

#print(person["pets"]["cat"])

foo = {42 : "aaa",
       2.78 : "bbb",
       True : "ccc"}

cd = {int : 1,
      float : 2,
      bool: 3}

#cd[int]

# Almost everything goes in a dictionary
# 1. A Key should only happen once

# RECAP
# int, float, string, byte, bool, list, dict

# CONDITIONAL STATEMENTS

# Syntax

# if <expr>:
#     <statement>

# Expression is evaluated based on its BOOLEAN

if False == True:
    print("This statement is True")
    print("This is also evaluated")

#print("This is always printed")

x = 0
y = 5

#if x < y:
    #print("x is less than y")

# if x:
#     print("x is True")
#
# if y:
#     print("x is True")

# Logic Operations
# and (if two are true it will be True, else its False
# or (if at least one is true it will be True, else False)
# not (if True then False, if False then True

#if not x:
    #print("x is nullified")

if x and y:
    print("what would happen?")

# x is zero, therefore it is FALSE
# y is five, therefore it is TRUE
# TRUE and FALSE = FAlSE

#if "ave" in "gravel":
    #print("Yes")

#if "apple" in ["banana", "mango", "strawberry"]:
    #print("Yes times 2")

# if "a" in ["a", "b"]:
#     print("a is in the list")
#
#     if "b" in ["a", "b"]:
#         print("a and b are in the list")

# value = float(input("Please enter a number: "))
#
# if value > 0:
#     print("Entered Value is positive")
# elif value < 0:
#     print("Entered Value is negative")
# else:
#     print("Entered Value is Zero")

# Designing a calculator

# Ask the user two floats (can be positive, negative, or zero)
# The user will choose operation (+, -, *, /)
# print out the result to the user.
# If the second number is zero print out (Can't divide by 0)

# a = float(input("Please Enter number a: "))
# b = float(input("Please Enter number b: "))
#
# operation = str(input("Please Choose your operation (+, -, *, /): "))
#
# if operation == "+":
#     print(a + b)
#
# elif operation == "-":
#     print(a - b)
#
# elif operation == "*":
#     print(a * b)
#
# elif operation == "/":
#     if int(b) == 0:
#         print("Bottom can't be zero!!!.")
#     else:
#         print(a / b)
#
# else:
#     print("Wrong operator was given!!!")

## One Line if Statements

#if "f" in "foo": print("1"); print("2"); print("3")

### Pass Statement

# if True:
#     pass
#
# print("yay")

# --- FOR LOOPS ----

# Syntax
# for <var> in <iterable>:
#     <statement>

# <var>       : x, i, _, a placeholder
# <iterable>  : list, dictionary
# <statement> : print(), operation, list.append()

# Example-1
# a = ["foo", "bar", "baz"]
#
# for i in a:
#     print(i)

# Example-2
# num = [1, 2, 3, 4, 5, 6, 7]
#
# for i in num:
#     print(i ** 3)

# String is iterable
#print(iter("foobar"))

# NOTE: int, float, built-in functions are not iterable. To
#       test iterability use th iter() function.

### Iterators

a = ['foo', 'bar', 'baz']

itr = iter(a)

# print(next(itr))
# print(next(itr))
# print(next(itr))

# Iterate Through a dictionary

d = {'foo': 1, 'bar':2 , 'baz': 3}

# for k in d:
#     print(d[k])

# Tuple
i, j= ((1, 2, 3), (3, 4, 5))

# for i, j in [(1, 2), (3, 4), (5, 6)]:
#     print(i, j)

# for n in (0, 1, 2, 3, 4, 5):
#     print(n)

# for x in range(21):
#     print(x)

# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         break
#     print(i)

# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         continue
#     print(i)

# it = 0
#
# while it < 10:
#     print(it)
#     it += 1 # this means it = it + 1

a = [1, 5, 3, 9, 34, 2, 4, 87, 8]
#
# max = 0
#
# for i in a:
#     if a.index(i) == 0:
#         max = i
#     else:
#         if i > max:
#             max = i
#
# print(max)
#
# print(sorted(a)[-1])

# a = [1, 2, 3, 4, 5, 6, 7, 45, 34, 2, 90]
#
# result = 1
#
# for val in a:
#     result = result * val
#
# print(result)

