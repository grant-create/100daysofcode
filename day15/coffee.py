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
            if MENU[order]["ingredients"]["water"] >= water:
                water -=  MENU[order]["ingredients"]["water"]
            else:
                print("Not enough water")
                
            if MENU[order]["ingredients"]["milk"] >= milk:
                milk -=   MENU[order]["ingredients"]["milk"]
            else:
                print("Not enough milk")
                
            if MENU[order]["ingredients"]["coffee"] >= coffee:
                coffee -=  MENU[order]["ingredients"]["coffee"]
            else:
                print("Not enough coffee")
                
        
            


        elif order == "report":
            print(f"Water: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
        else:
            break
            
        order = input("would you like to order anything else? (cappicino/latte/espresso, report, off) ")
get_coffee()























































