# create class
class BankAccount:
    """
    Represents a bank account with an account number, account holder, and balance.
        Allows deposits, withdrawals, and retrieving account details.
    """

# define init method with the proper parameters
    def __init__(self, account_number, account_name, balance):
        """
        Initializes a new BankAccount object.

        :param account_number: str - Unique identifier for the account
        :param account_holder: str - Name of the account holder
        :param initial_balance: float - Starting balance (default is 0.0)
        """
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = balance
# create the getter methods (account_number, account_name, and balance)
    def get_account_number(self) -> str:
        """Returns account number in a string"""
        return self.__account_number

    def get_account_name(self) -> str:
        """Returns account name in a string"""
        return self.__account_name

    def get_balance(self) -> float:
        """Returns balance in a float"""
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'You deposited {amount}')
        else:
            print("Deposit a positive number you weirdo")

    def withdraw(self, amount):
        # if 0 < amount <= self.balance
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f'Withdrawed {amount}')
            return
        print('Some kindof error occured. womp womp')

    def dele(self):
        del self.__balance
        del self.__account_number
        del self.__account_name
        del self

    def __str__(self):
        """Returns a formatted string representation of the account details."""
        return f"Account {self.__account_number} - {self.__account_name}: ${self.__balance}"

# write withdraw method that checks that amount is greater than 0,
# less than or equal to the amount currently in the account, withdraws if it is, and prints result

if __name__ == "__main__":
    print("\n# TEST 1: Creating a New Account")
    account = BankAccount("123456", "Alice Johnson", 500.0)
    print(str(account))  # Expected: "Account 123456 - Alice Johnson: $500.00"

    