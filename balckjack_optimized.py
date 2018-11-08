"""
BlackJack Game
"""
import random
DECK_CARDS = [11, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SCORE_USER = 0
SCORE_PC = 0

def give_me_one(visibility, req, pos):
    """
    It generates and prints a random card
    """
    random_card = random.choice(DECK_CARDS)
    if visibility:
        print("\n%s Card for %s: %d"%(pos, req, random_card))
    else:
        print("\n%s Card for %s: ?"%(pos, req))
    return random_card

def check_cards(cards_list, who):
    """
    Check Total of cards and status before Dealer plays
    """
    total = sum(cards_list)
    if total == 21:
        if who != "Dealer":
            print("\nWe have a Winner! 21!!")
        response = "winner"
    if total < 21:
        response = "still"
    if total > 21:
        if who != "Dealer":
            print("\nYou went too far..  %d!"%total)
        else:
            print("\nThe Dealer went too far..  %d! You WIN!"%total)
        response = "loser"
    return response

def compare(user, dealer, name):
    """
    Compare final total of cards, if no one pass beyond 21
    """
    user_total = sum(user)
    pc_total = sum(dealer)
    if user_total > pc_total:
        print("\nWe have a Winner! %s!"%name)
        response = "user"
    elif user_total < pc_total:
        print("\nThe Dealer Won!")
        response = "dealer"
    else:
        print("\nWe have a tie")
        response = "tie"
    return response

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
        if RESP_CARD == "n" or STATUS_USER == "loser":
            break
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
        if RESP_CONTINUE == "n" or RESP_CONTINUE == "y":
            break
    if RESP_CONTINUE == "n":        
        if SCORE_PC > SCORE_USER:
            print("\nSee you... Loser")
        else:
            print("\nCome back soon!")
        break
    print("**********************************************")

