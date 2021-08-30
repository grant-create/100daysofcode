"""
Create a game called higher or lower. two random names + descriptions are given and the user needs to pick
which one has a higher following (on instagram?)





"""
from game_data import data
from random import randint

game_over = False
count = 0

# get random person vs another random person
# data[random1] data[random2]
# make sure thhey are not the same

rand1 = randint(0, (len(data)-1))
name1 = data[rand1].get("name")
desc1 = data[rand1].get("description")
country1 = data[rand1].get("country")
while game_over == False:
    rand2 = randint(0, (len(data)-1))
    while rand1 == rand2:
        rand2 = randint(0, (len(data)-1))
    
    name2 = data[rand2].get("name")
    desc2 = data[rand2].get("description")
    country2 = data[rand2].get("country")

    print("")
    print(f"Compare A: {name1}, a {desc1} from {country1}.")
    print("")
    print("VS")
    print("")
    print(f"Compare B: {name2}, a {desc2} from {country2}.")
    print("")



    guess = input("A or B ").lower()
    print("")
    if (guess[0] == "a" and data[rand1].get("follower_count") > data[rand2].get("follower_count")) or ( guess[0] == "b" and data[rand1].get("follower_count") < data[rand2].get("follower_count")):
        count +=1
        print("Nice, you got it")
        print("")
        print(f"score: {count}")
        name1 = name2
        desc1 = desc2
        country1 = country2
    
    else:
        game_over = True
        print("oh no you lost, looks like you arent as into celebrities social media following as you thought")
        print(f"score: {count}")
