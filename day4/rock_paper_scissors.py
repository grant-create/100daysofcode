import random
move = int(input("Which do you choose? 0 for Rock, 1 for Paper, 2 for Scissors "))

rps = ["rock", "paper", "scissors"]

random_int = random.randint(0,2)
print(f"computer chose: {rps[random_int]} ||",f"you chose: {rps[move]}")
if random_int == move:
    print("tie game!")
elif move == random_int + 1:
    print("Player Wins!")

elif random_int == move + 1:
    print("Computer Wins!")
elif random_int - 2 == move:
    print("Player Wins!")
elif move - 2 == random_int:
    print("Computer Wins!")
elif move > 2:
    print(" you typed an invalid number")

