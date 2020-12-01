# By submitting this assignment, we agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "We have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Braeden Stewart, Grant Trusty, Collin Stafford
# Section:     219
# Assignment:  Team Project Part 2
# Date:        11 21 2020

from sys import exit

# Import project lib
import pokemon
import users
import battle
from lib import make_menu

# ---------------------------------------------------- Defining Functions ----------------------------------------------------

text_logo = """\
                                  ,'\ 
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|"""

def start_menu():
  """ Creates the opening menu for the game, including a logo.
     Parameters: None.
     Returns: None, but prints a logo and a statement. """
  print(text_logo)
  input('Press "enter" to start your Pokemon journey!')
  print()

def main_menu():
    """ Creates the main menu, to allow the player to create or load a user.
        Parameters: None
        Returns: None, but calls functions to create/load user. """
    start_menu()
    user_list = users.load_file()
    while True:
        selection = make_menu("Welcome! Pick an option.", [
            "Load user", 
            "Create user",
            "Save and Quit",
            ], last_is_special='q')
        if selection == 0:
            # Load user
            user_idx = users.get_player_user_idx(user_list)
            if user_idx is None:
                # user was not selected properly, so just display this menu again.
                continue
            player_menu(user_idx, user_list)
        elif selection == 1:
            # Create user
            name = input("What is your name? ")
            starter = pokemon.choose_starter()
            new_user = users.create_user(name, [starter], user_list)
            new_user_idx = user_list.index(new_user)
            player_menu(new_user_idx, user_list)
        else:
            # Save and quit
            print("Thank you for playing!")
            users.save_file(user_list)
            exit(0)

def player_menu(user_idx, user_list):
    """ Allows user to decide what to do with their turn. 
        Parameters: user_idx, an index of user_list
                    user_list (needed for battling functionality)
        Returns: None"""
    user = user_list[user_idx]
    while True:
        selection = make_menu("What would you like to do, {}?".format(user.name), [
            "View Pokemon",
            "Catch a new Pokemon",
            "Battle",
            "Log out",
            ], last_is_special='q')

        if selection == 0:
            # View Pokemon
            user = pokemon.current_pokemon_menu(user)
        elif selection == 1:
            # Catch a new Pokemon
            user = pokemon.catch_new_pokemon(user)
        elif selection == 2:
            # Battle
            # Get user
            opponent_idx = users.get_player_user_idx(user_list, to_pick="an opponent")
            while opponent_idx == user_idx:
                print('You cannot battle yourself, {}!'.format(user.name))
                opponent = users.get_player_user(user_list, to_pick="an opponent")
            if opponent_idx is None:
                print('No user selected, cancelling battle.')
                continue
            # Do battle
            opponent = user_list[opponent_idx]
            user_won = battle.battling(user, opponent)

            # Update winner to have 10 more candies
            if user_won:
                user = users.update_user(user, 
                    candies = user.candies + 10
                )
            else:
                # Put directly back into user_list
                user_list[opponent_idx] = users.update_user(opponent,
                    candies = opponent.candies + 10
                )

        else:
            # Save modified user back to user_list
            user_list[user_idx] = user
            return

main_menu()
