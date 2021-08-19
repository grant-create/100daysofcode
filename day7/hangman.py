import random

# while loop for tries/win
count = 0

word_list = ["aardvark", "baboon", "camel", "beekeeper"]
chosen_word = random.choice(word_list)
display = []
for thing in chosen_word:
    display.append("_")
x = ["".join(display)]
while count < 6 or "_" not in display:
    

    print(display, count)
    guess = input("Guess a letter: ").lower()
    count +=1
    


    for position in range(len(chosen_word)):
        
        if guess == chosen_word[position]:
            
            print("Right")
            display[position] = guess
            print(display)
        else:
            pass
