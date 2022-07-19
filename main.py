# Define empty board. It is modified as the game goes on
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
# Set first turn to X
turn = 'X'

# Arrays of positions of put elements
x_pos = []
o_pos = []

# Winner variable
winner = ['']


# Helper function to display the board in console
def display_board(board_in):
    board_temp = ""
    for row in range(3):
        for col in range(3):
            if col != 2:
                board_temp += board_in[row][col] + '|'
            else:
                board_temp += board_in[row][col]
        if row != 2:
            board_temp += '\n_ _ _\n'

    print(f'{board_temp}\n')


# Putting element (either O or X) to the board
def put_element(element, coord_in):
    board[coord_in[0] - 1][coord_in[1] - 1] = element

    # Save the coordinates of the elements for checking the winner
    if element == 'X':
        x_pos.append(coord_in)
    else:
        o_pos.append(coord_in)


# Check if the position is occupied
def check_coord(coord_in):
    # check if the square filled with something other than empty space
    if board[coord_in[0] - 1][coord_in[1] - 1] != ' ':
        return False

    return True


# Read the coordinates where user wants to put their element
def get_coords(turn_in, situation=''):

    # Get coordinates from the user
    if situation == 'w_coords':
        coord_out = input(f"Occupied element. Enter again. {turn_in}'s coordinates\n")
    else:
        coord_out = input(f"{turn_in}'s coordinates\n")

    return coord_out


# Checking the winner, returns 'w'
def check_winner(turn_in):
    # check if there is a horizontal connection
    if turn_in == 'X':
        if not (hor_conn(x_pos)) and not (ver_conn(x_pos)) and not (diag_conn(x_pos)):
            return 'O'

    else:
        if not (hor_conn(o_pos)) and not (ver_conn(o_pos)) and not (diag_conn(o_pos)):
            return 'X'

    winner[0] = turn_in

    return 'W'


# Check if it is a tie
def tie():
    if len(x_pos) >= 5:
        return True
    return False

# --- FUNCTIONS FOR CHECKING CONNECTED ELEMENTS --- #


# Check for horizontally connected elements
def hor_conn(positions):
    i = 0
    rows = [0] * 3
    while i < len(positions):
        rows[positions[i][0] - 1] += 1
        i += 1
    return True if 3 in rows else False


# Check for vertically connected elements
def ver_conn(positions):
    i = 0
    cols = [0] * 3
    while i < len(positions):
        cols[positions[i][1] - 1] += 1
        i += 1
    return True if 3 in cols else False


# Check for diagonally connected elements
def diag_conn(positions):
    dig = [[[1, 1], [2, 2], [3, 3]], [[2, 2], [1, 3], [3, 1]]]
    ds = [[0], [0]]

    for pair in positions:
        if pair in dig[0]:
            ds[0].append(1)
        if pair in dig[1]:
            ds[1].append(1)

    if sum(ds[0]) == 3 or sum(ds[1]) == 3:
        return True
    return False


# --- MAIN LOOP --- #

if __name__ == '__main__':
    print('\n\nWelcome to tic-tac-toe! X"s turn. Enter the coordinates where you want to put it. (Example: 1 1 is '
          'the top left corner, 3 3 is the bottom right corner')

    coord = get_coords(turn)

    # coord = 1111 stops the game
    while coord != 1111:
        # Prepare the format of the coordinates
        coord_list = [int(c) for c in coord.split()]

        # Check if the coordinate is not occupied
        while not check_coord(coord_list) and coord != 1111:
            coord = get_coords(turn, situation='w_coords')
            coord_list = [int(c) for c in coord.split()]

        # Put element to the coordinates
        put_element(turn, coord_list)

        # Display current board
        display_board(board)

        # Check if there is a winner
        turn = check_winner(turn)

        # Check if it is a tie
        if tie():
            print("It's a tie!")
            break

        # Break if there is a winner
        if turn == 'W':
            print(f"{winner[0]} is the Winner!")
            break

        # Ask for the next person's turn
        coord = input(f"{turn}'s coordinates\n")
