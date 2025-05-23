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
        if order_name:
            pass
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item does not exist.")
        return None