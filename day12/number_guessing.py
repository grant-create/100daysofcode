import random

number = random.randint(1,100)

def play():
    difficulty=input("Number guessing game, choose a difficulty: Easy or Hard ").lower()

    if difficulty == "easy":
        count = 10
    else:
        count = 5
    
    user_guess = int(input("Guess a number between 1-100 "))
    while count != 0:
        if user_guess > number:
            print("Too High")
            count -= 1
            
        elif user_guess < number:
            print("Too Low")
            count -= 1
        print(f"You have {count} attempts remaining to guess the number")

        user_guess = int(input("Guess a number between 1-100 "))
    
        if user_guess == number:
            print("You Win!")
            break
            
play()

