# checking account = conta corrent e savings account = conta poupança

from account import Account

my_account = Account("davi", 123, 1000, "checking")
my_account.withdraw(200)
my_account.bank_statement()
my_account.deposit(200)
my_account.bank_statement()