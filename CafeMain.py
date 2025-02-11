class MoneyMachine:
    CURRENCY = 'A$'
    COIN_VALUES = {
        "Andruarters": 0.25,
        "Andrimes": 0.1,
        "Andrickles": 0.05,
        "Andrennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f'Profit:{self.profit}{self.CURRENCY})CY}\nMoney recieved: {self.money_received}')

