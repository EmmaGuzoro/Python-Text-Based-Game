# 'Nriamah Guzorochukwu'
# Text Game codes

# creating introductory words when a player logs in to the game

def instructions():
    print("Welcome to the adventure game")
    print("You are to collect 8 key items from the rooms before heading for the boss")
    print("Use the keywords : 'Go west', 'Go east', 'Go north' and 'Go south' to navigate through the game")
    print("When you enter a room, use the keyword 'pick item' to collect the loot in the room")
    print("Key in 'inventory' to see a list of the items you have collected from the rooms")
    print("When you get to the 'Garage', use the keyword 'challenge boss' to take on the final boss")
    print("Are you ready to test your skills? Let's go!")
    print("--------------------------------------------")

def game_start():
    start_game = input("Welcome, Type 'enter' to Start: ")
    if start_game == 'enter':
        print('Select a difficulty')
    while start_game != 'enter':
        print('Type "enter" to Start, case sensitive')
        start_game = input("Welcome, Type 'enter' to Start: ")
        if start_game == 'enter':
            print('Select a difficulty')
        

# putting down the dictionary mapping for the rooms
rooms = {
    "Living Room": {
        "North": "Attic",
        "South": "Basement",
        "East": "Library",
        "West": "Corridor",
        "Description": "There is no item in this room"
    },
    "Attic": {
        "South": "Living Room",
        "West": "Ball Room",
        "Item": "Body Armour",
        "Description": "There is 'body armour' in this room",
    },
    "Ball Room": {
        "South": "Corridor",
        "East": "Attic",
        "Item": "Armour",
        "Description": "There is 'armour' in this room"
    },
    "Corridor": {
        "North": "Ball Room",
        "East": "Living Room",
        "Item": "Shotgun",
        "Description": "There is 'shotgun' in this room"
    },
    "Basement": {
        "North": "Living Room",
        "East": "Pool Room",
        "West": "Garden",
        "Item": "Portion",
        "Description": "There is 'portion' in this room"
    },
    "Pool Room": {
        "West": "Basement",
        "Item": "Bow and Arrow",
        "Description": "There is 'bow and arrow' in this room"
    },
    "Garden": {
        "East": "Basement",
        "South": "Courtyard",
        "Item": "Food",
        "Description": "There is 'food' in this room"
    },
    "Courtyard": {
        "North": "Garden",
        "Item": "Flame Thrower",
        "Description": "There is 'flame thrower' in this room"
    },
    "Library": {
        "North": "Garage",
        "West": "Living Room",
        "Item": "Map",
        "Description": "There is 'map' in this room"
    },
    "Garage": {
        "South": "Library",
        "Boss": "ICE MAN",  # boss
        "Description": "This is the final room. Do you wish to challenge the final boss?"
    }
}


# Game introduction
def main():
    movement = ['Go north', 'Go south', 'Go west', 'Go east']
    item_pick = 'pick item'
    inventory_command = 'inventory'
    current_room = 'Living Room'
    boss_challenge_command = 'challenge boss'
    inventory = set()
    items_required = 8

    instructions()
    game_start()

    # setting up the game movement.
    while True:
        move = input("")
        if move in movement:
            move = move.split()[1].capitalize()
            if move in rooms[current_room].keys():
                current_room = rooms[current_room][move]
                print(f'You are in the {current_room}')
                print(rooms[current_room]['Description'])
                print('Input a move')

        # creating codes for picking items
        elif move == item_pick:
            if 'Item' in rooms[current_room]:
                item = rooms[current_room]['Item']
                inventory.add(item)
                print(f'You are in the {current_room} and You have picked up: {item}')
                print('Input a move')
                del rooms[current_room]['Item']  # Remove item from room after picking
            elif 'Item' not in rooms[current_room]:
                print(f'You are in the {current_room} and there is nothing to pick')
                print('Input a move')

        # showing the list of inventory
        elif move == inventory_command:
            if inventory:
                print('You have collected the following items:')
                for item in inventory:
                    print(f'- {item}')
            else:
                print('Your inventory is empty.')
            print(f'You are in the {current_room}')
            print('Input a move')

        # Simulate a boss challenge
        elif move == boss_challenge_command and current_room == 'Garage':
            print("The ICE MAN appears!")
            if len(inventory) >= items_required:
                print("You have collected enough items. Prepare for the final challenge!")
                print("Choose your action: 'fight' or 'flee': ")
                action = input("")
                if action == 'fight':
                    print("You fought the ICE MAN and won the battle!")
                    print("Congratulations, you have completed the game!")
                    break  # to end the game after winning
                elif action == 'flee':
                    print("You chose to flee. The ICE MAN is still out there.")
                else:
                    print("Invalid action. Try 'fight' or 'flee'.")
            else:
                print("Game over, you don't have enough items to fight the boss. Try again")
                print("Try to collect more items next time and face the boss again.")
                break  # to end the game after loosing

        else:
            print("Invalid move.Enter valid move:('Go north','Go south','Go west','Go east','pick item' 'or' 'inventory').")


main()
