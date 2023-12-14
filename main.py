from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_completed = False

def start():
    global is_completed
    while not is_completed:
        available_items = menu.get_items()
        answer = input(f'What would you like to make?({available_items})')
        if answer.lower() == 'report':
            coffee_maker.report()
            money_machine.report()
        elif answer.lower() == 'off':
            is_completed = True
            return
        else:
            drink = menu.find_drink(answer.lower())
            if drink and coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


start()