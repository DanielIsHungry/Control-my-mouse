class MoneyMachiene:
    """Controls and manages the money"""
    CURRENCY = '$andre$'
    COINVALUES = {
        'penny': 0.01,
        'nickel': 0.05,
        'dime': 0.10,
        'quarter': 0.25
    }
    def __init__(self, user_funds):
        """Create varible instances"""
        self.funds = user_funds

        self.profit = 0
        self.money_recieved = 0

    def report(self):
        """Print the profit"""
        print(f'Current profit: {self.profit}{self.CURRENCY}')

    def ask_coins(self):
        try:
            quarters = float(input('How many quarters'))
            dimes = float(input('How many dimes'))
            nickels = float(input('How many nickels'))
            pennies = float(input('How many pennies'))

            return [quarters, dimes, nickels, pennies]
        except ValueError:
            print("error handling money. Try Again.")
            self.ask_coins()

    def process_coins(self, quarters, dimes, nickels, pennies):
        """Processes money using quarters, dimes and nickels."""
        quarters_given = quarters * self.COINVALUES['quarter']
        dimes_given = dimes * self.COINVALUES['dime']
        nickels_given = nickels * self.COINVALUES['nickel']
        pennies_given = pennies * self.COINVALUES['penny']
        total = quarters_given + dimes_given + nickels_given + pennies_given
        return total

    def make_payment(self, amount):
        """transfers funds to profit, unless unable to."""
        self.funds -= amount
        if self.funds < 0:
            self.funds -= amount
            print('Insufficient funds.')
            return False
        return True
