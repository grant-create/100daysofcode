from machineinfo import MENU
from machineinfo import resources
"""
What would you like? (espresso/latte/capuccino): 
or 
report - tells how much of each ingredient we have (including money)
or 
off

need prices for each drink and be able to calculate change from money inserted

remove ingredients after each transaction
"""
quarter = .25
dime = .1
nickel = .05
penny =.01


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

def get_coffee():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    order = input("What would you like to order ")
    while order != 'off':
        if order in MENU:
            print(f"The {order} costs:",MENU[order]["cost"])

            if MENU[order]["ingredients"]["water"] <= water:
                water -=  MENU[order]["ingredients"]["water"]
            else:
                print("Not enough water")
                
            if MENU[order]["ingredients"]["milk"] <= milk:
                milk -=   MENU[order]["ingredients"]["milk"]
            else:
                print("Not enough milk")
                
            if MENU[order]["ingredients"]["coffee"] <= coffee:
                coffee -=  MENU[order]["ingredients"]["coffee"]
            else:
                print("Not enough coffee")
            if (MENU[order]["ingredients"]["water"] <= water) and (MENU[order]["ingredients"]["milk"] <= milk) and (MENU[order]["ingredients"]["coffee"] <= coffee):
                print(f'That will cost: {MENU[order]["cost"]}')
                print("How will you pay for that?")
                quarters = int(input("Quarters: ")) * quarters
                dimes = int(input("Dimes: ")) * dime
                nickels = int(input("Nickels: ")) * nickel
                pennies = int(input("Pennies: ")) * penny
                
                user_pay = quarters + dimes + nickels + pennies
                
        
            


        elif order == "report":
            print(f"Water: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
        else:
            break
            
        order = input("would you like to order anything else? (cappicino/latte/espresso, report, off) ")
get_coffee()























































