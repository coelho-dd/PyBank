# checking account = conta corrent e savings account = conta poupança
import random
import sys
from account import Account

def main():
    print("Welcome to your personal bank!!")

    while True:
        u_input = input("Do you already have an account at our bank?[yes/no]: ")
        u_input = u_input.lower()

        if u_input == "yes":
            login(# account_obj)
        elif u_input == "no":
            while True:
                create = input("Do you wish to create an account?[yes/no]: ")
                create = create.lower()

                if create == "yes":
                    account = create_account()
                    login(account)
                elif create == "no":
                    print("Logging you out...")
                    sys.exit()
                else:
                    print("I'm sorry... I could not understand you. Please try again.")
        else:
            print("I'm sorry... I could not understand you. Please try again.")

def login(obj_account):
    pass

def create_account():
    owner = input("Your name: ")
    number = random.randint(100, 999)
    credit = input("The amount of money you wish to deposit on your account[type 0 for none]: ")
    type_of_account = input("What will be the type of your account[checking/savings]: ")

    account = Account(owner, number, credit, type_of_account)

    print("Your account was created successfully.")
    print("Logging you in...")

    return account

# Se eu estou executando o interpretador a partir desse arquivo, então execute a função main
if __name__ == "__main__":
    main()