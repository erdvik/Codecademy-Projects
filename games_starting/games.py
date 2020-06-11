import random
from time import sleep

def main():
    #Call your game of chance functions here
    # coinflip("Tails", 20)
    # cho_han("Odd", 10)
    #card_pick_game(10)
    roulette(00, 10)




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
             
def card_pick_game(amount):
    avalible_cards = [[j for j in range(14)] for i in range(4)] 
    global money
    if amount <= money: #game can start
        #player picks a card
        print('Player picks a card...')
        card = choose_random_card(avalible_cards)
        del avalible_cards[random.randint(0,3)][card]
        sleep(1)
        print('Player picked {0}'.format(card))
        sleep(2)
        #house picks a card
        print('House pics a card...')
        house_card = choose_random_card(avalible_cards)
        sleep(3)
        print('It was a {0}!'.format(house_card))
        sleep(1)
        if card > house_card:
            did_win(True, amount)
        elif card < house_card:
            did_win(False, amount)
        else:
            print("It was a tie! Money refunded.")
    else:
        print('Not enough money to play...')
    
def choose_random_card(avalible_cards):
    i = 0
    while i < 1000:
        deck = random.randint(0,3)
        card = random.randint(0,13)
        try:
            picked_card = avalible_cards[deck][card]
            return picked_card
        except:
            i += 1
            continue
        print("Couldnt find any avalible cards after 1000 tries")

def roulette(guess, amount):
    avalible_guesses = ["Odd", "Even", "Row", "00"] + [str(i) for i in range(36)]
    guess = str(guess)
    if guess in avalible_guesses:
        global money
        if amount <= money:
            print('Your guess is {0}'.format(guess))
            sleep(1)
            print("Rolling ball...")
            sleep(3)
            ball_landing = random.randint(0, 36)
            ball_landing = 36
            if ball_landing == 36: #36 is equal to a 00 guess
                ball_landing = "00"
            print("Ball landed on {0}".format(ball_landing))
            sleep(1)
            if (guess == "Row") and (str(ball_landing) == "0" or ball_landing == "00"):
                did_win(True, amount, 17)
            elif ball_landing == "00" and guess == "00": 
                did_win(True, amount, 35)
            elif guess == str(ball_landing):
                did_win(True, amount, 35)
            elif ball_landing % 2 == 0 and guess == "Even":
                did_win(True, amount, 1)
            elif ball_landing % 2 != 0 and guess == "Odd":
                did_win(True, amount, 1)
            else:
                did_win(False, amount)
        else:
            print("Not enough money...")
    else:
        print("Not an availible guess. Avalible guesses:")
        print(avalible_guesses)

    #TODO:
    # fix bug with 00 input  
            
            
                

            

            

        
        







if __name__ == "__main__":
    main()