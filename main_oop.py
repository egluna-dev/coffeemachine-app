from menu_oop import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()

total_profit = 0

program_on = True

while program_on:
    menu_items = my_menu.get_items()

    customer_order = input(
        "What drink would you like to buy? (espresso/latte/cappuccino):\n")

    if customer_order == "off":
        program_on = False

    elif customer_order == "report":
        my_coffee_maker.report()
        money_machine.report()
    else:
        drink_item = my_menu.find_drink(customer_order)
        drink_selected = drink_item.name
        drink_cost = drink_item.cost
        drink_ingredients = drink_item.ingredients

        sufficient_resources = my_coffee_maker.is_resource_sufficient(
            drink_item)
        if sufficient_resources:
            sufficient_money = money_machine.make_payment(drink_cost)
            if sufficient_money:
                my_coffee_maker.make_coffee(drink_item)
