import re

from banke_account_app.banke_account import BankeAccount
from banke_account_app.banke_atm_machine import BankeAtmMachine

def main():

    while True:
        print_menu()
        new_account = BankeAtmMachine()
        user_choice = input("Choose your preferred choice (1 to 7) and (0 to quit): ")
        while user_choice not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
            user_choice = input("Choose your preferred choice (1 to 7) and (0 to quit): ")

        if user_choice == "1":
                create_an_account(new_account)

        if user_choice == "2":
                deposit_money(new_account)

        if user_choice == "3":
            withdraw_money(new_account)

        if user_choice == "0":
            print("Thank you for using Banke ATM Machine!")
            break





def print_menu():
    print("""
 Welcome to Banke Bank!
    1. Create an account
    2. Deposit money
    3. Withdraw money
    4. Check Account Balance
    5. Transfer money
    6. Close an account
    7. Change Pin
    0. Exit
""")

def create_an_account(new_account):
    first_name = input("Enter your first name: ")
    while first_name is None or not re.match("^[a-zA-Z\\-]+$", first_name):
        first_name = input("Invalid input, Enter your first name: ")
        continue

    last_name = input("Enter your last name: ")
    while first_name is None or not re.match("^[a-zA-Z\\-]+$", last_name):
        last_name = input("Invalid input, Enter your last name: ")
        continue

    pin = input("Enter your pin: ")
    while pin is None or not pin.isdigit() or len(pin) != 4:
        pin = input("Invalid input, Enter your pin: ")
        continue

    new_account.create_account(first_name, last_name, pin)
    print("Account created successfully. " + first_name.upper() +" " + last_name.upper())



def deposit_money(new_account):
    pin = input("Enter your pin: ")
    while pin is None or not pin.isdigit() or len(pin) != 4:
        pin = input("Invalid input, Enter your pin: ")
        continue

    account = new_account.find_account_by_the_pin(pin)
    if account is None:
        print("Account not found.")
        return

    deposit = input("Enter deposit amount: ")
    while not deposit.isdigit() or float(deposit) <= 0.0:
        deposit = input("Invalid input, Enter deposit amount: ")

    deposit_amount = float(deposit)
    account.deposit(pin, deposit_amount)
    print(f"Deposit successful! Your new balance is: {account.get_balance()}")


def withdraw_money(new_account):
    pin = input("Enter your pin: ")
    while pin is None or not pin.isdigit() or len(pin) != 4:
        pin = input("Invalid input, Enter your pin: ")
        continue

    account = new_account.find_account_by_the_pin(pin)
    if account is None:
        print("Account not found.")
        return

    withdrawal_amount = input("Enter withdrawal amount: ")
    while not withdrawal_amount.isdigit() or float(withdrawal_amount) <= 0.0:
        withdrawal_amount = input("Please enter a valid withdrawal amount.")
        continue

    account.withdraw(pin, withdrawal_amount)
    print(f"Withdraw successful! Your new balance is: {account.get_balance()}")



if __name__ == '__main__':
    main()