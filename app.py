from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BLANK_SPACE = " "
DASHES = "-------"
player1 = "X"
player2 = "O"

# Function to initialize the board
def initialize_board():
    return [[BLANK_SPACE, BLANK_SPACE, BLANK_SPACE],
            [BLANK_SPACE, BLANK_SPACE, BLANK_SPACE],
            [BLANK_SPACE, BLANK_SPACE, BLANK_SPACE]]

# Function to check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Function to check if the board is full
def is_full(board):
    for row in board:
        if BLANK_SPACE in row:
            return False
    return True

@app.route('/')
def index():
    board = initialize_board()
    return render_template('game.html', board=board, next_player=player1)

@app.route('/move', methods=['POST'])
def move():
    # Get the entire board as a list (flat list of strings)
    board = request.form.getlist('board')  # Get the entire board as a flat list
    print(f"Raw board data: {board}")  # Debugging line to check the raw board data

    # Convert the board into a 2D list (3x3 grid)
    board = [board[i:i+3] for i in range(0, len(board), 3)]
    print(f"Board after conversion: {board}")  # Debugging line to check the reconstructed board

    # Get the current player
    current_player = request.form['player']
    
    # Get the player's move (row and column)
    try:
        row = int(request.form['row'])  # Convert to 0-based index
        col = int(request.form['col'])  # Convert to 0-based index
    except (ValueError, KeyError) as e:
        print(f"Error converting row/col: {e}")
        return "Invalid move data received.", 400  # Return a 400 error if row/col are invalid

    print(f"Player {current_player} moves to row {row}, col {col}")  # Debugging line to check row and col

    # Check if the move is valid
    if board[row][col] == BLANK_SPACE:
        board[row][col] = current_player  # Update the board with the current player's move

    # Check for a winner
    winner = None
    if check_winner(board, current_player):
        winner = current_player
    
    # Check for a draw
    if is_full(board) and winner is None:
        winner = "Draw"

    # Set the next player
    next_player = player2 if current_player == player1 else player1

    return render_template('game.html', board=board, winner=winner, next_player=next_player)



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

