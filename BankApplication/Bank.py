class Bank:

    def __init__(self, account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

    def deposit_amount(self, amount):
        print()
        try:
            self.account_balance += amount
            print(f"the amount of your deposit is : {amount} ")
        except TypeError as typeError:
            print(f"Dont enter the string type value '{amount}'", typeError)
        else:
            print(f"Your funds have been successfully added to your current account: {self.account_balance}")
            return self.account_balance

    def withdraw(self, amount):
        print()
        try:
            withdraw_balances = (self.account_balance - amount)
            if withdraw_balances < self.account_balance:
                print(f"After your withdraw your current balance is {withdraw_balances} ")
        except TypeError as typeError:
            print(f"Dont enter the string type value '{amount}'", typeError)
        else:
            self.account_balance = withdraw_balances
            return self.account_balance

    def transfer(self, to_account, amount):
        if self.account_balance < amount:
            raise ValueError("Insufficient balance")
        self.account_balance -= amount
        to_account.deposit_amount(amount)
        return f"Transferred {amount} to account number {to_account.account_number}"

    def get_account_info(self):
        return {
            "account_number": self.account_number,
            "account_holder_name": self.account_holder_name,
            "account_balance": self.account_balance
        }

