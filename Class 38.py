class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        
  
    def speak(self):
        print(self.name, self.name)
  
    def display_details(self):
        types_str = ', '.join(self.types)  # convert list to string
        print('Entry Number: ' + str(self.entry))
        print('Name: ' + self.name)
        print('Type: ' + self.types)
        print('Description: ' + self.description)
        print(self.is_caught)
        if self.is_caught:
            print(self.name + " has already been caught!")
        else:
            print(self.name + " has not been caught")


Pokédex_1 = Pokemon(1,"Bulbasaur", 'Grass and Posion', "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", True)
Pokédex_2 = Pokemon(11,"Metapod", 'Bug', "It is waiting for the moment to evolve. At this stage, it can only harden, so it remains motionless to avoid attack.", True)
Pokédex_3 = Pokemon(24,"Arbok", 'Posion', "The pattern on its belly appears to be a frightening face. Weak foes will flee just at the sight of the pattern.", False)


Pokédex_1.speak()

Pokédex_2.speak()

Pokédex_3.speak()


Pokédex_1.display_details()

Pokédex_2.display_details()

Pokédex_3.display_details()
