class MenuItem:
    """Models each Menu item"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = float(cost)
        self.ingredient = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }

class Menu:
    """Models the menu with the drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]


    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name, returns it if it exists otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item does not exist.")

class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
        }

        self.is_resource_sufficient('coffee')

    def report(self):
        """Prints a report of all resources"""
        # print(f'Water: {self.resources["water"]} ml')
        # print(f'Milk: {self.resources["milk"]} ml')
        # print(f'Coffee: {self.resources["coffee"]}g')

        for key, item in self.resources.items():
            print(f'{key}: {item}ml' if key != "coffee" else f'{key}: {item}g')

    def is_resource_sufficient(self, drink):
        """Checks if you have enough resources for a drink to be made"""
        m = Menu()
        drink_item = m.find_drink(drink)
        if drink_item:
            for ingredient, amount in drink_item.ingredient.items():
                if self.resources[ingredient] < amount:
                    print(f"Sorry, there is not enough {ingredient}.")
                    return False
            return True

class Money_machiene:
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