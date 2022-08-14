from art import logo
from menu import MENU, resources

# TODO: 1. Prompt user by asking 'What would you like? Espressor, latte or capuccino?'. Print drink menu with prices.

# TODO: 2. Turn of the coffee machine by entering off to the prompt

# TODO: 3. Print report of the machine's resources eg. water, milk, coffee, and money quantities.

# TODO: 4. When the user selects a drink, the program will check if there are enough resources to make it. If no,
#           the program will print "Sorry there is not enough water, milk etc."
# TODO: 5. If the resources are sufficient, the program will ask how many coins they want to insert. the total amount of coins
#           will be calculated and the program will check if the money is sufficient to purchase the drink. If the amount inserted
#           is not sufficient, the program will print "Sorry that's not sufficient money. Money refunded."
#           c. If too much money was inserted, the machine will offer change. Print: "Here is $2.45 dollars in change." The change
#           will be rounded to two decimal places.
# TODO: 6. Once the transaction is successful, the ingredients needed to make the drink will be subtracted from the machine's current
#           resources. A report will be created before and after creating the drink. b. Once the drink is created, the program
#           will print "Here is your {drink}. Enjoy!"


def menu():
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    menu = "Espresso: $" + str(espresso_cost) + "\nLatte: $" + \
        str(latte_cost) + "\nCappuccino: $" + str(cappuccino_cost) + "\n"
    print(logo)
    print("Welcome to Coffee Express!\nPlease have a look at our money and make a selection.")
    return menu
    # return "Espresso: $" + str(espresso_cost) + "\nLatte: $" + str(latte_cost) + "\nCappuccino: $" + str(cappuccino_cost) + "\n"

# Function calculates how much money the user has given the machine


def money_calculator(num_quarters, num_dimes, num_nickels, num_pennies):
    total = float(num_quarters) * 0.25 + float(num_dimes) * 0.1 + \
        float(num_nickels) * 0.05 + float(num_pennies) * 0.01
    return total

# Function takes sum total of money entered as input and outputs the calculated change if money is more than the price of the coffee


def change_calculator(money, coffee_price):
    change = money - coffee_price

    if change > 0:
        return round(change, 2)
    elif change < 0:
        return "Sorry, that's not enough money. Money refunded"

# Function handles money input and outputs the number of quarters, dimes, nickels and pennies


def accept_money():
    print("Please insert coins.\n")
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickels = input("How many nickels? ")
    pennies = input("How many pennies? ")

    return quarters, dimes, nickels, pennies


# Function initializes coffee machine
def coffee_machine_init():
    program_on = True
    coffee_machine_off = False

    water_remaining = resources["water"]
    milk_remaining = resources["milk"]
    coffee_remaining = resources["coffee"]

    while program_on:

        while not coffee_machine_off:
            print(menu())
            user_input = input("What would you like?: ")

            if user_input == "espresso":
                # Function will be called which will check if there are sufficient resources to make the drink
                quarters, dimes, nickels, pennies = accept_money()

                sum_total = money_calculator(
                    num_quarters=quarters, num_dimes=dimes, num_nickels=nickels, num_pennies=pennies)
                espresso_price = MENU["espresso"]["cost"]

                print(
                    f"Your change: {change_calculator(sum_total, espresso_price)}")
                print(sum_total)
                print(f"Water: {resources}")

            elif user_input == "latte":
                print("latte")
            elif user_input == "cappuccino":
                print("cappuccino")
            else:
                print("Please enter either 'espresso', 'latte', or 'cappuccino'.\n")
                program_on = False


start_coffee_machine = input(
    "Turn on coffee machine? Type 'y' if yes and 'n' if no.\n")

if start_coffee_machine == 'y':
    coffee_machine_init()
