"""We are going to make the user play a game/s of Black Jack
standard rules over 21 is bust and dealer deals until at least 17"""

import random
import sys
import time

#Intro upon first opening the code
print("""\nHello welcome to Black Jack! \n
The rules are simple if your cards added up are higher than the dealers
you win, but make sure you don't go over 21 or you'll bust and loss the game
""")

#adding a value to the list representing the hands
def drawcard(draw):
    draw = draw.append(random.randint(1,10))
    return draw

#fake loading to make it seem as if something is being processed
def loading():
    time.sleep(4)
    print("")

#the black jack game it self
def blackjack_game():
    loading()
#for the person who wins the game 1 for player 2 for dealer 3 for bust player 4 for bust dealer
    winner = 0

#defining the starting hands
    dealer_hand = []
    player_hand = []

    while len(player_hand)< 2 and len(dealer_hand) < 2:
        drawcard(player_hand)
        drawcard(dealer_hand)

    print(f"The dealer has a {dealer_hand[0]} showing and another card face down.\n")
    print(f"You have a {player_hand[0]} and a {player_hand[1]} for a total of {sum(player_hand)}.")

#allowing the player to hit or stand
    while True:
        if sum(player_hand) == 21:
            print("\nBlackJack!")
            break

        if sum(player_hand)>21:
            print("\nYou busted!\n")
            winner = 3
            break

        hit_stand = (input("\nWould you like to hit or stand (H for hit S to stand): ")).upper()

        if hit_stand in ["H","HIT"]:
            drawcard(player_hand)
            print(f"\nYou hit a {str(player_hand)[-3:-1]}\n")
            print(f"Your cards are now {str(player_hand)[1:-1]} for a total of {sum(player_hand)}")

        elif hit_stand in ["S","STAND"]:
            print(f"\nYou stand at {sum(player_hand)}")
            break

        else:
            print("\nNot a valid input please try again.")

#dealers turn
    if sum(player_hand) <= 21:
        loading()
        print(f"The dealer flips their facedown card it's a {str(dealer_hand)[-3:-1]}.\n")
        print(f"The dealers cards are {str(dealer_hand)[1:-1]} for a total of {sum(dealer_hand)}")
        loading()

        while winner == 0:
            if 21 < sum(dealer_hand):
                print("The dealers busts.\n")
                winner = 4

            elif sum(dealer_hand) <= 16:
                drawcard(dealer_hand)
                print(f"The dealer hits! It's a {str(dealer_hand)[-3:-1]}.\n")
                print(f"The dealers cards are {str(dealer_hand)[1:-1]} for a total of {sum(dealer_hand)}.")
                loading()

            elif sum(dealer_hand) >= sum(player_hand):
                winner = 2

            elif sum(player_hand) > sum(dealer_hand):
                winner = 1

#finding the winner of the game
    if winner == 1:
        print(f"Your total is {sum(player_hand)} and the dealers is {sum(dealer_hand)}.\n")
        print("congratulations you win!\n")

    elif winner == 2:
        if sum(dealer_hand) == sum(player_hand):
            print(f"You tied at {sum(dealer_hand)} but dealer wins ties.\n")

        else:
            print(f"The dealers total is {sum(dealer_hand)} and yours is {sum(player_hand)}.\n")
        print("The dealer wins. Better luck next time.\n")

    elif winner == 3:
        print("The dealer wins. Better luck next time.\n")

    elif winner == 4:
        print("congratulations you win!\n")

#function for if the player wants to continue to play or not also a giant loop everything happens in
def keep_playing():
    while True:
        gameplay = input("Would you like to play a game of Black Jack?\n\n(Y for Yes N for No): ")
        gameplay = gameplay.upper()

        if gameplay in ["Y","YES"]:
            blackjack_game()
            continue

        if gameplay in ["N", "NO"]:
            print("\nGoodbye")
            sys.exit()

        else:
            print("\nNot a valid input please try again.\n")

if __name__ == "__main__":
    keep_playing()
