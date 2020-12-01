from lib import make_menu
import random
import users

move_dict = {'Grass': 'Giga Drain', 'Fire': 'Flamethrower', 'Water': 'Surf', 'Bug': 'Bug Bite',
        'Flying': 'Wing Attack',
        'Normal': 'Headbutt', 'Poison': 'Poison Jab', 'Electric': 'Thunderbolt', 'Ground': 'Earthquake',
        'Psychic': 'Psycho Cut', 'Fighting': 'Karate Chop', 'Rock': 'Rockslide', 'Ice': 'Ice Beam',
        'Ghost': 'Shadow Ball',
        'Dragon': 'Draco Meteor'}

def battling(user1, user2):
    """ Allows two users to play a battle minigame together.
    Winner is determined by several factors, including CP, level, and type. 
    Parameters: user1 and user2 (named tuples containing data about a user's pokemon, number of candies, etc.).
    Returns: True if user1 won, else False.
    """
    
    # Will determine which pokemon is faster and assign it "user1"
    pokemon1 = user1.pokemon_list[user1.active_pokemon_idx]
    pokemon2 = user2.pokemon_list[user2.active_pokemon_idx]
    if pokemon1.CP > pokemon2.CP:
        swap = False
        # We need to do nothing because user1 is already faster
    elif pokemon2.CP > pokemon1.CP:
        user1, user2 = user2, user1
        pokemon1, pokemon2 = pokemon2, pokemon1
        swap = True
        # Swaps the users so that user2 goes first
    else:
        coin_toss = random.randint(1, 2)
        # If both pokemon have the same CP, then we just randomize which one goes first 
        if coin_toss == 1:
            swap = False
        else:
            user1, user2 = user2, user1
            pokemon1, pokemon2 = pokemon2, pokemon1
            swap = True

    pokemon1_type = pokemon1.type
    user1_cp = pokemon1.CP

    pokemon2_type = pokemon2.type
    user2_cp = pokemon2.CP
    # removes the data inside the tuples to format the battle

    winner = 0 #so that the while function 
    # variable will change depending on who is the winner of the battle

    print(user1.name + '\'s pokemon is {}'.format(pokemon1.name))
    print(user2.name + '\'s pokemon is {}'.format(pokemon2.name))

    battle_advantage = type_advantage_calc(pokemon1_type, pokemon2_type)
    type_move1 = move_dict[pokemon1_type]
    type_move2 = move_dict[pokemon2_type]

    user1_health = 3 * user1_cp
    user2_health = 3 * user2_cp
    # equation to define the health that each pokemon gets based on their CP's


    while winner == 0:
        # displays possible moves depending on the user's active/current pokemon
        print()
        user1_move = make_menu('What move will you use, {}?'.format(user1.name), [
            type_move1,
            'Tackle',
            'Block'
        ])
        print('\n' * 50) #So that the slower user cannot see what user1's move while picking
        #This gives the block move a use.
        user2_move = make_menu('What move will you use, {}?'.format(user2.name), [
            type_move2,
            'Tackle',
            'Block'
        ])
          # Uses the make_menu function to create a menu to take user inputs from for choosing a move

        if user1_move == 0 and user2_move != 2:
            user2_health -= battle_advantage[0] * (user1_cp / user2_cp) * 100
            user2_health = int(user2_health)
            # uses the values found in the battle_advantage function to calculate how much damage the type_specific move should do
        elif user1_move == 1 and user2_move != 2:
            user2_health -= 100
            user2_health = int(user2_health)
            # Would be equal to if type advantage was 1 and CPs were equal
        if user2_move == 0 and user1_move != 2 and user2_health >= 0:
            user1_health -= battle_advantage[1] * (user2_cp / user1_cp) * 100
            user1_health = int(user1_health)
        elif user2_move == 1 and user1_move != 2 and user2_health >= 0:
            user1_health -= 100 
            user1_health = int(user1_health)
             # Would be equal to a type move if the type advantage was 1 and CPs were equal


        action_printer(user1, user2, battle_advantage[0], battle_advantage[1], user1_move, user2_move, user1_health, user2_health)
        # Determines if there is a winner based off of health
        if user1_health <= 0:
            # User 2 won
            print()
            # The candies are updated in the caller function
            # which should be main.main_menu
            print('Player', user2.name, 'is the winner!\n', user2.name, 'has won 10 candies as a prize!')
            
            # We need to return if the original user1 is now the winner (user2),
            # which is exactly whether we swapped.
            return swap
        elif user2_health <= 0:
            # User 1 won
            print()
            # The candies are updated in the caller function
            # which should be main.main_menu
            print('Player', user1.name, 'is the winner!\n', user1.name, 'has won 10 candies as a prize!')
            
            # We need to return if the original user1 is now the winner (user1),
            # which is exactly whether we didn't swap.
            return not swap

def action_printer(user1, user2, type_advantage1, type_advantage2, user1_move, user2_move, user1_health, user2_health):
    """Reads through the moves each player selects and determines the order things will be printed out depending on pokemon the user will user
    Parameters: user1 and user2.
    Returns: winner,as to be used by battling function. """

    pokemon1 = user1.pokemon_list[user1.active_pokemon_idx]
    pokemon1_type = pokemon1.type
    pokemon1_name = pokemon1.name
    type_move1 = move_dict[pokemon1_type]

    pokemon2 = user2.pokemon_list[user2.active_pokemon_idx]
    pokemon2_type = pokemon2.type
    pokemon2_name = pokemon2.name
    type_move2 = move_dict[pokemon2_type]
    # removes the data inside the tuples to format the battle
        
    #Prints the "story" of the battle.
    if user1_move == 0:
        print(pokemon1_name + " used " + type_move1 + "!")
        if type_advantage1 == 0.5:
            print("It's not very effective...")
        elif type_advantage1 == 2:
            print("It's super effective!")
    elif user1_move == 1:
        print(pokemon1_name, "used Tackle!")
    elif user1_move == 2:
        print(pokemon1_name, "used Block!")
    else:
        ("An error occurred.")
    
    # then user2 (the slower pokemon) goes
    if user2_move == 0 and user2_health > 0:
        print(pokemon2_name + " used " + type_move2 + "!")
        if type_advantage2 == 0.5:
            print("It's not very effective...")
        elif type_advantage2 == 2:
            print("It's super effective!")
    elif user2_move == 1 and user2_health > 0:
        print(pokemon2_name, "used Tackle!")
    elif user2_move == 2 and user2_health > 0:
        print(pokemon2_name, "used Block!")
    else:
        print("An error occurred.")
    
        #Prints each pokemons resulting health
    if user1_move == 2 or user2_move == 2:
        # Both healths stay the same
        print()
        print(pokemon1_name + "'s health remains at " + str(user1_health))
        print(pokemon2_name + "'s health remains at " + str(user2_health))
        winner = 0
    else:
        print()
        if user1_health > 0 and user2_health > 0:
            print(pokemon1_name + "'s health is now " + str(user1_health))
            print(pokemon2_name + "'s health is now " + str(user2_health))
            winner = 0
        elif user1_health <= 0 and user2_health > 0:
            print(pokemon1_name + "'s health is now 0")
            print(pokemon2_name + "'s health is now " + str(user2_health))
            winner = 2
        elif user2_health <=0 and user1_health > 0:
            print(pokemon1_name + "'s health is now " + str(user1_health))
            print(pokemon2_name + "'s health is now 0")
            winner = 1

    return winner

#Hard codes the type advantages
strong = {'Grass': ['Water', 'Rock', 'Ground'], 'Water': ['Fire', 'Rock', 'Ground'],
            'Fire': ['Grass', 'Ice', 'Bug'], 'Rock': ['Fire', 'Ice', 'Bug', 'Flying'],
            'Flying': ['Grass', 'Bug', 'Fighting'], 'Bug': ['Grass', 'Psychic'],
            'ground': ['Fire', 'Rock', 'Poison', 'Electric'], 'Poison': ['Grass'], 'Normal': [],
            'Ghost': ['Psychic', 'Ghost'], 'Psychic': ['Fighting', 'Poison'], 'Fighting': ['Normal', 'Ice', 'Rock'],
            'Electric': ['Water', 'Flying'], 'Dragon': ['Dragon'], 'Ice': ['Grass', 'Ground', 'Flying', 'Dragon']}
# dictionary holds type advantages, meaning key will do double damage to any types in its value list

weak = {'Grass': ['Bug', 'Fire', 'Flying', 'Grass', 'Poison', 'Dragon'], 'Water': ['Grass', 'Dragon', 'Water'],
        'Fire': ['Water', 'Rock', 'Fire', 'Dragon'], 'Rock': ['Fighting', 'Ground'], 'Flying': ['Electric', 'Rock'],
        'Bug': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost'], 'Ground': ['Grass', 'Bug', 'Flying'],
        'Poison': ['Rock', 'Ground', 'Poison', 'Ghost'], 'Normal': ['Rock', 'Ghost'], 'Ghost': ['Normal'],
        'Psychic': ['Psychic'], 'Fighting': ['Psychic', 'Flying', 'Poison', 'Bug', 'Ghost'],
        'Electric': ['Grass', 'Ground', 'Electric', 'Dragon'], 'Dragon': [], 'Ice': ['Fire', 'Water', 'Ice']}
# inverse relationship between key and value here; key does 1/2 damage to any pokemon with a type in its value

def type_advantage_calc(pokemon1_type, pokemon2_type):
    """ Takes the types of the two pokemon that will be battling as parameters and determines the type advantage
    (aka damage multiplier) based on their respective types in order to calculate the effectiveness of type-specific
    moves like Surf. Returns each of the pokemon's type effectiveness as a tuple of floats. """

    if pokemon2_type in strong[pokemon1_type]:
        pokemon1_advantage = 2
    elif pokemon2_type in weak[pokemon1_type]:
        pokemon1_advantage = 0.5
    else:
        pokemon1_advantage = 1
    # statements define the multiplier for pokemon1 based on the defined dictionaries for its type
    if pokemon1_type in strong[pokemon2_type]:
        pokemon2_advantage = 2
    elif pokemon1_type in weak[pokemon2_type]:
        pokemon2_advantage = 0.5
    else:
        pokemon2_advantage = 1

    return pokemon1_advantage, pokemon2_advantage
    # values can be either 0.5, 1, or 2
