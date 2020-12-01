from collections import namedtuple
from math import log10

# A user is represented as a namedtuple:
# User: (id: int, name: str, pokemon_list: [pokemon],
#        active_pokemon_idx: int, candies: int)

User = namedtuple('User', ['id', 'name', 'pokemon_list',
        'active_pokemon_idx', 'candies'])

# A pokemon is represented as a tuple:
# (id: int, name: str, type: str, CP: int, level: int)

Pokemon = namedtuple('Pokemon', ['name', 'type', 'CP', 'level'])

def make_menu(prompt_text, menu_options, last_is_special=None):
    """Creates and displays a menu to the player, and returns the user's selection.
    Arguments: prompt_text: the string to prompt the user.
               menu_options: a list of options as strings for the user to choose from.
               last_is_special: an optional string that the user can input to choose the 
                   last option automatically. Useful when 'quit' is an option.
    Returns: The index of the menu_option chosen.
    """
    print(prompt_text)
    # Calculate the length needed for the option box
    num_length = int(log10(len(prompt_text)))
    format_string = '[{:' + str(num_length) + 'd}] {}'

    for i, option in enumerate(menu_options):
        # Start at 1 and count up
        print(format_string.format(i+1, option))

    # Loop until valid input
    while True:
        selection = input('\t> ')
        if last_is_special is not None and selection == last_is_special:
            return len(menu_options) - 1
        try:
            selection = int(selection)
            if 1 <= selection <= len(menu_options):
                print()
                # 0-indexed lists but 1-indexed display
                return selection - 1
            else:
                # Repeat if out of bounds
                print('Please pick an integer between 1 and {}'.format(len(menu_options)))
        except ValueError:
            # Repeat if not an integer at all
            print('Please pick an integer between 1 and {}'.format(len(menu_options)))

