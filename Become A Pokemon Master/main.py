import pokemon_starting
from pokemon_starting.pokemon import Pokemon
from pokemon_starting.trainer import Trainer
import random

def fight_text():
    print('options: ')
    print('"a" to attack')
    print('"p" to use potion')
    print('"s" to switch pokemon')
    choice = input("")
    return choice

def determine_action(choice, attacker, opponent):
    if choice == 'a':
        attacker.attack_trainer(opponent)
    elif choice == 'p':
        attacker.use_potion()
    elif choice == 's':
        attacker.switch_pokemon()


while(True):
    print('Welcome to Pokemon trainer mega battle arena super fight!')
    name = input('Please choose your name:')
    starting_pokemon_type = input('Now you must choose a starter pokemon. Press "f" for fire, "w" for water, and "g" for grass:')
    pokemon_name = input('What do you want your cute little monster to be named?')
    
    if starting_pokemon_type == "f":
        pokemon1 = Pokemon(pokemon_name, "Fire")
    elif starting_pokemon_type == "w":
        pokemon1 = Pokemon(pokemon_name, "Water")
    elif starting_pokemon_type == "g":
        pokemon1 = Pokemon(pokemon_name, "Grass")
    else:
        pokemon1 = Pokemon(pokemon_name, "Fire")

    main_trainer = Trainer(name, pokemon1)

    print('Hi {name}! You will be facing other trainers and fight your way to the top of this gym!'.format(name=main_trainer.name))

    fire_pokemon = Pokemon("Joe", "fire")
    first_trainer = Trainer("Obama", fire_pokemon)

    print('Your first opponent is {name}'.format(name=first_trainer.name))
    input("Press a key when you are ready to figth")
    win = False
    while (True):
        choice = fight_text()
        determine_action(choice, main_trainer, first_trainer)

        enemy_pokemon = first_trainer.pokemons[0]
        if enemy_pokemon.knocked_out == True:
            win = True
            break

        determine_action("a", first_trainer, main_trainer)

        my_pokemon = main_trainer.pokemons[0]

        if my_pokemon.knocked_out == True:
            win = False
            break
    
    if win == True:
        print("You won!")

    else:
        print("You lost...")
    
    break

"""
More trainers, pokemons and gyms could be added
"""

    



