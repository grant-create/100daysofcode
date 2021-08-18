print("Welcome to Treasure Island adventure")
first_choice = input("You're at a cross roads which way do you go? left or right?").lower()
if first_choice == "left":
    print("Oh no, you ran into a monster and died")
else:
    boat = input("you come to a lake. There is an island. Type wait to wait for a boat, type swim to swim to the island").lower()

    if boat == "swim":
        print("oh no! you get caught by the giant lamprey and drown")
    else:
        doors = input("You arrive at a house with 3 doors marked 1, 2, 3 which do you choose?").lower()

        if doors == "1":
            print("you found a room full of treasure! Neat!")
        else:
            print("It's a room full of fire, Game over")