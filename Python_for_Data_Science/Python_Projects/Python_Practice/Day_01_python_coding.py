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

# Problem 6: Find the Second Largest Number
# Write a function that takes a list of integers and returns the second largest number without using built-in sorting functions.
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements to find the second largest
    first = second = float('-inf')  # Initialize to negative infinity
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None

# Example usage
print(second_largest([1, 2, 3, 4, 5]))  # Output: 4
print(second_largest([5, 5, 5, 5]))      # Output: None
print(second_largest([10, 20, 30, 40, 50]))  # Output: 40
print(second_largest([2, 1])) # Output: 1
print("********** problem 6 completed **********")
print("")

# Problem 7: Simple Bank Account (OOP)
# Create a BankAccount class with methods deposit(), withdraw(), and check_balance(). Ensure you handle cases like insufficient balance.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}, New Balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrew: {amount}, New Balance: {self.balance}"

    def check_balance(self):
        return f"Current Balance: {self.balance}"
    
# Example usage
account = BankAccount(100)  # Create an account with an initial balance of 100
print(account.check_balance())  # Output: Current Balance: 100
print(account.deposit(50))      # Output: Deposited: 50, New Balance: 150
print(account.withdraw(30))     # Output: Withdrew: 30, New Balance: 120
print(account.withdraw(200))    # Output: Insufficient balance.
print(account.check_balance())  # Output: Current Balance: 120
print("********** problem 7 completed **********")
print("")

# Problem 8: Frequency Counter
# Write a function that takes a list and returns a dictionary with the frequency of each element.
def frequency_counter(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

# Example usage
print(frequency_counter([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}
print(frequency_counter(["apple", "banana", "apple", "orange"]))  # Output: {'apple': 2, 'banana': 1, 'orange': 1}
print(frequency_counter("hello")) # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print("********** problem 8 completed **********")
print("")
        
