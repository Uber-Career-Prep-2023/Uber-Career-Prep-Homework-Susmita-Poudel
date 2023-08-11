#Question 9: AdoptAPet
#An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home.
# Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal; 
#they are assigned the animal of that species that has been in the shelter longest. If there are no animals available of 
#the desired species, they must take the other species. You are given a list of pets in the shelter with their names, 
#species, and time in the shelter at the start of a week. You receive a sequence of incoming people (to adopt pets) and animals
# (new additions to the shelter) one at a time. Print the names and species of the pets as they are adopted out.

#Time-complexity: 0(n)    Space-complexity: 0(m), m = no. of pets
from collections import deque

class AnimalShelter:
    def __init__(self):
        self.cats = deque()
        self.dogs = deque()

    def add_pet(self, name, species, time):
        if species == "cat":
            self.cats.append((name, time))
        else:
            self.dogs.append((name, time))

    def adopt_pet(self, person_name, species):
        if species == "cat" and self.cats:
            adopted_name, _ = self.cats.popleft()
            return adopted_name, "cat"
        elif species == "dog" and self.dogs:
            adopted_name, _ = self.dogs.popleft()
            return adopted_name, "dog"
        elif self.cats:
            adopted_name, _ = self.cats.popleft()
            return adopted_name, "cat"
        elif self.dogs:
            adopted_name, _ = self.dogs.popleft()
            return adopted_name, "dog"
        else:
            return None, None

# Example usage:
shelter = AnimalShelter()

# Initial pets
shelter.add_pet("Sadie", "dog", 4)
shelter.add_pet("Woof", "cat", 7)
shelter.add_pet("Chirpy", "dog", 2)
shelter.add_pet("Lola", "dog", 1)

# Adopters and new pets
actions = [
    ("Bob", "person", "dog"),
    ("Floofy", "cat"),
    ("Sally", "person", "cat"),
    ("Ji", "person", "cat"),
    ("Ali", "person", "cat")
]

for action in actions:
    #person gets a pet
    if action[1] == "person":
        adopted_name, adopted_species = shelter.adopt_pet(action[0], action[2])
        if adopted_name:
            print(f"Output: {adopted_name}, {adopted_species}")
    #pets get added to queue
    else:

        shelter.add_pet(action[0], action[1], 0)
        print("Output:")
