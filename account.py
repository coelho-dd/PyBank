class Account:
    def __init__(self, owner, number, credit, type_account):
        self.owner = owner
        self.number = number
        self.credit = credit
        self.type_account = type_account
        self.info = {}

    def withdraw(self, amount):
        """ Removes an x amount of money from the current amount """
        if amount > self.credit:
            print("You're trying to withdraw more money than what you currently have. Please try again.")
        else:
            self.credit = self.credit - amount
            self.info["withdraw"] = amount # save the operation that the method represents inside the info dict
            print("Withdraw executed successfully.")

    def deposit(self, amount):
        """ Adds up an x amount on the current amount """
        self.credit = self.credit + amount
        self.info["deposit"] = amount
        print("Deposit executed successfully.")

    def check_amount(self):
        """ Checks the amount of money on the account at the moment """
        print("You have $" + str(self.credit) + " in the bank.")

    def bank_statement(self):
        """ Prints all the information inside the info dictionary, if there's any inside of it """
        if self.info:
            for key, value in self.info.items():
                print(f"{key}: {value}")
        else:
            print("You did not execute any action on the account so far.")