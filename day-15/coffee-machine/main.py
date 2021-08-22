# import from data.py
from data import MENU, resources


# create function if the answer is 'off'
def off():
    if answer == "off":
        exit()


# print prices
def print_flavours():
    while answer == "flavours":
        print("Espresso - $1.5")
        print("Latte - $2.5")
        print("Cappuccino - $3.0")
        welcome()


# create function if the answer is 'report'
def print_report():
    while answer == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        welcome()


# create a function based on coffee flavours, deduct ingredients, and money
def check():
    if answer == 'espresso':
        if MENU['espresso']['ingredients']['water'] <= resources['water']:
            if MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
                #ask for money
                print("Please, insert coins.")

                quarters = float(input("How many quarters? "))
                dimes = float(input("How many dimes? "))
                nickles = float(input("How many nickles? "))
                pennies = float(input("How many pennies? "))

                current_money = (0.25 * quarters) + (0.10 * dimes) + (
                    0.05 * nickles) + (0.01 * pennies)

                if current_money >= MENU['espresso']['cost']:
                    resources['water'] -= MENU['espresso']['ingredients'][
                        'water']
                    resources['coffee'] -= MENU['espresso']['ingredients'][
                        'coffee']
                    current_money -= MENU['espresso']['cost']
                    current_money = round(current_money, 2)
                    print("Here is your espresso ☕. Enjoy! ")
                    print(f"Here is ${current_money} dollars in change.")
                    current_money = 0
                    welcome()
                else:
                    current_money = 0
                    print("Sorry that's not enough money. Money refunded.")
                    welcome()
            else:
                print("Sorry there is not enough coffee.")
                welcome()
        else:
            print("Sorry there is not enough water.")
            welcome()

    if answer == 'latte':

        if MENU['latte']['ingredients']['water'] <= resources['water']:
            if MENU['latte']['ingredients']['coffee'] <= resources['coffee']:
                if MENU['latte']['ingredients']['milk'] <= resources['milk']:
                    print("Please, insert coins.")

                    quarters = float(input("How many quarters? "))
                    dimes = float(input("How many dimes? "))
                    nickles = float(input("How many nickles? "))
                    pennies = float(input("How many pennies? "))

                    current_money = round((0.25 * quarters) + (0.10 * dimes) +
                                          (0.05 * nickles) + (0.01 * pennies),
                                          2)
                    if current_money >= MENU['latte']['cost']:
                        resources['water'] -= MENU['latte']['ingredients'][
                            'water']
                        resources['coffee'] -= MENU['latte']['ingredients'][
                            'coffee']
                        resources['milk'] -= MENU['latte']['ingredients'][
                            'milk']
                        current_money -= MENU['latte']['cost']
                        current_money = round(current_money, 2)
                        print("Here is your latte ☕. Enjoy! ")
                        print(f"Here is ${current_money} dollars in change.")
                        current_money = 0
                        welcome()
                    else:
                        current_money = 0
                        print("Sorry that's not enough money. Money refunded.")
                        welcome()
                else:
                    print("Sorry there is not enough milk.")
                    welcome()
            else:
                print("Sorry there is not enough coffee.")
                welcome()
        else:
            print("Sorry there is not enough water.")
            welcome()

    if answer == 'cappuccino':

        if MENU['cappuccino']['ingredients']['water'] <= resources['water']:
            if MENU['cappuccino']['ingredients']['coffee'] <= resources[
                    'coffee']:
                if MENU['cappuccino']['ingredients']['milk'] <= resources[
                        'milk']:
                    print("Please, insert coins.")

                    quarters = float(input("How many quarters? "))
                    dimes = float(input("How many dimes? "))
                    nickles = float(input("How many nickles? "))
                    pennies = float(input("How many pennies? "))

                    current_money = round((0.25 * quarters) + (0.10 * dimes) +
                                          (0.05 * nickles) + (0.01 * pennies),
                                          2)
                    if current_money >= MENU['cappuccino']['cost']:
                        resources['water'] -= MENU['cappuccino'][
                            'ingredients']['water']
                        resources['coffee'] -= MENU['cappuccino'][
                            'ingredients']['coffee']
                        resources['milk'] -= MENU['cappuccino']['ingredients'][
                            'milk']
                        current_money -= MENU['cappuccino']['cost']
                        current_money = round(current_money, 2)
                        print("Here is your cappuccino ☕. Enjoy! ")
                        print(f"Here is ${current_money} dollars in change.")
                        current_money = 0
                        welcome()
                    else:
                        current_money = 0
                        print("Sorry that's not enough money. Money refunded.")
                        welcome()
                else:
                    print("Sorry there is not enough milk.")
                    welcome()
            else:
                print("Sorry there is not enough coffee.")
                welcome()
        else:
            print("Sorry there is not enough water.")
            welcome()


# print and ask the user for input on what type of coffee he wants
def welcome():
    global answer
    answer = input("\nWhat would you like?\n").lower()

    off()
    print_flavours()
    print_report()
    check()


print("Welcome to the Coffee Machine.")
print("'Flavours' for every flavour available and price.")
print("'Report' for the machine resources report.")
print("'OFF' to turn the machine off.")
welcome()
