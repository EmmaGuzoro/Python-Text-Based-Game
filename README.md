# Python-Text-Based-Game
A text based game whereby the player navigates through various rooms and collects items in order to defeat the final boss in the last room. 

# MAP DRAWING

Drawing a map of the rooms and adding items to the room which will serve as a reference point when creating a dictionary for the rooms and adding navigations through the rooms, collection of items, checking of inventory and challenging the boss. With the diagram of the map at hand, I am 10% closer to the final line of code of the text-based game.

# IN-GAME INSTRUCTIONS

The function 'instructions' is used to store the various instructions which is necessary to read through and not forget because most of the important messages on how to defeat the boss and navigate the game are written there. 
The start game function is used to kick off the game when the player is done reading through the instructions by typing the keyword 'enter

# GAME MOVEMENT

The rooms that are located on the map are keyed in to a dictionary; the direction being the key and the new room as the value. This leads me to setting up the variables for that was used for the game navigation in the "main" function such as the 'movement' variable, 'item_pick variable', 'inventory' and so on.
Setting up the gameplay was made possible using a while loop to continue running the game till the boss is either defeated by the player or the player is defeated by the boss.
The main function is called up in the last line of the codes to start the gameplay as soon as one runs the program using a python interpreter