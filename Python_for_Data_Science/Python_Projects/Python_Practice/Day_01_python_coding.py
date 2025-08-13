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
print("********** problem 1 completed **********")

# Problem 2: Count Vowels in a String: Create a function that counts the number of vowels (a, e, i, o, u) in a given string. Ignore case.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

# Example usage
print(count_vowels("Hello, World!"))  # Output: 3
print(count_vowels("Python"))         # Output: 1
print(count_vowels("AEIOUaeiou"))     # Output: 10
print(count_vowels("xyz"))            # Output: 0
print("********** problem 2 completed **********")