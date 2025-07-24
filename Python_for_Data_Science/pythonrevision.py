# general purpose - wide variety of applications, across multiple domains and tasks rather than being specialized for a specific area
# for example, Python is used in web development, data analysis, artificial intelligence, scientific computing, and more.
# unlike domain-specific languages like SQL which is specialized for database queries and html which is specialized for 
# web page structure

# interpreted - Python code is executed line by line, which makes it easier to debug and test
# Python is an interpreted language, meaning that it is executed by an interpreter rather than being compiled into machine code.
# This allows for more flexibility and ease of use, as developers can run code without needing to compile it first.
# This also means that Python code can be run on any platform with a compatible interpreter, making it highly portable.
# This is in contrast to compiled languages like C or C++ which require a compilation step before execution.
# interpreted languages are generally slower than compiled languages, but they offer more flexibility and ease of use

# high level - Python abstracts away many of the complex details of the computer's hardware, making it easier for developers 
# to write code without needing to manage memory or other low-level details.
# Python is a high-level language, meaning it is designed to be easy to read and write, with a syntax that is closer to human language.

# dynamically typed - Python does not require explicit declaration of variable types, allowing for more flexibility in coding.
# Python is dynamically typed, meaning that variable types are determined at runtime rather than in advance.


# object oriented - Python supports object-oriented programming, allowing developers to create classes and objects to encapsulate data 
# and behavior.
# Python is an object-oriented language, meaning it supports the concept of objects, which can encapsulate data and behavior.
# This allows for more modular and reusable code, as well as better organization of complex programs.
# Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
# procedural paradigm - Python supports procedural programming, which is a programming paradigm that focuses on the concept of 
# procedures or routines.
# functional programming - Python also supports functional programming, which is a programming paradigm that treats computation as 
# the evaluation of mathematical functions and avoids changing state and mutable data.
# Example of a simple Python program demonstrating some of these concepts
# This program checks if a user is a minor or an adult based on their age input.
# It uses basic input/output, conditional statements, and demonstrates Python's high-level syntax.


print("Hello World!")

age = int(input("Enter your age: "))
age1 = input("Enter your age again: ")
age2 = True
print(type(age))
print(type(age1))
print(type(age2))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")