import string


# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Mike Gotta                            |
# Last Modified: October 29, 2019       |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class Pokemon:
    def __init__(self, name, number, combat_points, pokemon_type):      # creating a pokemon class with these variables
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.pokemon_type = pokemon_type

    def get_name(self):
        return self.name        # creating four "getter" functions

    def get_number(self):
        return self.number

    def get_combat_points(self):
        return self.combat_points

    def get_pokemon_type(self):
        return self.pokemon_type
                                               # using the string function to print the information
    def __str__(self):
        return "Number: " + str(self.number) + ", Name: " + self.name + ", CP: " + str(self.combat_points) + ", Type: " + " and ".join(self.pokemon_type)

def lookup_by_name(pokedex, name):
    for pokemon in pokedex:
        if pokemon.get_name() == name:
            print(pokemon)
            return
    print("there is no pokemon named " + name)

def lookup_by_number(pokedex, number):
    for pokemon in pokedex:
        if pokemon.get_number() == number:
            print(pokemon)
            return
    print("There is no pokemon numbered " + str(number))


def total_by_type(pokedex, pokemon_type):
    total = 0
    for pokemon in pokedex:
        if pokemon_type in pokemon.get_pokemon_type():
            total += 1
    print("Number of pokemon that contain type " + pokemon_type + " = " + str(total))

def average_hit_points(pokedex):
    average = 0
    for pokemon in pokedex:
        average += pokemon.get_combat_points()
    print("Average Pokemon combat points = {0:.2f}".format(average/len(pokedex)))


def print_pokedex(pokedex):
     for pokemon in pokedex:
         print(pokemon)

def print_menu():
    print()
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")
    print()


# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])  # number
        name = pokelist[1]  # name
        combat_points = int(pokelist[2])  # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]  # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex


# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer


# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()


# ---------------------------------------

main()