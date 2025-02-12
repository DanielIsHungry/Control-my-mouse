from cafeclass import *

MENU = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachiene(user_funds=10)

choice = None

is_on = True

while is_on:
    choice = input(f"What would you like? ({MENU.get_items()}): ").strip().lower()

    if choice == 'off':
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
        break


    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()

    else:
        drink = MENU.find_drink(choice)
        if drink:
            if coffee_machine.is_resource_sufficient(choice):
                print(f"The {choice} costs {drink.cost:.2f}{money_machine.CURRENCY}. Please insert coins.")

                total_money = money_machine.process_coins(*money_machine.ask_coins())

                if total_money >= drink.cost:
                    change = round(total_money - drink.cost, 2)
                    if change > 0:
                        print(f"Here is your change: ${change:.2f}")

                    money_machine.profit += drink.cost
                    for ingredient, amount in drink.ingredient.items():
                        coffee_machine.resources[ingredient] -= amount

                    print(f"Here's your {choice} ☕. Enjoy!")
                else:
                    print("Not enough money inserted. Refunding coins.")
