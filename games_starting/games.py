import random
from time import sleep

def main():
    #Call your game of chance functions here

    # coinflip("Tails", 20)
    # print(money)

    # cho_han("Odd", 10)

    card_pick(None, None)



money = 100

#Write your game of chance functions here
def coinflip(guess, amount):
    avalible_guesses = ["Heads", "Tails"]
    if guess in avalible_guesses: 
        global money
        if amount <= money:
            num = random.randint(1,2)
            coin = ""
            if num == 1:
                coin = "Heads"
            elif num == 2:
                coin = "Tails"
            if guess == coin:
                did_win(True, amount, 1)           
            else:
                did_win(False, amount)     
        else:
            print('Not enough money to play.')
    else:
        print('Not an avalible guess. Here are the avalible guesses:')
        print(avalible_guesses)

def cho_han(guess, amount):
    avalible_guesses = ["Odd", "Even"]
    if guess in avalible_guesses:
        global money
        if amount <= money:
            print('Rolling dices...')
            sleep(2)
            dice_roll_1 = random.randint(1, 6)
            print('First roll: {0}'.format(dice_roll_1))
            sleep(2)
            dice_roll_2 = random.randint(1, 6)
            print('Second roll: {0}'.format(dice_roll_2))
            sleep(1)
            score = dice_roll_1 + dice_roll_2
            print('Score: {0}'.format(score))
            sleep(1)
            if score % 2 == 0: #even number
                if guess == "Even":
                    did_win(True, amount, 1)
                else:
                    did_win(False, amount)
            else: #odd number
                if guess == "Odd":
                    did_win(True, amount, 1)
                else:
                    did_win(False, amount)
                
def did_win(won, amount, multiplier=1):
    global money
    if won == True:
        money += amount * multiplier
        print('You won! New balance is {money}.'.format(money=money))
    elif won == False:
        money -= amount
        print('You lost.. New balance is {money}.'.format(money=money))
    else:
        print('Error in won_or_loss function')          
             
def card_pick(card, amount):
    avalible_cards = [[j for j in range(14)] for i in range(4)]
    if card in avalible_cards:
        global money
        if amount <= money:
            #player 



            #house picks a card
            deck = random.randint(0,3)
            card = random.randint(0,13)











if __name__ == "__main__":
    main()