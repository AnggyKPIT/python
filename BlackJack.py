import random
deck=[11, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score_u=0
score_pc=0

def give_me_one(visibility,req,pos):
    random_card=random.choice(deck)
    if visibility==True:
        print("\n%s Card for %s: %d"%(pos,req,random_card))
    else:
        print("\n%s Card for %s: ?"%(pos,req))
    return random_card

def check_cards(cards_list,who):
    total=sum(cards_list)
    if total==21:
        if who!="Dealer":
            print("\nWe have a Winner! 21!!")
        return "winner"
    if total<21:
        return "still"
    if total>21:
        if who!="Dealer":
            print("\nYou went too far..  %d!"%total)
        else:
            print("\nThe Dealer went too far..  %d! You WIN!"%total)
        return "loser"

def compare(user,pc,name):
    user_total=sum(user)
    pc_total=sum(pc)
    print("\nYour cards total: %d"%user_total)
    print("\nDealer's cards total: %d"%pc_total)
    if user_total>pc_total:
        print("\nWe have a Winner! %s!"%name)
        return "user"
    elif user_total<pc_total:
        print("\nThe Dealer Won!")
        return "dealer"
    else:
        print("\nWe have a tie")
        return "tie"
    
name=input("Welcome! Who is going to play?: ")
while(True):
    user_cards=[]
    pc_cards=[]
    statusU="none"
    statusPC="none"
    final_winner="none"
    user_cards.append(give_me_one(True,name,"1st"))
    user_cards.append(give_me_one(True,name,"2nd"))
    pc_cards.append(give_me_one(True,"Dealer","1st"))
    pc_cards.append(give_me_one(False,"Dealer","2nd"))
    statusU=check_cards(user_cards,name)
    while(statusU=="still"):
        resp=input("%s, Do you want an extra card? (y/n): "% name)
        if resp=="y":
            user_cards.append(give_me_one(True,name,"Additional"))
            statusU=check_cards(user_cards,name)
        if resp=="n" or statusU=="loser":
            break
    if statusU=="still":
        while(sum(pc_cards)<17):
            pc_cards.append(give_me_one(True,"Dealer","Additional"))
        statusPC=check_cards(pc_cards,"Dealer")
    print(user_cards,pc_cards)
    if (statusPC=="still" and statusU=="still") or statusPC=="winner":
        final_winner=compare(user_cards,pc_cards,name)
    if statusU=="winner" or final_winner=="user" or statusPC=="loser":
        score_u+=1
    if statusPC=="winner" or final_winner=="dealer" or statusU=="loser":
        score_pc+=1
    print("\nYour cards total: %d"% sum(user_cards))
    print("Dealer's cards total: %d"% sum(pc_cards))
    print("\n%s Score: %d\n%s Score: %d\n"%(name, score_u, "Dealer's", score_pc))
    while True:
        resp_continue = input("Do you want to play another one? (y/n): ")
        if resp_continue == "n" or resp_continue == "y":
            break
    if resp_continue == "n":        
        if score_pc > score_u:
            print("\nSee you... Loser")
        else:
            print("\nCome back soon!")
        break
    print("**********************************************")

