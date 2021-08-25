import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
dealer_cards = []



# Deal cards
def deal(player_cards, dealer_cards):


    # print two random nums from list for player
    for num in range(2):
        rand = random.randint(0,(len(cards)-1))
        player_cards.append(cards[rand])
    
    # print one random for dealer (only supposed to show one)
    for num in range(2):
        rand = random.randint(0,(len(cards)-1))
        dealer_cards.append(cards[rand])
    print("Dealer's cards:", dealer_cards[0],"_")
    print("Your cards: ",player_cards)


# Hit or Pass
def hitpass():
    hit_or_pass = input("Would you like to hit or pass? h / p ")
    while hit_or_pass == "h" and sum(player_cards) <= 21:
        
    # if hit, add one more random num to player list
        if hit_or_pass == "h":
            rand = random.randint(0,(len(cards)-1))
            player_cards.append(cards[rand])
            
            
        # if hit and player has 11 and it goes over 21, subtract 10
            if 11 in player_cards and sum(player_cards) > 21:
                player_cards[player_cards.index(11)] = 1
        print("Your cards: ",player_cards, "Your total:", sum(player_cards))
        if sum(player_cards) == 21 or sum(player_cards) > 21: 
            hit_or_pass = "p"
        else:       
            hit_or_pass = input("would you like to hit or pass? h / p ") 
        
    # if pass, reveal dealers cards
    if hit_or_pass == "p":
        print("dealer's cards",dealer_cards)
        print("Your cards: ",player_cards)
        while sum(dealer_cards) < 16:
            rand = random.randint(0,(len(cards)-1))
            dealer_cards.append(cards[rand])
            sum(dealer_cards)
        print("Dealer's cards",dealer_cards)
        


# Win check 
def win_check():
    # check to see if player's cards are less than or equal to 21
    if sum(player_cards) > 21:
        print("Oh no, you went over 21, BUST")
    elif sum(dealer_cards) > 21 and sum(player_cards) < 21:
        print("The dealer went over, You Win!")
     

    # if dealer == 21 and player == 21, lose
    elif sum(player_cards) == sum(dealer_cards) and sum(player_cards) == 21:
        print("You tied the Dealer with Blackjack, LOSE")
    # elif dealer == player, draw
    elif sum(player_cards) == sum(dealer_cards):
        print("You tied the dealer! DRAW")
    # elif dealer > player, lose
    elif sum(dealer_cards) > sum(player_cards):
        print("The dealer beat you! LOSE")
    # else player wins
    elif sum(player_cards) == 21:
        print("Blackjack! Congratualtions!")
    elif sum(player_cards) > sum(dealer_cards):
        print("Player wins!")
    else:
        pass



deal(player_cards, dealer_cards)
hitpass()
win_check()