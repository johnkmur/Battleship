#! /usr/bin/python

# John Murphy
# Coatue Coding Challenge

# Types of ships with their abbreviations as well as their length.
ship_list = {"carrier":['5', 'C'],
              "battleship":['4', 'b'],
             "submarine":['3', 's'],
             "cruiser":['2', 'c'],
             "destroyer":['2', 'd']}

# Player A's ships
my_ships_A = {}

# The coordinates of all of Player A's ships
ship_coordinates_A = []

# Player B's ships
my_ships_B = {}

# The coordinates of all of Player B's ships
ship_coordinates_B = []

# Player A's gameboard, this represents Player A's ship positions and where 
# Player B has attacked.
board_A = []

# Player B's gameboard, this represents Player B's ship positions and where
# Player A has attacked.
board_B = []

# Player A's target record, this is a record of where A has attacked and whether
# is was a hit ('H') or a miss ('M').
board_A_targets = []

# Player B's target record, this is a record of where A has attacked and whether
# is was a hit ('H') or a miss ('M').
board_B_targets = []

# Create the boards used for gameplay
def create_boards(board_size):
    for i in range( int(board_size) ):
        board_row = []
        for j in range( int(board_size) ):
            board_row.append('.')
        board_A.append(board_row)

    for i in range( int(board_size) ):
        board_row = []
        for j in range( int(board_size) ):
            board_row.append('.')
        board_B.append(board_row)

    for i in range( int(board_size) ):
        board_row = []
        for j in range( int(board_size) ):
            board_row.append('.')
        board_A_targets.append(board_row)

    for i in range( int(board_size) ):
        board_row = []
        for j in range( int(board_size) ):
            board_row.append('.')
        board_B_targets.append(board_row)

    return board_A, board_B, board_A_targets, board_B_targets

# This function is used to roughly determine the minimum board size to allow for
# the placement of the ships that the user selected.
def determine_min_size(ships):
    max_length = -1
    total_area = 0
    for ship in ships:
        if (ships[ship] > 0):
            total_area = total_area + (ships[ship] * int(ship_list[ship][0]) )
            if (int(ship_list[ship][0]) > max_length):
                max_length = int(ship_list[ship][0])
    
    return max_length, total_area

# Returns true if the sink was sunk.
def is_ship_sunk(coordinates, destination, my_ships):
    x_coor, y_coor = coordinates.split(",")

    x_coor = int(x_coor)
    y_coor = int(y_coor)

    type_of_ship = destination[x_coor][y_coor]

    for i in range( len(my_ships[type_of_ship] )):
        if coordinates in my_ships[type_of_ship][i]:
            my_ships[type_of_ship][i].remove(coordinates)
            if (len(my_ships[type_of_ship][i]) == 0):
                return True;

    return False

# Determines if missile hit or missed.
def fire_at_target(coordinates, source, destination, player_ships, my_ships):
    x_coor, y_coor = coordinates.split(",")

    x_coor = int(x_coor)
    y_coor = int(y_coor)

    if (destination[x_coor][y_coor] is '.'):
        # Miss
        destination[x_coor][y_coor] = 'M'
        source[x_coor][y_coor] = 'M'
        print "MISS"
        return player_ships

    else:
        # Hit, check if last missile sunk the ship
        sunk = is_ship_sunk(coordinates, destination, my_ships)

        destination[x_coor][y_coor] = 'H'
        source[x_coor][y_coor] = 'H'

        if (sunk == True):
            player_ships = player_ships - 1
            print "HIT and sunk a ship!"
        else:
            print "Target HIT!"

        return player_ships


# Checks that target is within battlefield dimensions and not visited before.
def is_valid_target(board_in, coordinates):
    x_coor, y_coor = coordinates.split(",")

    if (int(x_coor) < 0 or int(x_coor) > len(board_in)-1):
        print "Sorry, the coordinate you have entered is not valid, try again."
        return False

    if (int(y_coor) < 0 or int(y_coor) > len(board_in)-1):
        print "Sorry, the coordinate you have entered is not valid, try again."
        return False

    if (board_in[int(x_coor)][int(y_coor)] == 'H' or board_in[int(x_coor)][int(y_coor)] == 'M'):
        print "Sorry, you have already fired at this location, try again."
        return False

    return True

# Places a Player A's ships onto their board.
def place_ship_A(start, end, ship):
    x_start, y_start = start.split(",")
    x_end, y_end = end.split(",")

    x_min = min( int(x_start), int(x_end))
    x_max = max( int(x_start), int(x_end))
    y_min = min( int(y_start), int(y_end))
    y_max = max( int(y_start), int(y_end))

    move_vertical = False
    if (x_min == x_max):
        # We are moving vertically
        move_vertical = True

    all_coors = []
    while (x_min != x_max or y_min != y_max):
        board_A[x_min][y_min] = ship_list[ship][1]
        all_coors.append(str(x_min) + "," + str(y_min))
        if (move_vertical == True):
            y_min = y_min + 1
        else:
            x_min = x_min + 1
    board_A[x_min][y_min] = ship_list[ship][1]
    all_coors.append(str(x_min) + "," + str(y_min))
    ship_coordinates_A.append(all_coors)
    my_ships_A[ship_list[ship][1]] = ship_coordinates_A

# Places a Player B's ships onto their board.
def place_ship_B(start, end, ship):
    x_start, y_start = start.split(",")
    x_end, y_end = end.split(",")

    x_min = min( int(x_start), int(x_end))
    x_max = max( int(x_start), int(x_end))
    y_min = min( int(y_start), int(y_end))
    y_max = max( int(y_start), int(y_end))

    move_vertical = False
    if (x_min == x_max):
        # We are moving vertically
        move_vertical = True

    all_coors = []
    while (x_min != x_max or y_min != y_max):
        board_B[x_min][y_min] = ship_list[ship][1]
        all_coors.append(str(x_min) + "," + str(y_min))
        if (move_vertical == True):
            y_min = y_min + 1
        else:
            x_min = x_min + 1
    board_B[x_min][y_min] = ship_list[ship][1]
    all_coors.append(str(x_min) + "," + str(y_min))
    ship_coordinates_B.append(all_coors)
    my_ships_B[ship_list[ship][1]] = ship_coordinates_B

# Returns True is a ship can be placed in the given location, False otherwise.
def is_valid_placement(board_in, ship, start, end):
    x_start, y_start = start.split(",")
    x_end, y_end = end.split(",")

    x_min = min( int(x_start), int(x_end))
    x_max = max( int(x_start), int(x_end))
    y_min = min( int(y_start), int(y_end))
    y_max = max( int(y_start), int(y_end))

    if (x_min < 0 or y_min < 0 or x_max > len(board_in) - 1 or y_max > len(board_in) - 1):
        print "\nSorry, please choose coordinates within the battlefield\n"
        return False

    vertical_diff = y_max - y_min
    horizontal_diff = x_max - x_min

    min_diff = min(vertical_diff, horizontal_diff)
    max_diff = max(vertical_diff, horizontal_diff) 

    if ( not (min_diff == 0 and max_diff == int(ship_list[ship][0]) - 1) ):
        # Size of ship doesn't match
        print "\nSorry, that is not the correct dimension of the ship, try again.\n"
        return False

    move_vertical = False
    if (x_min == x_max):
        # We are moving vertically
        move_vertical = True

    while (x_min != x_max or y_min != y_max):
        if (board_in[x_min][y_min] == '.'):
            if (move_vertical == True):
                y_min = y_min + 1
            else:
                x_min = x_min + 1
        else:
            print "\nSorry, this spot is already taken, try again.\n"
            return False
        
    return True

# Game board print function
def board_print(board_in):
    board_size_in = len(board_in)
    line = "  "
    for i in range(board_size_in):
        line = line + str(i) + ' '
    print line
    line = ''

    j = 0
    for row in board_in:
        line = line + str(j) + ' '
        for col in row:
            line = line + col + ' '
        print line
        line = ""
        j = j + 1

def main():
    ships = {}
    print "Which ships would you like to play with and how many?"
    print "The ships available are:\nCarrier (5x1)\nBattleship (4x1)\nSubmarine (3x1)\nCruiser (2x1)\nDestroyer (2x1)\n"

    num_ships = 0

    while (num_ships == 0):
        ship_number = input("Would you like to play with a Carrier? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        ships["carrier"] = int(ship_number)
        num_ships = num_ships + int(ship_number)

        ship_number = input("Would you like to play with a Battleship? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        ships["battleship"] = int(ship_number)
        num_ships = num_ships + int(ship_number)

        ship_number = input("Would you like to play with a Submarine? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        ships["submarine"] = int(ship_number)
        num_ships = num_ships + int(ship_number)

        ship_number = input("Would you like to play with a Cruiser? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        ships["cruiser"] = int(ship_number)
        num_ships = num_ships + int(ship_number)

        ship_number = input("Would you like to play with a Destroyer? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        ships["destroyer"] = int(ship_number)
        num_ships = num_ships + int(ship_number)

        if (num_ships == 0):
            print "You must select at least one ship."

    # Determine the minimum size board given the ships selected.
    max_length, total_area = determine_min_size(ships)
    
    print "\n"
    board_size = input("Enter the dimensions (Ex. type '10' if you want a 10x10 board) that you would like to play on: ")

    while ( int(board_size) < 1):
            print "Error, dimensions must be greater than one"
            board_size = input("Enter dimensions again: ")

    good_board_size = False
    while (not good_board_size):
        if ( (int(board_size) * int(board_size)) < total_area or int(board_size) < max_length):
            print "Given the number of ships and type of ships that you entered, the battlefield needs to be larger"
            board_size = input("Enter dimensions again: ")
        else:
            good_board_size = True

    print "\nA battlefield of size " + str(board_size) + "x" + str(board_size) + " will be created."

    # Create the gameboards
    board_A, board_B, board_A_targets, board_B_targets = create_boards(int(board_size))

    # Switch to Player A so that they can place their ships.
    print "Player A will now select where to place their ships, Player B, look away.\n\n"

    for ship in ships:
        for num in range(ships[ship]):
            # Print board_A
            board_print(board_A)
            print "Where would you like to place this ship: " + ship + " (" + ship_list[ship][0] + "x" + ship_list[ship][0] + ")"
            coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
            coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")

            # Check if it is a valid spot to place the ship.
            valid = is_valid_placement(board_A, ship, str(coor_start), str(coor_end))
 
            while (not valid):
                print "Where would you like to place this ship: " + ship + " (" + ship_list[ship][0] + "x" + ship_list[ship][0] + ")"
                coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
                coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")
                valid = is_valid_placement(board_A, ship, str(coor_start), str(coor_end))


            place_ship_A(str(coor_start), str(coor_end), ship)
            print "Successfully added the ship\n\n"

    print "Board A complete, Player A, this is the positioning of your ships."
    board_print(board_A)

    # Now switch to Player A so that they can place their ships.
    print "Now Player B will now select where to place their ships, Player A, look away.\n\n"

    for ship in ships:
        for num in range(ships[ship]):

            # Print board_A
            board_print(board_B)
            print "Where would you like to place this ship: " + ship + " (" + ship_list[ship][0] + "x" + ship_list[ship][0] + ")"
            coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
            coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")

            # Check if it is a valid spot to place the ship.
            valid = is_valid_placement(board_B, ship, str(coor_start), str(coor_end))
 
            while (not valid):
                print "Where would you like to place this ship: " + ship + " (" + ship_list[ship][0] + "x" + ship_list[ship][0] + ")"
                coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
                coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")


            place_ship_B(str(coor_start), str(coor_end), ship)
            print "Successfully added the ship\n\n"

    print "Board B complete, Player B, this is the positioning of your ships."
    board_print(board_B)

    # Now we get into the game play portion.
    # Set up players
    player_A_ships = num_ships
    player_B_ships = num_ships

    game_over = False
    turn = "A"
    winner = ""

    while (not game_over):
        # Display the Player's board so that they know how they are doing.
        if (turn == "A"):
            print "\n\nThis is your board \n"
            board_print(board_A)

            print "\nNow select the coordinate that you want to target on Player B's board.\n"
            board_print(board_A_targets)

            target = raw_input("\nWhat coordinate (x,y) would you like to fire at?: ")

            valid = is_valid_target(board_A_targets, str(target))
 
            while (not valid):
                # print "\nI am sorry, that spot is not a valid target. Try again.\n"
                target = raw_input("\nWhat coordinate (x,y) would you like to fire at?: ")
                valid = is_valid_target(board_A_targets, str(target))

            player_B_ships = fire_at_target(str(target), board_A_targets, board_B, player_B_ships, my_ships_B)

            if (player_B_ships == 0):
                game_over = True
                winner = turn
            else:
                turn = "B"
        else:
            print "\n\nThis is your board \n"
            board_print(board_B)

            print "\nNow select the coordinate that you want to target on Player B's board.\n"
            board_print(board_B_targets)

            target = raw_input("\nWhat coordinate (x,y) would you like to fire at?: ")

            valid = is_valid_target(board_B_targets, str(target))
 
            while (not valid):
                # print "\nI am sorry, that spot is not a valid target. Try again.\n"
                target = raw_input("\nWhat coordinate (x,y) would you like to fire at?: ")
                valid = is_valid_target(board_B_targets, str(target))

            player_A_ships = fire_at_target(str(target), board_B_targets, board_A, player_A_ships, my_ships_A)

            if (player_A_ships == 0):
                game_over = True
                winner = turn
            else:
                turn = "A"

    print "\n\nGAME OVER, Player " + winner + " has won!"
    
if __name__=="__main__":
    main()