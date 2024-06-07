# checking account = conta corrente e savings account = conta poupança
import random
import sys
from account import Account

def main():
    print("Welcome to your personal bank!!")

    while True:
        u_input = input("Would you like to login to your account?[yes/no]: ")
        u_input = u_input.lower()

        if u_input == "yes":
            account = login()
            pybank(account)
        elif u_input == "no":
            break
        else:
            print("I'm sorry... I could not understand you. Please try again.")

def login():
    """ Creates an instance of the Account class that represents the account of an user """
    owner = input("Your name: ")
    number = random.randint(100, 999)
    credit = input("The amount of money you wish to deposit on your account[type 0 for none]: ")
    type_of_account = input("What will be the type of your account[checking/savings]: ")

    account = Account(owner, number, credit, type_of_account)

    print("Your account was created successfully.")
    print("Logging you in...")

    return account

def pybank(obj):
    """ Contains the logic of the program that resembles an atm machine """
    print("This is the screen where you can perform actions on your account, such as:")
    print("Deposit and withdraw money, visualize your bank statement and so on...")
    print("\nSelect one of the options below to execute it:")
    print("1[withdraw], 2[deposit], 3[check your amount], 4[check bank statement] and 5[to quit the app]")

    while True:
        u_input = input(">>> ")
        u_input = u_input.lower()

        if u_input == "1":
            w_value = input("What would be the amount that you'd like to withdraw: ")
            w_value = int(w_value)
            obj.withdraw(w_value)
        elif u_input == "2":
            d_value = input("What would be the amount that you'd like to deposit: ")
            obj.deposit(d_value)
        elif u_input == "3":
            obj.check_amount()
        elif u_input == "4":
            obj.bank_statement()
        elif u_input == "5":
            print("Logging you out...")
            sys.exit()
        else:
            print("I'm sorry... I could not understand you. Please try again.")

# Se eu estou executando o interpretador a partir desse arquivo, então execute a função main
if __name__ == "__main__":
    main()