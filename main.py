
#Tic Tac Toe game 
#require a board
#display board
#play game
#handle turn
#check win
  #check rows
  #check columns
  #check diagonals
#check tie
#flip player

#-------------GLOBAL VARIABLES----------------


# Creating an empty game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_is_still_going = True

# Who is the winner? or tie?
winner = None

current_player = "X"

# Displaying the board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():
  # Displays the initial board
  display_board()
  print()
  # While the game is still going
  while game_is_still_going:
    
    # Handle a single turn of an arbitrary player
    handle_turn(current_player)

    # Checks if the game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # The game has ended
  if winner == "X" or winner == "O":
    print()
    print(winner + " won.")
  elif winner == None:
    print()
    print("It's a tie!")

# Handle a single turn of an arbitrary player
def handle_turn(player):

  # Displaying the player's turn
  print()
  print(player + "'s turn.")
  # Asking the user to enter a position to enter either X or O
  position = input("Choose a position from 1-9: ")

  # Checking if the user enters only the numbers between the range 1-9
  if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    position = input("Invalid input. Choose a position from 1-9: ")


  position = int(position) - 1

  board[position] = player
  print()
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  # Setting up the global variable
  global winner
  # Check rows
  row_winner = check_rows()
  # Check columns
  column_winner = check_columns()
  # Check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

  return 

def check_rows():

  # Setting up the gobal variable
  global game_is_still_going
  # Checking if any of the rows have same value (and is not empty)0
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'

  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_is_still_going = False

  # Returns the winner(X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return 

def check_columns():
  # Setting up the global variable
  global game_is_still_going

  # Checking if any of the columns have same value, (and is not empty)
  col_1 = board[0] == board[3] == board[6] != '-'
  col_2 = board[1] == board[4] == board[7] != '-'
  col_3 = board[2] == board[5] == board[8] != '-'

  # If any of the columns have match, flag that there is a win
  if col_1 or col_2 or col_3:
    game_is_still_going = False

  # Returns the winner(X or O)
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]

  return  


def check_diagonals():

  # Setting up the global variable
  global game_is_still_going

  # Checking if the diagonals have same value, and is not empty
  diagonal_1 = board[0] == board[4] == board[8] != '-'
  diagonal_2 = board[2] == board[4] == board[6] != '-'

  # If any of the diagonals have match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_is_still_going = False

  # Returns the winner(X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]

  return

def check_if_tie():
  # Setting up the global variable
  global game_is_still_going

  # Checking if the board is empty
  if "-" not in board:
    game_is_still_going = False
  
  return


def flip_player():
  # Setting up the global variable
  global current_player
  # If the current player is "X" then change it to "O"
  if current_player == "X":
    current_player = "O"
  # If the current player is "O" then change it to "X"
  elif current_player == "O":
    current_player = "X" 
  return
  
  
play_game()
