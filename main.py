from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

koffiemachine = CoffeeMaker()
kassa = MoneyMachine()

continue_dispensing = True
while continue_dispensing:
    choice = input("What would you like? " + (Menu().get_items()) + ": ")

    if choice == "off":
        continue_dispensing = False

    elif choice == "report":
        koffiemachine.report()
        kassa.report()

    else:
        drink_in_menu = Menu().find_drink(choice)
        if koffiemachine.is_resource_sufficient(drink_in_menu):
            if kassa.make_payment(drink_in_menu.cost):
                koffiemachine.make_coffee(drink_in_menu)
