from random import choice, randrange
from csv import reader
from lib import make_menu, Pokemon
from math import sqrt
import users

def update_pokemon(pokemon, *, name=None, CP=None, level=None):
    """Updates a pokemon with the attributes in this function since tuples are not mutable.
       Parameters: Pokemon, optional and name only: name, CP, level
       Returns: Pokemon with updated stats"""

    return Pokemon(
        pokemon.name  if name  is None else name,
        pokemon.type, # Note: type cannot change
        pokemon.CP    if CP    is None else CP,
        pokemon.level if level is None else level,
    )

def choose_starter():
    """ User can choose squirtle, charmander or bulbasaur.
        Parameters: None
        Returns: Starter Pokemon """
    # This function will be called when a new user is created
    selection = make_menu("Choose your starter pokemon!", [
            "Bulbasaur:  Grass Type",
            "Squirtle:   Water Type",
            "Charmander: Fire Type",
    ])

    if selection == 0:
        return Pokemon('Bulbasaur', 'Grass', 200, 1)
    elif selection == 1:
        return Pokemon('Squirtle', 'Water', 200, 1)
    elif selection == 2:
        return Pokemon('Charmander', 'Fire', 200, 1)
    
def current_pokemon_menu(user):
    """ Shows the pokemon menu and allows user to update their current pokemon
    goes back to menu to choose actions. """

    # Note: from the assignment:
    # "The Pokemon selection menu must show multiple options per row"
    
    # PRINT POKEMON MENU

    # No pokemon has name longer than 10 characters, so we will use 16 character blocks
    name_format_string = "[{:2d}] {:<10s}"
    info_format_string = " lvl: {:<2d} CP: {:3d}"

    print("Pokemon Selection Menu:")

    # Generate all name and info strings for each pokemon
    name_strings = []
    info_strings = []
    for i, pokemon in enumerate(user.pokemon_list):
        name_strings.append(name_format_string.format(i + 1, pokemon.name))
        info_strings.append(info_format_string.format(pokemon.level, int(pokemon.CP)))
    
    # Print name and info strings in chunks of 4
    while name_strings:
        # Note: slices that exceed the length of the list do *not*
        # throw errors. 
        print('  '.join(name_strings[:4]))
        print(' '.join(info_strings[:4]))
        name_strings = name_strings[4:]
        info_strings = info_strings[4:]

    # Print other info about the user
    print('The active pokemon is currently {}, #{}.'.format(
        user.pokemon_list[user.active_pokemon_idx].name,
        user.active_pokemon_idx + 1, # remember that thing about 1-indexing?
    ))
    print()
    print("You have {} candies.".format(user.candies))
    print()
    
    # GET USER ACTION
    
    while True:
        selection = make_menu("Would you like to do anything?", [
                "Change active Pokemon",
                "Level up active Pokemon",
                "Exit",
        ])
        if selection == 0:
            # Change active Pokemon
            try:
                new_active = int(input("What number do you want to make the new active Pokemon? ")) - 1
            except ValueError:
                # Unable to cast to int
                print("Not a valid number.")
                continue

            if 0 <= new_active < len(user.pokemon_list):
                user = users.update_user(user, active_pokemon_idx=new_active)
                print("The new active pokemon is", user.pokemon_list[user.active_pokemon_idx].name)
            else:
                # Outside of valid range
                print("Not a valid number.")
        elif selection == 1:
            # Level up active Pokemon
            user = users.level_up_pokemon_of(user)
        else:
            # Exit
            return user
            
def level_up(pokemon):
    """ Determines the new level of the pokemon and candies required to do so.
    Arguments: pokemon
    Returns: pokemon with updated level and CP, number of candies required """
    # Code here determines the new level of the pokemon and the candies required to do so
    # Keep in mind that levels 30-39 need 2 candies to level up
    
    if pokemon.level < 30:
        pokemon = update_pokemon(pokemon,
            CP = pokemon.CP + (pokemon.CP * 0.0094) / (0.095 * sqrt(pokemon.level)),
            level = pokemon.level + 1,
        )
        return pokemon, 1
    elif pokemon.level < 40:
        pokemon = update_pokemon(pokemon,
            CP = pokemon.CP + (pokemon.CP * 0.0045) / (0.095 * sqrt(pokemon.level)),
            level = pokemon.level + 1,
        )
        return pokemon, 2
    else:
        return pokemon, 0
    
def catch_new_pokemon(user):
    """ catches a pokemon if mini-game won and adds it to a bank of pokemon the user can select
    awards candy to the user if won
    switches to other user
    pops up menu for new user to pick an action. """
    if not minigame():
        return user
    else:
        # GET NEW POKEMON
    
        # Gets the pokemon names from the csv and puts them in a list
        pokemon_choices = []
        with open('pokemon_list.csv', 'r', newline = '') as mons_file:
            csv_reader = reader(mons_file)
            for row in csv_reader:  #index essentially means "row"
                pokemon_choices.append(row)
    
        # Pick a random pokemon from the list and instantiate it
        random_pokemon = choice(pokemon_choices)
        idx, name, min_cp, max_cp, type = random_pokemon
        min_cp, max_cp = int(min_cp), int(max_cp)
        
        cp = randrange(min_cp, max_cp)
    
        pokemon = Pokemon(name, type, cp, 1)
        
        # Level up the pokemon to a random level between 1 and 10
        level_ups = randrange(10)
        for _ in range(level_ups):
            # We don't care about candies required
            pokemon, _ = level_up(pokemon)
    
        print("You caught a {}!".format(pokemon.name))
        print("It has a level of {} and a CP of {}.".format(pokemon.level, int(pokemon.CP)))
        print("Be sure to take good care of it!")

        # Randomly give the user some amount of candies
        candies_earned = choice([1, 1, 1, 3, 3, 3, 5, 5, 7, 10])
        user = users.update_user(user,
            candies = user.candies + candies_earned
        )
        print("You now have {} candies!".format(user.candies))
    
        print()
    
    user = users.add_pokemon(user, pokemon)
    return user

def minigame():
    """Creates a minigame for the user to play. Gives the user candies and a new pokemon if they win.
        Parameters: None
        Returns: True or False depending on if the user won or lost."""
    words = ['pokemon', 'python', 'misty', 'brock', 'ash', 'function', 'matplotlib', 'spears',
            'engineering','aggies', 'alakazam', 'cadet', 'snorlax', 'gengar', 'mew',
            'coding', 'pikachu', 'monster', 'frodo', 'sbisa', 'aggieland', 'bonfire',
            'reveille', 'passback', 'whoop', 'sully', 'magikarp', 'northgate', 'tradition',
            'howdy', 'hullabaloo', 'muster', 'wildcat', 'rapidash', 'zachry', 'code', 'masterball', 
            ]
    
    word = choice(words)
    won = False
    guesses = set()
    chances = 8

    while chances > 0 and not won:
        # Print out the only the letters that have been guessed
        unknown = 0
        for letter in word:
            if letter in guesses:
                print(letter, end='')
            else:
                print('*', end='')
                unknown += 1
        print()
    
        # If all letters have been guessed, 
        if unknown == 0:
            print('You won!')
            print('The words was: ', word)
            won = True
            break
    
        # Get a guess from the user
        guess = input('Guess a letter: ')
        while not (guess and guess[0].isalpha()):
            print('Please enter a letter (a-z).')
            guess = input('Guess a letter: ')
        guess = guess[0].lower()
    
        if guess in guesses:
            print('The letter {} has already been guessed.'.format(guess))
            print('Guessed letters: {}'.format(''.join(sorted(guesses))))
            continue
    
        guesses.add(guess)
        
        # Finish the guess:
        if guess not in word:
            chances -= 1
            print('The word did not contain your guess {}'.format(guess))
            print('You have {} guesses remaining.'.format(chances))
    
    # After the game has been played, they have either won or not
    if won:
        print('Congratulations! You won!')
        return True
    else:
        print('You lost :(')
        return False