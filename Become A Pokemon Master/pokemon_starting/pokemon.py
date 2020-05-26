class Pokemon():
    def __init__(self, name, p_type, level=1):
        self.name = name
        self.p_type = p_type
        self.level = level
        self.max_health = update_max_health()
        self.current_health = max_health
        self.knocked_out = False
    
    def update_max_health(self):
        self.max_health = 97 + (self.level * 3) #formula for calculating max health

    def lose_health(self, amount_lost):
        new_health = self.current_health - amount_lost
        if new_health <= 0:
            self.current_health = 0
            knock_out()
            print('{name} lost all their health and is knocked out!'.format(name=self.name))
        else:
            self.current_health = new_health
            print('{name} now has {health} health'.format(name=self.name, health=self.current_health))
    
    def regain_health(self, amount_regained):
        if not self.knocked_out:
            new_health = self.current_health + amount_regained
            if new_health > self.max_health:
                self.current_health = self.max_health
            else:
                self.current_health = new_health
            print('{name} health is regained to {health}'.format(name=self.name, healht=self.current_health))

        else:
            print('{name} is knocked out and need to be revived to access health regain'.format(name=self.name))

    def revive_pokemon(self):
        self.knocked_out = False
        print('{name} has been revived!'.format(name=self.name))

    def knock_out(self):
        self.knocked_out = True
    
    def attack(self, pokemon):
        pass