from menu import resources, MENU


def process_coins(option):
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    change = verify(option,total)
    print(f"Your change is: {change}")


def verify(item, value):
    if value >= item:
        return value - item
    else:
        print("Sorry, not enough cash")


def resources_management(input):
    if resources['water'] > input['water']:
        resources['water'] -= input['water']
    else:
        print("Sorry, there's not enough water")
    if resources['milk'] > input['milk']:
        resources['milk'] -= input['milk']
    else:
        print("Sorry, there's not enough milk")
    if resources['coffee'] > input['coffee']:
        resources['coffee'] -= input['coffee']
    else:
        print("Sorry, there's not enough coffee")

    return resources


def espresso():
    commit = input(f"An espresso is ${MENU['espresso']['cost']}. Confirm this order?:")
    if commit.lower() == 'yes':
        process_coins(MENU['espresso']['cost'])
        resources_management(MENU['espresso']['ingredients'])
    else:
        run()


def latte():
    commit = input(f"A latte is ${MENU['latte']['cost']}. Confirm this order?:")
    if commit.lower() == 'yes':
        process_coins(MENU['latte']['cost'])
        resources_management(MENU['latte']['ingredients'])
    else:
        run()


def cappuccino():
    commit = input(f"A cappuccino is ${MENU['cappuccino']['cost']}. Confirm this order?:")
    if commit.lower() == 'yes':
        process_coins(MENU['cappuccino']['cost'])
        resources_management(MENU['cappuccino']['ingredients'])

    else:
        run()


def run():
    end = False
    while not end:
        choice = int(input('What would you like?\nPress 1 for a ingredient report\nPress 2 for a Espresso\nPress 3 for a Latte\nPress 4 for a Cappuccino\n'))
        if choice == 1:
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        elif choice == 2:
            espresso()
        elif choice == 3:
            latte()
        elif choice == 4:
            cappuccino()
        else:
            print("Please insert a valid option.")

        should_continue = input("Do you wish to make another purchase? ")
        if should_continue.lower() == 'no':
            print("Thanks for buying from the Python Coffee Machine!")
            end = True
        else:
            run()

run()


