import random

# while loop for tries/win
count = 0

word_list = ["aardvark", "baboon", "camel", "beekeeper"]
chosen_word = random.choice(word_list)
display = []
for thing in chosen_word:
    display.append("_")
x = ["".join(display)]
end_of_game = False
while not end_of_game:
    

    print(display)
    print("turns left: ", count, "of 6")
    guess = input("Guess a letter: ").lower()
    count +=1
    


    for position in range(len(chosen_word)):
        
        if guess == chosen_word[position]:
            
            print("Right")
            display[position] = guess
            
        else:
            pass
    if "_" not in display:
        end_of_game = True
        print("you WIN!")
    elif count > 6:
        end_of_game = True
        print("LOSER")
    else:
        pass
