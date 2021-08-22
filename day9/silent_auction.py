# Silent auction: 
from IPython.display import clear_output
end = False

# dictionary
silent_dictionary= {}

# While loop to allow continuous inputs
while end != True:


  

    # input for users to enter their bid
    name = input("Please enter your name ")
    bid = int(input("please enter your bid "))
    
    # add inputs to dictionary

    silent_dictionary[name] = bid
    print(silent_dictionary)
    # check for end of while loop
    signal = input("Are there any more bids? y/n ")
    if signal == "n":
        end = True
        sorted_bids = dict(sorted(silent_dictionary.items(), key=lambda item: item[1]))
        els = list(sorted_bids.items())
        print(els[-1], "is the winner!")
        

    else:
        
        clear_output()


# order the dictionary and return the winner