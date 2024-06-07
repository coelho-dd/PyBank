# checking account = conta corrente e savings account = conta poupança
import random
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
    owner = input("Your name: ")
    number = random.randint(100, 999)
    credit = input("The amount of money you wish to deposit on your account[type 0 for none]: ")
    type_of_account = input("What will be the type of your account[checking/savings]: ")

    account = Account(owner, number, credit, type_of_account)

    print("Your account was created successfully.")
    print("Logging you in...")

    return account

def pybank(obj):
    pass

# Se eu estou executando o interpretador a partir desse arquivo, então execute a função main
if __name__ == "__main__":
    main()