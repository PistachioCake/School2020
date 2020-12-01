import csv
import pokemon
from lib import make_menu, Pokemon, User
# lib.Pokemon used in the eval in load_file

FILE_NAME = 'users.csv'

def update_user(user, *, id=None, name=None, pokemon_list=None, active_pokemon_idx=None, candies=None):
    """Updates a user with the attributes in this function since tuples are not mutable.
       Parameters: User, optional and name only: name, pokemon_list, active_pokemon_idx, candies
       Returns: User with updated stats"""
    return User(
        user.id                 if id                 is None else id,
        user.name               if name               is None else name,
        user.pokemon_list       if pokemon_list       is None else pokemon_list,
        user.active_pokemon_idx if active_pokemon_idx is None else active_pokemon_idx,
        user.candies            if candies            is None else candies
    )

def add_pokemon(user, new_pokemon):
    """Adds pokemon to user's pokemon.
       Parameters: user and the pokemon to be added
       Returns: user """
    if len(user.pokemon_list) < 12:
        user.pokemon_list.append(new_pokemon)
        print("Congratulations! {} has joined the party!".format(new_pokemon.name))
    else:
        # We need to drop a pokemon to not exceed 12 pokemon
        selection = make_menu(
            "You can only have 12 pokemon in your party at a time. Which pokemon would you like to remove?", 
            [pokemon.name for pokemon in user.pokemon_list] + [new_pokemon.name],
        )
        if selection == 12:
            # The new pokemon
            print("You let {} go.".format(new_pokemon.name))
        else:
            # One of the old pokemon
            removed = user.pokemon_list.pop(selection)
            print("You let {} go.".format(removed.name))
            user.pokemon_list.append(new_pokemon)
            print("Congratulations! {} has joined the party!".format(new_pokemon.name))
    return user
    
def level_up_pokemon_of(user):  # needs the user #, the pokemon, its Cp and its level, their # of candies,
    """Levels up user's active pokemon with player input (i.e. if the player can and wants to)
       Parameters: user
       Returns: user with levelled up pokemon, or same user"""

    pokemon_list = user.pokemon_list
    active_pokemon = pokemon_list[user.active_pokemon_idx]

    leveled_up, candies_reqd = pokemon.level_up(active_pokemon)

    if candies_reqd == 0:
        # pokemon is lvl 40 or higher or something went wrong
        print('You cannot level up this pokemon.')
        return user
    if candies_reqd > user.candies:
        print('You do not have enough candies to level up this pokemon. Try battling or\n'
              'catching more pokemon to get more candies.')
        return user
     
    # Get user input
    print('Would you like to level up {} to level {}?'.format(active_pokemon.name, leveled_up.level))
    if candies_reqd == 1:
        # singular candy
        print('It requires {} candy. [y/n]'.format(candies_reqd))
    else:
        # multiple candies
        print('It requires {} candies. [y/n]'.format(candies_reqd))

    choice = input('\t> ')

    while choice[0].lower() not in 'yn':
        # repeat until choice is valid
        print('Please enter \'y\' or \'n\'.')
        choice = input('\t> ')

    if choice[0].lower() == 'y':
        # user wants to level up pokemon
        # remove candies
        user = update_user(user,
            candies = user.candies - candies_reqd
        )
        # update pokemon_list
        user.pokemon_list[user.active_pokemon_idx] = leveled_up
        print('Your {} is now level {}, and has a CP of {}'.format(
            leveled_up.name, leveled_up.level, int(leveled_up.CP)))
        # if the user doesn't want to level up the pokemon, we do nothing
        
    return user

def load_file():
    """Loads a list of users from file
       Parameters: None
       Returns: list of users"""
    try:
        datFile = open(FILE_NAME, 'r')
    except FileNotFoundError:
        # No file to read, so no users to read
        return []
    reader = csv.reader(datFile)
    user_list = []
    for line in reader:
        # Extract user information from line
        user_id = int(line[0])
        user_name = line[1]
        # FIXME: THIS IS TERRIBLE
        # but it does work...
        pokemons = eval(line[2])
        active_pokemon_idx = int(line[3])
        candies = int(line[4])

        user = User(user_id, user_name, pokemons, active_pokemon_idx, candies)
        user_list.append(user)

    datFile.close()
    return user_list

def save_file(user_list):
    """ Saves user_list to file
        Parameters: list of users
        Returns: None """
    datFile = open(FILE_NAME, 'w', newline='')
    writer = csv.writer(datFile)
    writer.writerows(user_list)
    datFile.close()

def create_user(user_name, pokemons=None, user_list=None):
    """ Creates and saves a user.
        Parameters: name user
                    pokemons
                    user_list
        Returns: user """
    if user_list is None:
        user_list = load_file()
    if pokemons is None:
        pokemons = []
        active_pokemon_idx = None
    else:
        active_pokemon_idx = 0
    # get user_id: the highest currently used user_id plus one
    # Not the best way to do it, but it'll work.
    # Actually now that I think about it user_ids are kinda superfluous...
    user_id = max([user[0] for user in user_list], default=0) + 1
    user = User(user_id, user_name, pokemons, active_pokemon_idx, 0)
    user_list.append(user)
    return user


def get_player_user_idx(user_list=None, to_pick="a user"):
    """ Allows player to choose their user and chose which user to battle.
        Parameters: user_list,
                    to_pick (a string describing what to pick, default "a user")
        Returns: the *index of* the user the player selected or None"""
    if user_list is None:
        user_list = load_file()
    if not user_list:
        print("There are no users saved. Please create a new one.")
        return None
    # To avoid overwhelming the user, we'll split it up into smaller chunks
    # if there are more than 25 options.
    if len(user_list) > 25:
        offset = 0
        while user_list:
            choices = [user.name for user in user_list[:23]]
            choices.append("Exit selection")
            choices.append("Next page")
            selection = make_menu("Pick {}:".format(to_pick), choices)
            if selection == len(choices) - 1: # Note: choices may not have 25 elements, so == 24 would be wrong
                # Next Page
                user_list = user_list[23:]
                offset += 23
                continue
            elif selection == len(choices) - 2:
                # Exit selection
                return None
            else:
                return offset + selection
        # If they exit the while loop, meaning they exhausted all users,
        print("That's all the users saved. Exiting user selection.")
        return None
    else:
        # There are 25 or fewer users, so we just give them all at once
        choices = [user.name for user in user_list]
        choices.append("Exit selection")
        selection = make_menu("Pick {}:".format(to_pick), choices)
        if selection == len(choices) - 1:
            # Exit selection
            return None
        else:
            return selection
        
