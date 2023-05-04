from BankApplication.Bank import Bank


class RunnerClass:

    first_customer = Bank(123, "arun", 1000)
    print(first_customer.get_account_info())

    first_customer.deposit_amount(1000)
    print(first_customer.get_account_info())

    first_customer.withdraw(200)
    print(first_customer.get_account_info())

    second_customer = Bank(23, "arun", 1000)
    transaction_info = second_customer.transfer(first_customer, 300)
    print(transaction_info)
    print(first_customer.get_account_info())
