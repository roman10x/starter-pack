class CoffeeMachine:
    def __init__(self):
        self.money = 550
        self.water_vol = 400
        self.milk_vol = 540
        self.beans = 120
        self.disposable_cups = 9

    def print_supplies(self):
        print(f"\nThe coffee machine has:\n"
              f"{self.water_vol} of water\n"
              f"{self.milk_vol} of milk\n"
              f"{self.beans} of coffee beans\n"
              f"{self.disposable_cups} of disposable cups\n"
              f"{self.money} of money")

    def buy(self):
        water_per_cup = 0
        milk_per_cup = 0
        beans_per_cup = 0
        cost = 0
        limit = 0
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        type_of_coffee = input("> ")
        if type_of_coffee == '1':
            water_per_cup = 250
            milk_per_cup = 0
            beans_per_cup = 16
            cost = 4
        elif type_of_coffee == '2':
            water_per_cup = 350
            milk_per_cup = 75
            beans_per_cup = 20
            cost = 7
        elif type_of_coffee == '3':
            water_per_cup = 200
            milk_per_cup = 100
            beans_per_cup = 12
            cost = 6
        elif type_of_coffee == 'back':
            pass
        if (self.water_vol - water_per_cup) >= 0 \
                and (self.milk_vol - milk_per_cup) >= 0 \
                and (self.beans - beans_per_cup) >= 0 \
                and type_of_coffee != 'back':
            print("I have enough resources, making you a coffee!")
            self.money += cost
            self.disposable_cups -= 1
        else:
            self.money = self.money
            self.disposable_cups = self.disposable_cups
        if (self.water_vol - water_per_cup) < 0 \
                or (self.milk_vol - milk_per_cup) < 0 \
                or (self.beans - beans_per_cup) < 0:
            if (self.water_vol - water_per_cup) < 0:
                limit = "water"
            elif (self.milk_vol - milk_per_cup) < 0:
                limit = "milk"
            elif (self.beans - beans_per_cup) < 0:
                limit = "beans"
            print(f"Sorry, not enough {limit}!")

        else:
            self.water_vol -= water_per_cup
            self.milk_vol -= milk_per_cup
            self.beans -= beans_per_cup

    def fill(self):
        print("\nWrite how many ml of water do you want to add:")
        water_vol_fill = int(input().replace('> ', ''))
        self.water_vol += water_vol_fill
        print("Write how many ml of milk do you want to add:")
        milk_vol_fill = int(input().replace('> ', ''))
        self.milk_vol += milk_vol_fill
        print("Write how many grams of coffee beans do you want to add:")
        beans_vol_fill = int(input().replace('> ', ''))
        self.beans += beans_vol_fill
        print("Write how many disposable cups of coffee do you want to add:")
        cups_fill = int(input().replace('> ', ''))
        self.disposable_cups += cups_fill

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


machine = CoffeeMachine()

while True:
    print("\nWrite action (buy, fill, take, remaining, exit):")
    action = input("> ")
    if action == 'buy':
        machine.buy()
    elif action == 'fill':
        machine.fill()
    elif action == 'take':
        machine.take()
    elif action == 'remaining':
        machine.print_supplies()
    elif action == 'exit':
        break
