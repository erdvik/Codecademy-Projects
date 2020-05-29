class Trainer():
    def __init__(self, name, starter_pokemon, potions=2):
        self.name = name
        self.starter_pokemon = starter_pokemon
        self.pokemons = [starter_pokemon]
        self.potions = potions
        self.currently_acctive_pokemon = self.pokemons[0]

    """
    methods:
    - switch currently acctive pokemon
    """
    def use_potion(self):
        pokemon = self.currently_acctive_pokemon
        potion_regain_amount = pokemon.level / 2
        print('{name} used a potion on {pokemon}!'.format(name=self.name, pokemon=pokemon.name))
        self.currently_acctive_pokemon.regain_health(potion_regain_amount)
    
    def attack_trainer(self, trainer):
        self_pokemon = self.currently_acctive_pokemon
        enemy_pokemon = trainer.currently_acctive_pokemon
        print('{name} started an attack on {trainer}!'. format(name=self.name, trainer=trainer.name))
        self_pokemon.attack(enemy_pokemon)

    def switch_pokemon(self):
        print('Avalible Pokemons:')
        for pokemon in pokemons:
            print(pokemon.name)
        name = input('Which pokemon do you want to switch to?')
        for i in range(pokemons.len()):
            if pokemons[i.name] == name:
                old_pokemon = self.currently_acctive_pokemon
                new_pokemon = pokemons[i]
                self.currently_acctive_pokemon = new_pokemon
                print('{trainer} switched pokemon from {old} to {new}'.format(trainer=self.name, old=old_pokemon, new=new_pokemon))
            else:
                print("Could not find pokemon in list")


                
        

        