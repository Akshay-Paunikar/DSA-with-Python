MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# below function is useful for collecting user input that gets the deposit from the user.
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

# below function will ask players how much amount to bet and on how much on each lines they want to bet on.
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1 - "+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines



# let's check if our function works as it is intended or not
# deposit()

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
main()