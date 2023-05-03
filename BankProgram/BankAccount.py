class BankAccount:
    current_value = None

    def __init__(self, account_number, account_holdername, account_balance):
        try:
            if len(str(account_number)) < 7:
                raise ValueError("Account number must be at least 7 characters long")
            if any(char.isdigit() for char in account_holdername):
                raise ValueError("Account holder name should not contain any digits.")
            if not str(account_balance).isdigit():
                raise ValueError("Error: Account balance should only contain numeric characters.")
            self.account_number = account_number
            self.account_holdername = account_holdername
            self.account_balance = account_balance
        except ValueError as valueError:
            print(f"Error: {valueError}")

    def deposit(self, amount):
        print("Deposit amount :")
        try:
            self.current_value = self.account_balance + amount
            print(f"the amount of your deposit is : {amount} ")
        except TypeError as typeError:
            print(f"Dont enter the string type value '{amount}'", typeError)
        else:
            print(f"Your funds have been successfully added to your current account: {self.current_value}\n")
            return self.current_value

    def withdraw(self, amount):
        print("Withdraw amount :")
        try:
            withdraw_balances = (self.current_value - amount)
            if withdraw_balances > self.account_balance:
                print(f"After your withdraw your current balance is {withdraw_balances} ")
            elif withdraw_balances < self.account_balance:
                print(f"Insufficient funds")
        except TypeError as typeError:
            print(f"Dont enter the string type value '{amount}'", typeError)
        else:
            print(f"Your Current Balance is : {withdraw_balances}\n")
            self.current_value = withdraw_balances
            return self.current_value

    def get_balance(self):
        print("Get my balance :")
        try:
            if self.current_value is not None:
                print(f"Your current balance is {self.current_value}")
            else:
                raise ValueError("Current value is not set.")
        except ValueError as valueError:
            print(f"Error: {valueError}")
