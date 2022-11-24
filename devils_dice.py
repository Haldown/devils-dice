'''
Devils Dice
By Adam Muenz
Last Updated 11/23/2022
'''
import random

# Globals
starting_gold = 10
high_score = 0

# Function to play game
def play_game(): 
    global high_score
    while True:
        current_gold = starting_gold
        print("Lets play Devils Dice!")
        print("1) Rules")
        print("2) Play Game")
        print("3) No thanks")
        choice = input("Choose an option: ").lower()
        if choice == "1" or choice == "rules":
            print("-"*20 + "\n")
            print("Here are the rules for Devils Dice!")
            print("You place a bet up to your current gold total.\nThen you roll one dice and the house rolls three dice.\nIf your dice matches ONE of the house\'s dice you get your bet back plus an equal amount.\nIf your dice matches TWO of the house\'s dice you get your bet back plus double.\nIf your dice matches THREE of the house\'s dice you get your bet back plus tripple.\nBUT if you don\'t match any dice you lose your bet.")
            print("If you run out of money you lose the game.")
            print("Good luck!\n")
        if choice == "2" or choice == "play game" or choice == "play":
            while True:
                print("-"*20)
                print(f'The high score is {high_score} gold.')
                print(f'You have {current_gold} gold.')
                bet = input("What is your bet? ")
                if bet == "0" or int(bet) > current_gold:
                    print(f'Please place a bet between 1 and {current_gold}')
                else:
                    current_gold -= int(bet)
                    player_dice = random.randint(1, 6)
                    house_dice_1 = random.randint(1, 6)
                    house_dice_2 = random.randint(1, 6)
                    house_dice_3 = random.randint(1, 6)
                    print("-"*20)
                    print("You rolled", player_dice)
                    print("The house rolled", house_dice_1, house_dice_2, house_dice_3)
                    print("-"*20)
                    if player_dice == house_dice_1 and player_dice == house_dice_2 and player_dice == house_dice_3:
                        print("You matched 3 of the house\'s dice!")
                        current_gold += int(bet) * 4
                    elif (player_dice == house_dice_1 and player_dice == house_dice_2) or (player_dice == house_dice_1 and player_dice == house_dice_3) or (player_dice == house_dice_2 and player_dice == house_dice_3):
                        print("You matched 2 of the house\'s dice!")
                        current_gold += int(bet) * 3
                    elif player_dice == house_dice_1 or player_dice == house_dice_2 or player_dice == house_dice_3:
                        print("You matched 1 of the house\'s dice!")
                        current_gold += int(bet) * 2
                    else:
                        print("Oh no! You didn\'t match any dice!")
                    print(f'You now have {current_gold} gold')
                    if current_gold > high_score:
                        high_score = current_gold
                        print(f'{high_score} is a new high score!')
                    print("-"*20)
                    if current_gold == 0:
                        print("Game Over")
                        break
        if choice == "3" or choice == "no thanks" or choice == "no":
            print("Goodbye!")
            quit()

play_game()