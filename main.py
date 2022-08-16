from logo import logo
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

# GLOBAL VARIABLE
profit_sum = 0

# Function prints menu to display to customer


def menu():
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    menu = "Espresso: $" + str(espresso_cost) + "\nLatte: $" + \
        str(latte_cost) + "\nCappuccino: $" + str(cappuccino_cost) + "\n"
    print("Welcome to Coffee Express!\nPlease have a look at our money and make a selection.")
    return menu
    # return "Espresso: $" + str(espresso_cost) + "\nLatte: $" + str(latte_cost) + "\nCappuccino: $" + str(cappuccino_cost) + "\n"

# Function calculates how much money the user has given the machine


def money_calculator():
    num_quarters = int(input("Number of quarters: ")) * 0.25
    num_dimes = int(input("Number of dimes: ")) * 0.10
    num_nickels = int(input("Number of nickels: ")) * 0.05
    num_pennies = int(input("Number of pennies: ")) * 0.01
    total = num_quarters + num_dimes + num_nickels + num_pennies
    return total

# Function checks if the current resources are sufficient to make the drink


def resources_sufficient(drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(
                f"Not enough resources to make your drink. More {ingredient} required.")
            return False
        else:
            return True

# Function handles money input and outputs the number of quarters, dimes, nickels and pennies


def transaction_successful(money_inserted, drink_price):
    if money_inserted >= drink_price:
        change = round(money_inserted - drink_price, 2)
        print(f"Here is your change: ${change}")
        global profit_sum
        profit_sum += drink_price
        return True
    else:
        print(
            "Sorry, that's not enough money. The drink is ${drink_price}. Money refunded.\n")


# Function creates report of current machine resources


def print_report(current_resources, money_available):
    for resource in current_resources:
        if resource == "water":
            print(f"W{resource[1:]}: {current_resources[resource]}ml")
        elif resource == "milk":
            print(f"M{resource[1:]}: {current_resources[resource]}ml")
        else:
            print(f"C{resource[1:]}: {current_resources[resource]}g")
    print(f"Money: ${money_available}")


# Function takes the drink as input and subtracts the required ingredients from the current resources


def make_coffee(drink_selected, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink_selected}, enjoy!")


# Function initializes coffee machine
program_on = True

water_remaining = resources["water"]
milk_remaining = resources["milk"]
coffee_remaining = resources["coffee"]

print(logo)

while program_on:
    menu()
    selection = input("What would you like?: ")

    if selection == "off":
        program_on = False
    elif selection == "report":
        print_report(resources, money_available=profit_sum)
    else:
        drink = MENU[selection]
        if resources_sufficient(drink["ingredients"]):
            payment = money_calculator()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(selection, drink["ingredients"])
