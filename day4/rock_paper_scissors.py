import random
move = int(input("Which do you choose? 0 for Rock, 1 for Paper, 2 for Scissors "))

rps = ["Rock", "Paper", "Scissors"]

random_int = random.randint(0,2)

if move <=2:
    print(f"Computer: {rps[random_int]} ||",f"You: {rps[move]}")

if random_int == move:
    print("tie game!")
elif move == random_int + 1:
    print("You Win!")
elif random_int == move + 1:
    print("Computer Wins!")
elif random_int - 2 == move:
    print("You Win!")
elif move - 2 == random_int:
    print("Computer Wins!")
elif move > 2:
    print(" you typed an invalid number")

