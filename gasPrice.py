def gas_price(prev_price, new_price):
    #Percent equation takes the two price inputs and determines the percent
    #difference between them and are taken in whole numbers, as
    #seen in the if statements that follow.
    percent = ((new_price - prev_price)/prev_price) * 100
    if percent <= 0:
        return 'Full Tank'
    elif percent < 20:
        return '3/4 Tank'
    elif percent >= 20 and percent < 80:
        return 'Half Tank'
    elif percent >= 80 and percent < 100:
        return '1/4 Tank'
    else:
        return 'Go Home'

def level(num_coins, difficulty):
    #'if' and 'elif' statements get string value of difficulty
    #and use them to divide the total num_coins by the value
    #given to us for each difficulty (4, 4, 6, 6, 8, 10).
    if difficulty == 'Beginner':
        return int(num_coins/4)
    elif difficulty == 'Amateur':
        return int(num_coins/4)
    elif difficulty == 'Intermediate':
        return int(num_coins/6)
    elif difficulty == 'Pro':
        return int(num_coins/6)
    elif difficulty == 'Expert':
        return int(num_coins/8)
    elif difficulty == 'Legendary':
        return int(num_coins/10)
    else:
        #Really shouldn't execute, but it's here.
        return 'error'

def card_game(player1_card, player2_card, tiebreak_with_card):
    #For the 2 upcoming if groupings, subtracted in increments of 13
    #since there is 13 cards per suit, so increments will be
    #0, 13, 26, 39.
    
    #Determining suit and value given input of player1_card
    card1_suit = 0
    card1_value = 0
    if player1_card >= 1 and player1_card <= 13:
        card1_suit = 1
        card1_value = player1_card
    elif player1_card >= 14 and player1_card <= 26:
        card1_suit = 2
        card1_value = player1_card - 13
    elif player1_card >= 27 and player1_card <= 39:
        card1_suit = 3
        card1_value = player1_card - 26
    elif player1_card >= 40 and player1_card <= 52:
        card1_suit = 4
        card1_value = player1_card - 39
    else:
        #Really shouldn't execute, but it's here.
        return 'error'

    #Similar to player1_card, just applying it to player2_card.
    card2_suit = 0
    card2_value = 0
    if player2_card >= 1 and player2_card <= 13:
        card2_suit = 1
        card2_value = player2_card
    elif player2_card >= 14 and player2_card <= 26:
        card2_suit = 2
        card2_value = player2_card - 13
    elif player2_card >= 27 and player2_card <= 39:
        card2_suit = 3
        card2_value = player2_card - 26
    elif player2_card >= 40 and player2_card <= 52:
        card2_suit = 4
        card2_value = player2_card - 39
    else:
        #Really shouldn't execute, but it's here.
        return 'error'

    #Values to determine winner.
    if card1_suit < card2_suit and card1_value > card2_value:
        return 'Player 1 Wins'
    elif card2_suit < card1_suit and card2_value > card1_value:
        return 'Player 2 Wins'
    else:
        #Can not end with tie, as the tie break conditions
        #still need to be applied.
        if tiebreak_with_card == True:
            if card1_value > card2_value:
                return 'Player 1 Wins'
            elif card1_value < card2_value:
                return 'Player 2 Wins'
            else:
                return 'Tie'
        elif tiebreak_with_card == False:
            if card1_suit < card2_suit:
                return 'Player 1 Wins'
            elif card2_suit < card1_suit:
                return 'Player 2 Wins'
            else:
                return 'Tie'
        else:
            #Probably isn't used, but here to act as a safety net.
            return 'Tie'
    
    


