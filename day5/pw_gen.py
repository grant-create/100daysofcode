import random
chars = [
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
['!', '#', '$', '%', '&', '(', ')', '*', '+']
]
print("Welcome to the PyPassword Generator!")
letters= int(input("How many letters would you like in your password?\n")) 
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))
listofoptions = [letters, symbols, numbers]
names = ["letters", "symbols", "numbers"]

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw = []
total_len = letters + symbols + numbers
count = 0

for x in range(0,total_len):
    count +=1
    #pick a letter, number, symbol
    pick = random.randint(0,2)
    
    # make sure that if one is at 0, another will be picked in it's place
    while listofoptions[pick] == 0:
        pick = random.randint(0,2)

    # subtract number from item count
    listofoptions[pick] -= 1

    # This print statement for testing along the way:
    # print(names[pick],listofoptions[pick])

    # pick a random item within the sub list (minus 1 bc len and indexing are different)
    addtopw = random.randint(0, (len(chars[pick])-1))

    #add random char within to pw
    pw.append(chars[pick][addtopw])

# Join the list together
secure_pw = ["".join(pw)]
        
# print(count, len(pw))

# The secure password!!!
print(secure_pw[0])