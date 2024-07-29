# Cassy Gates

# Set the rooms as dicts.
rooms = {
    'Drop off Location':
        dict(South='Southern Forest',
             North='Northern Forest',
             East='Eastern Ridge Line',
             West='Western Wall',
             Item='Nothing',
             Description='This area is a large opening in a forest. It is somewhat flat here.'),
    'Southern Forest':
        dict(South='Lower Southern Forest',
             North='Drop off Location',
             East='South Eastern Ridge Line',
             West='South Western Wall',
             Item='Jake',
             Description='There are sparse trees here and the slope is starting to get steep. The slope looks even'
                         ' steeper to the south.'),
    'Lower Southern Forest':
        dict(Item='Avalanche',
             Description='Avalanche'),
    'South Eastern Ridge Line':
        dict(South='Lower South Eastern Ridge Line',
             North='Eastern Ridge Line',
             West='Southern Forest',
             Item='Nothing',
             Description='You are on top of a narrow ridge line. You look to the east and see a deep ravine. The slope '
                         'to the west looks really steep'),
    'Lower South Eastern Ridge Line':
        dict(North='South Eastern Ridge Line',
             West='Lower Southern Forest',
             Item='Darby',
             Description='You are on top of a narrow ridge line. You look to the east and see a deep ravine. To the '
                         'south you see a large rocky out cropping.'),
    'Eastern Ridge Line':
        dict(South='South Eastern Ridge Line',
             West='Drop off Location',
             Item='Dan',
             Description='You are on top of a narrow ridge line. You look to the north and east and see a deep ravine.')
    ,
    'Northern Forest':
        dict(South='Drop off Location',
             West='North Western Wall',
             Item='Nothing',
             Description='You have found yourself in a thick pine forest. It looks even thicker to the north'),
    'North Western Wall':
        dict(South='Western Wall',
             East='Northern Forest',
             Item='Amber',
             Description='This is a large steep open area with a dense forest to the north and cliffs to the west.'),
    'Western Wall':
        dict(South='South Western Wall',
             North='North Western Wall',
             East='Drop off Location',
             West='Western Face',
             Item='Nothing',
             Description='You are in a large steep open area. It looks even steeper to the west.'),
    'South Western Wall':
        dict(South='Lower South Western Wall',
             North='Western Wall',
             East='Southern Forest',
             West='South Western Face',
             Item='Nothing',
             Description='This is a steep open area.'),
    'Lower South Western Wall':
        dict(North='South Western Wall',
             East='Lower Southern Forest',
             Item='Spencer',
             Description='This is a large steep open area with a large rocky out cropping to the south and cliffs to '
                         'the west.The slope looks even steeper to the east'),
    'Western Face':
        dict(Item='Avalanche',
             Description='Avalanche'),
    'South Western Face':  # Julia
        dict(North='Western Face',
             East='South Western Wall',
             Item='Julia',
             Description='You are now on a barren mountain face with cliffs to the west and south. The slope to the '
                         'north looks awfully steep.')
}

# Set variables and list the acceptable answers.
acceptable_directions = ['North', 'East', 'South', 'West']
acceptable_answers = ['y', 'n']
full_item_list = ['Amber', 'Dan', 'Darby', 'Jake', 'Julia', 'Spencer']
user_items = []
current_room = 'Drop off Location'
line = '\n-------------------------------------------------------------------------------------------------------------'


# Define the function to get the users location
def get_new_state(current_room, direction_from_user):
    current_room = rooms[current_room][direction_from_user]
    return current_room


# Define the function that shows the user where they are and what they still need to find.
def show_status():
    print(f'\nYou are in the {current_room}.\n')
    if rooms[current_room]['Item'] != 'Avalanche':
        print(rooms[current_room]['Description'])
        if rooms[current_room]['Item'] != 'Nothing' and rooms[current_room]['Item'] not in user_items:
            item_found = rooms[current_room]['Item']
            print(f'\nCongratulations, you have found {item_found}.')
            user_items.append(item_found)
            user_items.sort()
        if len(user_items) == 0:
            print('\nYou have not found anyone yet.')
        else:
            print('\nSo far you have found:')
            for item in user_items:
                print(f'*{item}')
        print('\nYou still need to find:')
        for item in full_item_list:
            if item not in user_items:
                print(f'*{item}')
        print('\nFrom here you can go:')
        for directions in rooms[current_room]:
            if directions in acceptable_directions:
                print(f'*{directions}')
    else:
        user_items.append('Avalanche')
    return user_items


# Define the function that creates the avalanche.
def avy_function(character='o'):
    for i in range(0, 10):
        print(character)
        character += character
    for i in range(10, 30):
        print(character)
    print('\nOh no you have triggered an avalanche! Game over.')
    game_answer = input('Would you like to play again? (y/n) ').strip().lower()
    while game_answer not in acceptable_answers:
        game_answer = input('Invalid entry. Would you like to play again? (y/n) ').strip().lower()
    else:
        return game_answer


# Get username.
user_name = input('Enter name: ')
print(line)

# Introductions.
print(f'\nHello {user_name}.\n\nIn this game your character is a skilled search and rescue ski patrol.\nYou work in '
      'Steamboat Springs, Colorado. Disaster has just struck the near by mountain of Hans Peak.\nYou are called to '
      'the ranger station to help in the search efforts...')

print('\nYou arrive at the station. The rangers tell you that there is 6 skiers missing.\nThe missing skiers are '
      'Amber, Dan, Darby, Jake, Julia, and Spencer.\nThe rangers warn you that the snow is very unstable and you '
      'should be careful on the steeper slopes.\nYou hop on a snowmobile and drive to the location the group was '
      'last seen...\n\nYou are at the drop off location. Where would you like to go from here?\nYou can enter '
      'north, east, south, or west or type exit at eny point to end the game.')

# Get users direction, unless the user enters exit. If the user enters exit, end the game.
direction_from_user = input('\nEnter Direction: ').strip().capitalize()
while direction_from_user != 'Exit':
    while direction_from_user not in acceptable_directions:
        direction_from_user = input('\nInvalid Entry. Enter Direction: ').strip().capitalize()
    else:
        while direction_from_user not in rooms[current_room]:
            print(
                f'\nYou have hit a map boundary. You can not go {direction_from_user.lower()} from here. You are still '
                f'in the {current_room}.')
            print('\nFrom here you can go:')
            while direction_from_user not in acceptable_directions:
                direction_from_user = input('\nInvalid Entry. Enter Direction: ').strip().capitalize()
            for directions in rooms[current_room]:
                if directions in acceptable_directions:
                    print(f'*{directions}')
            direction_from_user = input('\nEnter a different direction: ').capitalize()
        current_room = get_new_state(current_room, direction_from_user)
        show_status()
    if 'Avalanche' in user_items:
        if avy_function() == 'n':
            print(f'Goodbye {user_name}')
            break
        else:
            current_room = 'Drop off Location'
            user_items = []
            print('\nResetting game...\n')
            show_status()
            direction_from_user = input('\nEnter Direction: ').strip().capitalize()
    else:
        if user_items == full_item_list:
            print(f'\nCongratulations {user_name} you win!!!')
            break
        else:
            direction_from_user = input('\nEnter Direction: ').strip().capitalize()
else:
    print(f'\nGoodbye {user_name}')
