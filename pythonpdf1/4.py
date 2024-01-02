class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print("Account {} created with initial balance ${}".format(account_number, initial_balance))
        else:
            print("Account {} already exists. Cannot create duplicate accounts.".format(account_number))

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print("Balance in account {}: ${}".format(account_number, self.accounts[account_number]))
        else:
            print("Account {} not found. Please check the account number.".format(account_number))

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print("${} deposited into account {}. New balance: ${}".format(amount, account_number, self.accounts[account_number]))
        else:
            print("Account {} not found. Please check the account number.".format(account_number))

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("${} withdrawn from account {}. New balance: ${}".format(amount, account_number, self.accounts[account_number]))
            else:
                print("Insufficient funds in account {}. Cannot withdraw ${}.".format(account_number, amount))
        else:
            print("Account {} not found. Please check the account number.".format(account_number))


bank = Bank()

bank.create_account("123456", 1000)
bank.create_account("789012", 500)

bank.check_balance("123456")

bank.deposit("123456", 200)
bank.withdraw("789012", 100)

bank.check_balance("789012")