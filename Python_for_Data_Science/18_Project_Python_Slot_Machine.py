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

# below functions will ask players how much amount to bet and on how much on each lines they want to bet on.
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

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount
    

# let's check if our function works as it is intended or not
# deposit()

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is ${balance}.")
        else:
            break            
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    
main()