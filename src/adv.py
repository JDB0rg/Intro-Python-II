from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def get_room_with_ifs(cmd, current_room):
    if cmd == 'n':
        return current_room.n_to 
    elif cmd == 's':
        return current_room.s_to 
    elif cmd == 'w':
        return current_room.w_to 
    elif cmd == 'e':
        return current_room.e_to 

def get_room(cmd, current_room):
    moving = cmd + '_to'
    return getattr(current_room, moving, None)
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
#
print("Enter a key to continue...\n [n]orth\n [s]outh\n [e]ast\n [w]est\n or [q]uit.")
directions = ['n', 's', 'e', 'w']
while True:
    # * Prints the current room name
    print(player.current_room)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # * Waits for user input and decides what to do.
    cmd = input(" -> ")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if cmd in directions:
        new_room = get_room(cmd, current_room)
        if new_room is not None:
            player.current_room = new_room
        else: 
            print("You can't move any further in that direction.")
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    elif cmd == 'q':
        break
    else: 
        print("Invalid input. Please enter any of the following:, {directions}")