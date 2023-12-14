# OOP Virtual Coffee Machine

## Overview
This Python project simulates a virtual coffee machine using Object-Oriented Programming (OOP). It consists of several classes that handle different aspects of a coffee machine, such as making coffee, handling menu items, and processing payments. Users can select drinks from a menu, pay with virtual coins, and the machine checks for sufficient resources before making the drink.

## Features
- **Menu Selection**: Offers a selection of coffee drinks including latte, espresso, and cappuccino.
- **Resource Management**: Checks if there are enough ingredients to make the chosen drink.
- **Payment Processing**: Simulates the insertion and calculation of coins, and checks if the payment is enough for the selected drink.
- **Coffee Making**: Prepares the chosen coffee if the resources and payment are sufficient.
- **Reporting**: Provides a report of the machine's resources and total earnings.

## Modules and Classes
- `Menu`: Manages the drinks available in the coffee machine.
- `MenuItem`: Represents an individual drink item with its ingredients and cost.
- `CoffeeMaker`: Handles the making of coffee and tracks the machine's resources.
- `MoneyMachine`: Manages the processing of virtual coins and payments.

## How to Run the Project
1. Ensure Python is installed on your system.
2. Create the following Python files: `main.py`, `menu.py`, `coffee_maker.py`, and `money_machine.py`.
3. Copy the provided code into the respective files.
4. Run `main.py` to start the coffee machine program.

## How to Use
1. When prompted, enter the name of the coffee you'd like to purchase (latte, espresso, or cappuccino).
2. Follow the instructions to insert virtual coins.
3. The machine will check if you have inserted enough money and if it has the necessary resources to make your drink.
4. If the transaction is successful, your coffee is prepared. If not, your money is refunded.
5. Type 'report' to view the machine's current resources and earnings.
6. Type 'off' to turn off the machine.

## Dependencies
- This project does not require any external libraries.

## Note
This script is a simulation and does not involve real transactions or physical coffee making. It's designed for educational purposes, particularly to demonstrate the use of OOP in Python.

---

Enjoy your virtual coffee-making experience!