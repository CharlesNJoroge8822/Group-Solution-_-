# Question 5
# Create a Command-Line Interface (CLI) project in Python that mimics Safaricom's SIM Toolkit. When you run the program, it should display menus dynamically based on user input. The program should handle user choices and navigate through different options just like the Safaricom SIM Toolkit.

# Requirements:
# Main Menu: When the program starts, display the following options:
# SIM 1
# 1. Safaricom
# 2. M-PESA
# Enter your choice: ________

# Submenu for M-PESA: If the user selects option 1 (M-PESA), show the following menu:
# SIM 1
# 1. Send Money
# 2. Withdraw Cash
# 3. Buy Airtime
# 4. Loans and Savings
# 5. Lipa na M-PESA
# 6. My Account
# Enter your choice: ________

# Submenu for "Send Money": If the user selects option 1 (Send Money), display:
# Enter Phone Number: 
# (Digits 0-9, *, #, +) 
# 10-13 characters: 
# ________________
# After each action, the program should handle input validation and navigate back to the appropriate menu or exit the program if the user wishes.
# Example Interaction:
# - User runs the program this displays in the terminal :
# SIM 1
# 1. Safaricom
# 2. M-PESA
# Enter your choice: 2

# - Next screen appears:
# SIM 1
# 1. Send Money
# 2. Withdraw Cash
# 3. Buy Airtime
# 4. Loans and Savings
# 5. Lipa na M-PESA
# 6. My Account
# Enter your choice: 1

# - Next screen appears:
# Enter Phone Number:
# (Digits 0-9, *, #, +)
# 10-13 characters: ________


# MPESA KIT
# Implemented only the send money ...

def menu():
    # Display the main menu options
    print('''
SIM TOOL-KIT:
    1. M-PESA
    2. Safaricom
    ''')
    
    # Ask the user to choose an option and store their input as text
    user_input = input('Enter choice: ')
    
    # Check if the input is a number
    if user_input.isdigit():
        # Convert the input to an integer to use for decision making
        choice = int(user_input)
        
        # If the choice is 1, go to the M-PESA menu
        if choice == 1:
            mpesa()
        else:
            # If the choice is anything other than 1, print an error message and show the menu again
            print("Invalid choice. Try again.")
            menu()
    else:
        # If the input isn't a number, tell the user and ask again
        print("Invalid input. Enter a number.")
        menu()


def mpesa():
    # Display the M-PESA options menu
    print('''
M-PESA Options:
    1. Send Money
    2. Withdraw Cash
    3. Buy Airtime
    4. Lipa na M-PESA
    ''')
    
    # Ask the user to choose an option from M-PESA and store their input as text
    user_input = input("Enter option: ")
    
    # Check if the input is a number (contains only digits)
    if user_input.isdigit():
        # Convert the input to an integer (a number) to use for decision making
        option = int(user_input)
        
        # If the option is 1, go to the Send Money function
        if option == 1:
            send()
        # If the option is 2, 3, or 4, print that the feature is coming soon, then show the M-PESA menu again
        elif option is [2, 3, 4]:
            print(f"Option {option} coming soon.")
            mpesa()
        else:
            # If the option isn't valid, show an error message and ask again
            print("Invalid option. Try again.")
            mpesa()
    else:
        # If the input isn't a number, tell the user and ask again
        print("Invalid input. Enter a number.")
        mpesa()


def send():
    # This function is for sending money using M-PESA
    
    print("Send Money")
    
    # Ask the user to enter the phone number, amount, and M-PESA PIN
    phone = input("Phone Number: ")
    amount = input("Amount: ")
    pin = input("M-PESA PIN: ")

    # Simulate sending money by printing the details of the transaction
    print(f"{amount} has been successfully sent to {phone} on this date on transaction cost of 27 ksh. New m-pesa balance is ksh 1, 450. Your trusted business partner. Visit ...")

    # After sending money, return to the M-PESA menu
    mpesa()


# Start the program by showing the main menu
menu()
