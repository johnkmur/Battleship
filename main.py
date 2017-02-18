#! /usr/bin/python

#types of ships
ship_list = {"carrier":5,
              "battleship":4,
             "submarine":3,
             "cruiser":2,
             "destroyer":2}

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

def update_board_A(start, end):
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

    print str(x_min) + " " + str(x_max) + " " + str(y_min) + " " + str(y_max)
    while (x_min != x_max or y_min != y_max):
        board_A[x_min][y_min] = 'S'
        if (move_vertical == True):
            y_min = y_min + 1
        else:
            x_min = x_min + 1
    board_A[x_min][y_min] = 'S'

def update_board_B(start, end):
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

    while (x_min != x_max or y_min != y_max):
        board_B[x_min][y_min] = 'S'
        if (move_vertical == True):
            y_min = y_min + 1
        else:
            x_min = x_min + 1
    board_B[x_min][y_min] = 'S'

def is_valid_placement(board_in, ship, start, end):
    x_start, y_start = start.split(",")
    x_end, y_end = end.split(",")

    x_min = min( int(x_start), int(x_end))
    x_max = max( int(x_start), int(x_end))
    y_min = min( int(y_start), int(y_end))
    y_max = max( int(y_start), int(y_end))

    vertical_diff = y_max - y_min
    horizontal_diff = x_max - x_min

    min_diff = min(vertical_diff, horizontal_diff)
    max_diff = max(vertical_diff, horizontal_diff) 

    if ( not (min_diff == 0 and max_diff == ship_list[ship] - 1) ):
        # Size of ship doesn't match
        return False

    move_vertical = False
    if (x_min == x_max):
        # We are moving vertically
        move_vertical = True

    while (x_min != x_max and y_min != y_max):
        if (board[x_min][y_min] != '.'):
            return False
        if (move_vertical == True):
            y_min = y_min + 1
        else:
            x_min = x_min + 1


    return True

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

    at_least_one_ship = False;

    while (not at_least_one_ship):
        ship_number = input("Would you like to play with a Carrier? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        if (str(ship_number) != 0):
            at_least_one_ship = True;
        ships["carrier"] = int(ship_number)

        ship_number = input("Would you like to play with a Battleship? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        if (str(ship_number) != 0):
            at_least_one_ship = True;
        ships["battleship"] = int(ship_number)

        ship_number = input("Would you like to play with a Submarine? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        if (str(ship_number) != 0):
            at_least_one_ship = True;
        ships["submarine"] = int(ship_number)

        ship_number = input("Would you like to play with a Cruiser? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        if (str(ship_number) != 0):
            at_least_one_ship = True;
        ships["cruiser"] = int(ship_number)

        ship_number = input("Would you like to play with a Destroyer? If so, how many? (Enter 0 if you don't want to use a carrier: ")
        if (str(ship_number) != 0):
            at_least_one_ship = True;
        ships["destroyer"] = int(ship_number)

        if (at_least_one_ship == False):
            print "You must select at least one ship."

    # Determine the minimum size board given the ships selected.
    

    print "\n"
    board_size = input("Enter the dimensions (Ex. type '10' if you want a 10x10 board) that you would like to play on: ")

    while ( int(board_size) < 1):
        print "Error, dimensions must be greater than one"
        board_size = input("Enter dimensions again: ")

    print "\nA battlefield of size " + str(board_size) + "x" + str(board_size) + " will be created."


    # Create the gameboard now, call constructor.
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

    # Switch to Player A so that they can place their ships.
    print "Player A will now select where to place their ships, Player B, look away.\n\n\n\n"

    for ship in ships:
        for num in range(ships[ship]):

            # Print board_A
            board_print(board_A)
            print "Where would you like to place this ship: " + ship + " (" + str(ship_list[ship]) + "x" + str(ship_list[ship]) + ")"
            coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
            coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")

            # Check if it is a valid spot to place the ship.
            valid = is_valid_placement(board_A, ship, str(coor_start), str(coor_end))
 
            while (not valid):
                print "\nI am sorry, that spot is already taken by another ship.\n"
                print "Where would you like to place this ship: " + ship + " (" + str(ship_list[ship]) + "x" + str(ship_list[ship]) + ")"
                coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
                coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")


            update_board_A(str(coor_start), str(coor_end))
            print "Successfully added the ship\n\n"

    print "Board A complete, Player A, this is the positioning of your ships."
    board_print(board_A)

    # Now switch to Player A so that they can place their ships.
    print "Now Player B will now select where to place their ships, Player A, look away.\n\n\n\n"

    for ship in ships:
        for num in range(ships[ship]):

            # Print board_A
            board_print(board_B)
            print "Where would you like to place this ship: " + ship + " (" + str(ship_list[ship]) + "x" + str(ship_list[ship]) + ")"
            coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
            coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")

            # Check if it is a valid spot to place the ship.
            valid = is_valid_placement(board_B, ship, str(coor_start), str(coor_end))
 
            while (not valid):
                print "\nI am sorry, that spot is already taken by another ship.\n"
                print "Where would you like to place this ship: " + ship + " (" + str(ship_list[ship]) + "x" + str(ship_list[ship]) + ")"
                coor_start = raw_input("Please enter the coordinates (x,y) of the front of the ship: ")
                coor_end = raw_input("Please enter the coordinates (x,y) of the back of the ship: ")


            update_board_B(str(coor_start), str(coor_end))
            print "Successfully added the ship\n\n"

    print "Board B complete, Player B, this is the positioning of your ships."
    board_print(board_B)

    # Now we get into the game play portion.
    turn = "A"

    
if __name__=="__main__":
    main()