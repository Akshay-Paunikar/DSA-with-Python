# Understanding and Practicing OOPS concepts
# OOPS - Object Oriented Programming System

# Class - Blueprint for creating an object
# Object -  Instance of a class

# class Student:
#     name = "Akshay"
    
# s1 = Student()
# print(s1.name)

# __init__ - All classes have this function called __init__() which is always executed when the object is being initiated.
# self -  The self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class.

# class Student:
#     name = "Akshay"
#     def __init__(self):
#         print("Adding new student to the database...")
        
# s2 = Student()

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Adding new student to the database ...")
        
# s3 = Student(name="John")
# print(s3.name)

# s4 = Student(name="Arjun")
# print(s4.name)

# Class attributes are common to all the objects and the object/instance attributes are specific to the objects being created.
# Methods - Methods are function that belong to objects.

# class Student:
#     college = "ABC college" # class attribute
    
#     def __init__(self, name, marks):
#         self.name = name # instance attribute
#         self.marks = marks
#         print("Adding new student to the database ...")
    
#     def welcome(self):
#         print("Welcome students...!!!", self.name)
        
#     def get_marks(self):
#         return self.marks
        
# s3 = Student("John", 98)
# print(s3.name)
# print(s3.get_marks())

# s4 = Student("Arjun", 85)
# print(s4.name)
# print(s4.get_marks())
# print(s4.college)
# s4.welcome()

# practice
# create a student class that takes name & marks of 3 subjects as arguments in the constructor.
# then create a method to print the average

class Student:
    def __init__(self, name, physics, chemistry, maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        
    def average_marks(self):
        print("Hi", self.name, "Your average score is:", (self.physics + self.chemistry + self.maths) // 3)

student1 = Student("Akshay", 88, 77, 66)
print(student1.name)
student1.average_marks()

# Static Methods : Methods that don't use the self parameter (work at class level).
# Decorator: Decorator allows us to wrap another function in order to extend the behaviour of the wrapped function without
# permanently modifying it.

class Student:
    def __init__(self, name, physics, chemistry, maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        
    @staticmethod #decorator
    def hello():
        print("Hello")
        
    def average_marks(self):
        print("Hi", self.name, "Your average score is:", (self.physics + self.chemistry + self.maths) // 3)

student1 = Student("Akshay", 88, 77, 66)
print(student1.name)
student1.average_marks()
student1.hello()


# Abstraction, Encapsulation, Inheritance, 