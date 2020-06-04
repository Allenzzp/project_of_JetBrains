class CoffeeMac():
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550
    status = False

    def __init__(self):
        self.action = None
        if not self.status:
            self.move()

    def remaining(self):
        print(f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money
            """)

    def fill(self):
        CoffeeMac.water += int(input("Write how many ml of water do you want to add:\n"))
        CoffeeMac.milk += int(input("Write how many ml of milk do you want to add:\n"))
        CoffeeMac.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        CoffeeMac.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def buy(self):
        type_of_drk = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if type_of_drk == "back":
            pass
        else:
            if type_of_drk == "1":
                if self.water >= 250 and self.coffee_beans >= 16:
                    print("I have enough resources, making you a coffee!")
                    CoffeeMac.water -= 250
                    CoffeeMac.coffee_beans -= 16
                    CoffeeMac.money += 4
                    CoffeeMac.cups -= 1
                else:
                    if self.water < 250:
                        print("Sorry, not enough water!")
                    else:
                        print("Sorry, not enough coffee beans!")
            elif type_of_drk == "2":
                    if self.water < 350:
                        print("Sorry, not enough water!")
                    elif self.milk < 75:
                        print("Sorry, not enough milk!")
                    elif self.coffee_beans < 20:
                        print("Sorry, not enough coffee beans!")
                    else:
                        print("I have enough resources, making you a coffee!")
                        CoffeeMac.water -= 350
                        CoffeeMac.milk -= 75
                        CoffeeMac.coffee_beans -= 20
                        CoffeeMac.money += 7
                        CoffeeMac.cups -= 1
            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                else:
                    print("I have enough resources, making you a coffee!")
                    CoffeeMac.water -= 200
                    CoffeeMac.milk -= 100
                    CoffeeMac.coffee_beans -= 12
                    CoffeeMac.money += 6
                    CoffeeMac.cups -= 1

    def take(self):
        print(f"I gave you ${self.money}")
        CoffeeMac.money = 0

    def move(self):
        CoffeeMac.status = True
        while CoffeeMac.status:
            print("Write action (buy, fill, take, remaining, exit):")
            self.action = input()
            if self.action == "remaining":
                self.remaining()
            elif self.action == "fill":
                self.fill()
            elif self.action == "take":
                self.take()
            elif self.action == "buy":
                self.buy()
            else:
                CoffeeMac.status = False


CoffeeMac()

