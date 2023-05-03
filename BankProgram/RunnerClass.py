from BankProgram.BankAccount import BankAccount


class RunnerClass(BankAccount):

    bank = BankAccount(1634442, "Arun", 7000)
    bank.deposit(3000)
    bank.withdraw(10)
    bank.get_balance()
