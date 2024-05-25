# PyBJ (PythonBJ, PythonBlackJack, etc)
#
# RULES:
# dealer cards predetermined
# players bet
# player(s) keep hitting cards, card scores range from 1-10 points depending on how much the card is, king/queen/jack is 10 points, ace is 1 or 11 points
# cannot go over 21 points.
# one of dealers card is shown, other is secret. after hitting is done, if dealer point is under 16, required to hit, 17 or over required to stay.
# player with 21 points/highest score without going over 21 wins.
#
# TO-DO:
# - Add saving system
# - Add text-based GUI 
# - Make graphical GUI (in the future)

import random
import sys
import csv

money = 100
bet = 0
pts = 0
dealerpts = 0
starterdeck = 0

carddb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jack", "Ace"]
cardtypedb = ["♠", "♥"]
dealeracechoice = [1, 11]

dealerdeck = []
deck = []

name = input("Enter your name: ")

def intro():
    global name
    global money
    global bet
    global dealerpts
    global pts
    global starterdeck
    global dealerdeck
    global deck

    bet = 0
    pts = 0
    dealerpts = 0
    starterdeck = 0
    dealerdeck = []
    deck = []
    
    if money == 0:
        print("\nGame over. You're out of money!")
        sys.exit()

    bet = int(input("\nWelcome, " + name + "!\nMoney: " + str(money) + "\nHow much do you wish to bet? "))
    while bet > money:
        print("You can't bet what you don't have!")
        bet = int(input("Money: " + str(money) + "\nHow much do you wish to bet? "))
    dealer()

def dealer():
    global money
    global pts
    global dealerpts
    global carddb
    global cardtypedb
    global starterdeck
    global dealerdeck
    global deck
    if starterdeck == 0:
        for x in range(0,2):
            cardselect = random.choice(carddb)
            cardtypeselect = random.choice(cardtypedb)
            dealerdeck.append(str(cardselect) + " of " + str(cardtypeselect))
            if cardselect == "Queen" or cardselect == "King" or cardselect == "Jack":
                dealerpts += 10
            elif cardselect == "Ace":
                dlrchoice = random.choice(dealeracechoice)
                dealerpts += dlrchoice
            else:
                dealerpts += cardselect          
            print("Dealer's score: ???")
            player()
    elif starterdeck == 1:
        if dealerpts >= 17:
            print("Dealer stands.")
            endgame()
        elif dealerpts <= 16:
            cardselect = random.choice(carddb)
            cardtypeselect = random.choice(cardtypedb)
            dealerdeck.append(str(cardselect) + " of " + str(cardtypeselect))
            print("Dealer has picked out a new card!")
            if cardselect == "Queen" or cardselect == "King" or cardselect == "Jack":
                dealerpts += 10
            elif cardselect == "Ace":
                dlrchoice = random.choice(dealeracechoice)
                dealerpts += dlrchoice
            else:
                dealerpts += cardselect          
            print("Dealer's score: " + str(dealerpts))
            endgame()

def player():
    global money
    global pts
    global dealerpts
    global carddb
    global cardtypedb
    global starterdeck
    global deck
    global dealerdeck
    if starterdeck == 0:
        for x in range(0,2):
            cardselect = random.choice(carddb)
            cardtypeselect = random.choice(cardtypedb)
            deck.append(str(cardselect) + " of " + str(cardtypeselect))
            if cardselect == "Queen" or cardselect == "King" or cardselect == "Jack":
                pts += 10
            elif cardselect == "Ace":
                plrchoice = input("You got an ace!\nA - Add 11 points\nB - Add 1 point?\n")
                if plrchoice.upper() == "A":
                    pts += 11
                elif plrchoice.upper() == "B":
                    pts += 1
                else:
                    print("Invalid answer. Adding 1 point.")
                    pts += 1
            else:
                pts += cardselect
            starterdeck = 1
    if pts > 21:
        print("Bust!")
        money -= bet
        intro()
    if pts == 21:
        endgame()
    else:
        print("\nDealer's Deck:")
        for x in range(0, len(dealerdeck) + 1):
            if x == 1:
                print("???")
            else:
                print(dealerdeck[x])
        print("\nYour Deck:")
        for x in range(0, len(deck)):
            print(deck[x])
        decision = input("\nYour Points: " + str(pts) + "\nDo you wish to hit or stand?\nH - Hit\nS - Stand\n")
        if decision.upper() == "H":
            cardselect = random.choice(carddb)
            cardtypeselect = random.choice(cardtypedb)
            deck.append(str(cardselect) + " of " + str(cardtypeselect))
            print("\nCard: " + str(cardselect) + " of " + str(cardtypeselect))
            if cardselect == "Queen" or cardselect == "King" or cardselect == "Jack":
                pts += 10
            elif cardselect == "Ace":
                plrchoice = input("You got an ace!\nA - Add 11 points\nB - Add 1 point?\n")
                if plrchoice.upper() == "A":
                    pts += 11
                elif plrchoice.upper() == "B":
                    pts += 1
                else:
                    print("Invalid answer. Adding 1 point.")
                    pts += 1
            else:
                pts += cardselect
            player()
        elif decision.upper() == "S":
            dealer()

def endgame():
    global money
    global bet
    global dealerpts
    global pts
    global deck
    global dealerdeck
    if dealerpts > pts:
        print("Dealer wins!\n")
        money -= bet
        intro()
    if pts > dealerpts:
        print("You win!\n")
        money += bet * 2
        intro()
    if dealerpts == pts:
        print("Draw!\n")
        intro()
    print("\nDealer's Deck:")
    for x in range(0, len(dealerdeck)):
        print(dealerdeck[x])
    print("\nYour Deck:")
    for x in range(0, len(deck)):
        print(deck[x])


if money != 0:
    intro()
