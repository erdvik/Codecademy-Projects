import random
from time import sleep



def main():
    
    #Call your game of chance functions here
    money = 100
    print("Money: {money}".format(money=money))
    money += coinflip("Heads", 10, money)
    print("Money: {money}".format(money=money))
    sleep(2)
    money += cho_han("Odd", 10, money)
    print("Money: {money}".format(money=money))
    sleep(2)
    money += card_pick_game(10, money)
    print("Money: {money}".format(money=money))
    sleep(2)
    money += roulette("Row", 50, money)
    print("Money: {money}".format(money=money))

#Write your game of chance functions here
def coinflip(guess, amount, avalible_funds):
    print('Coinflip:')
    sleep(1)
    money_won_or_lost = 0
    avalible_guesses = ["Heads", "Tails"]
    if guess in avalible_guesses: 
        if amount <= avalible_funds:
            print('Your guess is {0}'.format(guess))
            sleep(1)
            print('Flipping coin...')
            sleep(2)
            num = random.randint(1,2)
            coin = ""
            if num == 1:
                coin = "Heads"
            elif num == 2:
                coin = "Tails"
            print('It was a {0}!'.format(coin))
            sleep(1)
            if guess == coin:
                money_won_or_lost = did_win(True, amount, 1)           
            else:
                money_won_or_lost = did_win(False, amount)     
        else:
            print('Not enough money to play.')
    else:
        print('Not an avalible guess. Here are the avalible guesses:')
        print(avalible_guesses)
    return money_won_or_lost

def cho_han(guess, amount, avalible_funds):
    print('Cho Han:')
    sleep(1)
    money_won_or_lost = 0
    avalible_guesses = ["Odd", "Even"]
    if guess in avalible_guesses:
        if amount <= avalible_funds:
            print('Your guess is {0}'.format(guess))
            sleep(1)
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
                    money_won_or_lost = did_win(True, amount, 1)
                else:
                    money_won_or_lost = did_win(False, amount)
            else: #odd number
                if guess == "Odd":
                    money_won_or_lost = did_win(True, amount, 1)
                else:
                    money_won_or_lost = did_win(False, amount)
    return money_won_or_lost
                  
def did_win(won, amount, multiplier=1):
    if won == True:
        money_won = amount * multiplier
        print('You won {0} dollars!'.format(money_won))
        return money_won
    elif won == False:
        print('You lost {0} dollars...'.format(amount))
        return -amount
    else:
        print('Error in did_win function')          
             
def card_pick_game(amount, avalible_funds):
    print('Card Pick:')
    sleep(1)
    money_won_or_lost = 0
    avalible_cards = [[j for j in range(14)] for i in range(4)] 
    if amount <= avalible_funds: #game can start
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
            money_won_or_lost = did_win(True, amount)
        elif card < house_card:
            money_won_or_lost = did_win(False, amount)
        else:
            print("It was a tie! Money refunded.")
    else:
        print('Not enough money to play...')
    return money_won_or_lost
    
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

def roulette(guess, amount, avalible_funds):
    print('American Roulette:')
    sleep(1)
    money_won_or_lost = 0
    avalible_guesses = ["Odd", "Even", "Row", "00"] + [str(i) for i in range(36)]
    if isinstance(guess, str):
        if guess in avalible_guesses:
            if amount <= avalible_funds:
                print('Your guess is {0}'.format(guess))
                sleep(1)
                print("Rolling ball...")
                sleep(3)
                ball_landing = random.randint(0, 36)
                if ball_landing == 36: #36 is equal to a 00 guess
                    ball_landing = 4
                print("Ball landed on {0}".format(ball_landing))
                sleep(1)
                if (guess == "Row") and (ball_landing == 0 or ball_landing == "00"):
                    money_won_or_lost = did_win(True, amount, 17)
                elif guess == str(ball_landing):
                    did_win(True, amount, 35)
                elif ball_landing != "00" and ball_landing != 0:
                    if ball_landing % 2 == 0 and guess == "Even":
                        money_won_or_lost = did_win(True, amount, 1)
                    elif ball_landing % 2 != 0 and guess == "Odd":
                        money_won_or_lost = did_win(True, amount, 1)
                    else:
                        money_won_or_lost = did_win(False, amount)
                else:
                    money_won_or_lost = did_win(False, amount)
            else:
                print("Not enough money...")
        else:
            print("Not an availible guess. Avalible guesses:")
            print(avalible_guesses)
    else:
        print("Guess needs to be of type String")
    return money_won_or_lost
     
            
            

if __name__ == "__main__":
    main()