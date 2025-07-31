# what is python?
# python is a general purpose, high level, interpreted, dynamically typed programming language which allows programmming
# in object oriented and procedural paradigms.

# python language is very popular among beginners and professionals because of its simplicity and readability.
# it is widely used in web development, data science, machine learning, artificial intelligence, automation, and more.
# python has a huge collection of standard libraries and frameworks that make it easy to build complex applications quickly.
# python is an open source language, which means it is free to use and distribute.
# python is a case sensitive language, which means that variable names and keywords must be written in the correct case.
# Python programs are generally smaller than other programming languages and the indentation requirement of the language, 
# makes them readable all the time.

# Now, let's breakdown the definition of python:
# 1. General purpose: Python can be used for a wide range of applications, from web development to data analysis.
# 2. High level: Python is designed to be easy to read and write, with a syntax that is similar to natural language.
# 3. Interpreted: Python code is executed line by line, which makes it easier to debug and test.
# 4. Dynamically typed: Python does not require you to declare the data type of a variable before using it, which makes it more flexible.
# 5. Object oriented: Python supports object-oriented programming, which allows you to create reusable code and organize your 
# programs into classes and objects.
# 6. Procedural paradigms: Python also supports procedural programming, which allows you to write code in a linear fashion, 
# using functions and procedures.

# let's write our first python program
# print("Hello, World!")

# Rules for identifiers (such as variable names, function names, or class names)

# In Python, variable names must follow certain rules to be valid. Here are the key rules for naming variables:
# 1. Identifier names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. Identifier names can contain letters, numbers, and underscores.
# 3. Identifier names are case-sensitive, meaning that "myVariable" and "myvariable" are considered different variables.
# 4. Identifier names cannot be a reserved keyword in Python (e.g., "if", "else", "while", "for", etc.).
# 5. Identifier names should be descriptive and meaningful, making it easier to understand the purpose of the variable.
# 6. Identifier names should not contain spaces or special characters (except for underscores).
# 7. Identifier names should not start with a number.

import keyword
# print(keyword.kwlist)

age = 25  # valid variable name
_age = 30  # valid variable name with underscore
age1 = 35  # valid variable name with a number

# print(age, _age, age1)

# Invalid variable names
# 1age = 40  # invalid variable name, cannot start with a number
# print(1age)  # this will raise an error

# name = "akshay"
# last_name = "kumar"

# print(name, last_name)
# print(f"My name is {name} {last_name}.")  # formatted string literal (f-string)
# print("My name is {} {}.".format(last_name, name))  # using format method
# print("My name is {name} {surname}.".format(name = name, surname = last_name))  # using format method

# print "Hello, World!" 5 times using a while loop
# count = 1
# while count <= 5:
#     print("Hello, World!")
#     count += 1  # increment the count by 1
    
# print numbers from 1 to 10 using a while loop
# count = 1
# while count <= 10:
#     print(count)
#     count += 1  # increment the count by 1

# print numbers from 1 to 10 using a while loop
# count = 10
# while count >= 1:
#     print(count)
#     count -= 1  # decrement the count by 1
    
# multipication table for a number using a while loop
# num = int(input("Enter a number: "))
# count = 1
# while count <= 10:
#     print(f"{num} x {count} = {num * count}")
#     count += 1  # increment the count by 1

# search for a number x in this tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int(input("Enter a number to search in the tuple: "))
# idx = 0

# while idx < len(tup):
#     if tup[idx] == x:
#         print(f"{x} found at index {idx}.")
#         break
#     idx += 1  # increment the index by 1

# write a function to calculate the factorial of a number using a while & for loop
# def factorial_while(n):
#     if n < 0:
#         print("Factorial is not defined for negative numbers.")
#     result = 1
#     count = 1
#     while count <= n:
#         result *= count
#         count += 1
#     print(result)
    
# num1 = int(input("Enter a number to calculate factorial using while loop: "))
# factorial_while(num1)  

# def factorial_for(n):
#     if n < 0:
#         print("Factorial is not defined for negative numbers.")
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     print(result)
    
# num2 = int(input("Enter a number to calculate factorial using for loop: "))    
# factorial_for(num2)  

# python function is a block of reusable code that performs a specific task.
# it can take input parameters and return a value.
# functions are defined using the def keyword followed by the function name and parentheses.
# def function_name(parameters):
#     # function body
#     return value

def even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(even_or_odd, lst)))  # using filter function to filter even numbers from the list

print(list(filter(lambda x: x % 2 == 0, lst)))  # using lambda function to filter even numbers from the list

