menu = {
    'coffee': {
        'price': 4.5,
        'milk': 50,
        'foam': 10,
        'coffee powder': 100,
        'water': 150
    },
    'latte': {
        'price': 3.99,
        'milk': 20,
        'foam': 100,
        'coffee powder': 100,
        'water': 50
    },
    'cappuccino': {
        'price': 2.99,
        'milk': 50,
        'foam': 50,
        'coffee powder': 50,
        'water': 25
    },
    'mystery juice': {
        'price': 999.99,
        'milk': 1000,
        'foam': 1000000000,
        'coffee powder': 10000000000,
        'water': 100000000
    },
    'water': {
        'price': 0.10,
        'milk': 0,
        'foam': 0,
        'coffee powder': 0,
        'water': 100
    },
    'americano': {
        'price': 4.99,
        'milk': 100,
        'foam': 10,
        'coffee powder': 75,
        'water': 50
    }
}
liquids = {
    'milk': 1000,
    'water': 1000,
    'coffee powder': 1000,
    'foam': 1000
}

inventory = list()
funds = 100
given = 0
profit = 0
menuSeen = False
askAgain = False
shutdown = False
hasPay = False
wantOrder = True


def pay():
    global given, funds, profit, inventory, hasPay, shutdown
    try:
        given = 0
        ans = int(input('How many quarters? ($0.25)'))
        given += ans * 0.25
        ans = int(input('How many dimes? ($0.10)'))
        given += ans * 0.1
        ans = int(input('How many nickels ($0.05)'))
        given += ans * 0.05
        ans = int(input('How many pennies? ($0.01)'))
        given += ans * 0.01

        p = 0
        for v in inventory:
            p += menu[v]['price']

        change = given - p

        if change < 0:
            print("That is not enough!")
            profit -= given + change
            funds += given + change
            given = 0
        else:
            funds -= given + change
            if funds < 0:
                print('You dont have enough funds.')
                profit -= given + change
                funds += given + change
            else:
                hasPay = True
                shutdown = True
                funds -= given + change
                profit += given + change
                print(f'You have paid ${given} and have been refunded ${change} change')
                print('Thank you for coming! Please come again.')

    except ValueError:
        print('That is not an option!')


def display_menu():
    global menuSeen
    menuSeen = True
    print('menu:\n')
    for _k, _v in menu.items():
        print(f'{_k}')
        for k, v in _v.items():
            print(f'{k} : {v}ml' if k != 'price' else f'{k} : ${v}', end=',\n')
        print('', end='\n')


def prompt(userinput):
    return input(f'{userinput}\n').lower()


def ui():
    global funds, menuSeen, askAgain, profit, shutdown, wantOrder
    if shutdown:
        pass
    else:
        ans = ""
        if not menuSeen:
            ans = prompt('Would you like to see the menu?')
        if ans.lower() == "yes" and not menuSeen:
            display_menu()
            ui()
        elif ans.lower() == 'no' or menuSeen:
            if wantOrder:
                ans = prompt(
                    'What would you like to order?'
                    if not askAgain else
                    'Would you like to order anything else?'
                )
            else:
                payment_now = input('Would you like to pay now?').lower()
                if payment_now == 'yes':
                    pay()
                else:
                    wantOrder = True

            for key, item in menu.items():
                if ans == key.lower():
                    price = menu[ans.lower()]["price"]
                    print(f'That will be ${price}\nThank you for your order!')

                    liquids['milk'] -= menu[ans]['milk']
                    liquids['water'] -= menu[ans]['water']
                    liquids['coffee powder'] -= menu[ans]['coffee powder']
                    liquids['foam'] -= menu[ans]['foam']

                    inventory.append(ans)

                    payment_now = input('Would you like to pay now?').lower()
                    if payment_now == 'yes':
                        pay()
                    else:
                        wantOrder = True

                    for __k, __i in liquids.items():
                        if int(__i) < 0:
                            print('We dont have enough ingredients to fulfill your order.')
                            break

                    askAgain = True
                    menuSeen = True
                    ui()
            else:
                if ans == 'report':
                    print('Our current resources:\n')
                    for k, v in liquids.items():
                        print(f'{k}: {v}ml')
                elif ans == 'inventory':
                    print(f'What you ordered:')
                    print(*inventory, sep=', ')
                elif ans == 'profit':
                    print(f'We have made ${profit} today.')
                elif ans == 'shutdown':
                    if hasPay:
                        print('Cafe has been shutdown. Goodbye!')
                        shutdown = True
                        pass
                    else:
                        print('Hey! You cant leave without paying! Please pay.')
                        ui()
                        pass
                elif ans == 'no':
                    print('Alright.')
                    wantOrder = False
                else:
                    print('That item doesnt seem to be on the menu.' if not shutdown else "")
                if shutdown:
                    pass
                else:
                    ui()


print('Hello and welcome to daniels ultimate cafe!!1!1!')
ui()
