print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
people = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to leave? 10, 12, 15, 20? "))

pay = round((total + (total*(tip/100)))/people,2)

print(f"Each person should pay: {pay}")