# Day - 1 of solving python coding problems

# Problem 1: Reverse a string without using built-in functions or slicing
def reverse_string(text):
    reversed_str = ""
    for i in text:
        reversed_str = i + reversed_str
    return reversed_str

# Example usage
print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
print(reverse_string("Python"))       # Output: "nohtyP"
print(reverse_string("Level"))        # Output: "leveL"
print(reverse_string("akshay"))        # Output: "yahska"