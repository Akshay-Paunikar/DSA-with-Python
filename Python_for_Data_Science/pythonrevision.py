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
print("Hello, World!")

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
print(keyword.kwlist)

age = 25  # valid variable name
_age = 30  # valid variable name with underscore
age1 = 35  # valid variable name with a number

print(age, _age, age1)

# Invalid variable names
# 1age = 40  # invalid variable name, cannot start with a number
# print(1age)  # this will raise an error

name = "akshay"
last_name = "kumar"

print(name, last_name)
print(f"My name is {name} {last_name}.")  # formatted string literal (f-string)
print("My name is {} {}.".format(name, last_name))  # using format method
print("My name is {name} {surname}.".format(name = name, surname = last_name))  # using format method


