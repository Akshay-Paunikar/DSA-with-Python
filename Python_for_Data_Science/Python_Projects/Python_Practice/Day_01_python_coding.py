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
print("")

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
print("")

# Problem 3: Remove Duplicates from a List:
# Write a function that removes duplicates from a list without using set() while preserving the original order.
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
print(remove_duplicates([1, 2, 3, 2, 1, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates(["apple", "banana", "apple", "orange"]))  # Output: ["apple", "banana", "orange"]
print(remove_duplicates(["a", "b", "a", "c"])) # Output: ["a", "b", "c"]
print("********** problem 3 completed **********")
print("")

# Problem 4: Check for Palindrome: Given a string, check if it’s a palindrome (case-insensitive, ignore spaces).
def is_palindrome(text):
    cleaned_text = ''.join(text.split()).lower()  # Remove spaces and convert to lowercase
    return cleaned_text == cleaned_text[::-1]  # Check if the string is equal to its reverse

# Example usage
print(is_palindrome("Madam"))  # Output: True
print(is_palindrome("Apple"))  # Output: False
print(is_palindrome("Racecar"))                # Output: True
print(is_palindrome("A man a plan a canal Panama")) # Output: True
print(is_palindrome("Hello"))                  # Output: False
print("********** problem 4 completed **********")
print("")

# Problem 5: Merge Two Dictionaries and if a key exists in both, sum values.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum values if key exists in both
        else:
            merged_dict[key] = value  # Add new key-value pair
    return merged_dict

# Example usage
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # Output: {'a': 1, 'b': 5, 'c': 4}
print(merge_dictionaries({'x': 10, 'y': 20}, {'y': 30, 'z': 40}))  # Output: {'x': 10, 'y': 50, 'z': 40}
print(merge_dictionaries({'name': 'Alice', 'age': 25}, {'age': 5, 'city': 'Wonderland'}))  # Output: {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
print("********** problem 5 completed **********")
print("")