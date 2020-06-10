import random

def main():
    #Call your game of chance functions here

    coinflip("Tails", 20)
    print(money)



money = 100

#Write your game of chance functions here
avalible_guesses = ["Heads", "Tails"]
def coinflip(guess, amount):
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
                amount_won = amount * 2
                money += amount_won
                print('You won! New balance is {money}.'.format(money=money))
            else:
                money -= amount
                print('You lost.. New balance is {money}.'.format(money=money))
        else:
            print('Not enough money to play.')
    else:
        print('Not an avalible guess. Here are the avalible guesses:')
        print(avalible_guesses)



if __name__ == "__main__":
    main()