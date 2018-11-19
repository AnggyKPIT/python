"""
BlackJack is a comparing card game between the player and the dealer.

The objective of the game is to beat the dealer in one of the following ways:
    *Get 21 points on the first two cards, called Blackjack.
    *Reach a final score higher than the dealer without exceeding 21.
    *Let the dealer draw additional cards until their hand exceeds 21.

Game:
    -First, the user receives 2 cards and the dealer is also dealt two cards,
    one exposed and one hidden.
    -A hand's value is the sum of the card values.
    -The user is allowed to draw additional cards to improve the hand.
    -Once the player has completed the hand, it is the dealer's turn.
    -The dealer then reveals the hidden card and must hit until
    the cards total 17 or more points.

"""
import random
DECK_CARDS = [11, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SCORE_USER = 0
SCORE_PC = 0

def give_me_one(visibility, requester, position):
    """
    It generates an prints a random card
    INPUTS  - visibility: false for dealer's second card
            - requester: Dealer or User
            - position: number of card

    OUTPUT  -random card
    """
    random_card = random.choice(DECK_CARDS)
    if visibility:
        print("\n%s Card for %s: %d"%(position, requester, random_card))
    else:
        print("\n%s Card for %s: ?"%(position, requester))
    return random_card

def check_cards(cards_list, who):
    """
    Check Total of cards before the Dealer draws additional cards
    INPUT   -cards_list: list of cards to sum
            -who: Dealer or User cards

    OUTPUT  -status: status after sum of cards (winner, still playing or loser)
    """
    total = sum(cards_list)
    if total == 21:
        if who != "Dealer":
            print("\nWe have a Winner! 21!!")
        status = "winner"
    if total < 21:
        status = "still"
    if total > 21:
        if who != "Dealer":
            print("\nYou went too far..  %d!"%total)
        else:
            print("\nThe Dealer went too far..  %d! You WIN!"%total)
        status = "loser"
    return status

def compare(user_cards, dealer_cards, name):
    """
    Compare final total of cards, after no one pass beyond 21
    INPUT:  -user_cards: user's cards
            -dealer_cards: dealer's cards
            -name: name of user
    OUTPUT: -status: winner (user or dealer) or tie
    """
    user_total = sum(user_cards)
    pc_total = sum(dealer_cards)
    if user_total > pc_total:
        print("\nWe have a Winner! %s!"%name)
        status = "user"
    elif user_total < pc_total:
        print("\nThe Dealer Won!")
        status = "dealer"
    else:
        print("\nWe have a tie")
        status = "tie"
    return status

NAME = input("Welcome! Who is going to play?: ")
while True:
    FINAL_WINNER = "none"
    STATUS_USER = "none"
    STATUS_PC = "none"
    USER_CARDS = []
    PC_CARDS = []
    USER_CARDS.append(give_me_one(True, NAME, "1st"))
    USER_CARDS.append(give_me_one(True, NAME, "2nd"))
    PC_CARDS.append(give_me_one(True, "Dealer", "1st"))
    PC_CARDS.append(give_me_one(False, "Dealer", "2nd"))
    STATUS_USER = check_cards(USER_CARDS, NAME)
    while STATUS_USER == "still":
        RESP_CARD = input("%s, Do you want an extra card? (y/n): "% NAME)
        if RESP_CARD == "y":
            USER_CARDS.append(give_me_one(True, NAME, "Additional"))
            STATUS_USER = check_cards(USER_CARDS, NAME)
        elif RESP_CARD == "n" or STATUS_USER == "loser":
            break
        else: print("You should only enter 'y' or 'n'")
    if STATUS_USER == "still":
        while sum(PC_CARDS) < 17:
            PC_CARDS.append(give_me_one(True, "Dealer", "Additional"))
        STATUS_PC = check_cards(PC_CARDS, "Dealer")
    print(USER_CARDS, PC_CARDS)
    if (STATUS_PC == "still" and STATUS_USER == "still") or STATUS_PC == "winner":
        FINAL_WINNER = compare(USER_CARDS, PC_CARDS, NAME)
    if STATUS_USER == "winner" or FINAL_WINNER == "user" or STATUS_PC == "loser":
        SCORE_USER += 1
    if STATUS_PC == "winner" or FINAL_WINNER == "dealer" or STATUS_USER == "loser":
        SCORE_PC += 1
    print("\nYour cards total: %d"% sum(USER_CARDS))
    print("Dealer's cards total: %d"% sum(PC_CARDS))
    print("\n%s Score: %d\n%s Score: %d\n"%(NAME, SCORE_USER, "Dealer's", SCORE_PC))
    while True:
        RESP_CONTINUE = input("Do you want to play another one? (y/n): ")
        if RESP_CONTINUE in ("n", "y"):
            break
        else: print("You should only enter 'y' or 'n'")
    if RESP_CONTINUE == "n":
        if SCORE_PC > SCORE_USER:
            print("\nSee you... Loser")
        else:
            print("\nCome back soon!")
        break
    print("**********************************************")
