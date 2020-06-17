#Global Variables

    # board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

    # if game is still going
game_still_going = True

    # tie or win
winner = None

    # Turn
player = "x"


#display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# play game 
def play_game():
     # setup global variable
    global winner

    # display the initial board
    display_board()
    

    while game_still_going:
         
        # handle a single turn of a player
        handle_turn(player)
        
        # check  if the game has ended
        check_if_game_over()

        # switch player
        flip_player()
    # end of game
    if winner == 'x' or winner == 'o' :
        print('the player : ' + winner + '  , won !')
    elif winner== None :
        print('Tie !')


# handle turn 
def handle_turn(player):

    print('turn : ' + player)
    position = input('choose a position from 1 to 9: ')

    valid = False
    while not valid :

        while position not in ['1','2','3','4','5','6','7','8','9'] :
            position=input("Invalid input. choose a position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again ")


    board[position] = player

    display_board()

# check if game over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

# check if win 
def check_for_winner():
    # setup global variable
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else :
        winner = None
    
   
#check rows 
def check_rows():
     # setup global variable
    global game_still_going

    #check if rows have same value and not empty 
    row_1 = board[0] == board[1] == board[2] != '-' 

    row_2 = board[3] == board[4] == board[5] != '-' 

    row_3 = board[6] == board[7] == board[8] != '-' 

    # if row does have a match
    if row_1 or row_2 or row_3:
        game_still_going= False
    # return winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


#check columns
def check_columns():
    # setup global variable
    global game_still_going

    #check if columns have same value and not empty 
    column_1 = board[0] == board[3] == board[6] != '-' 

    column_2 = board[1] == board[4] == board[7] != '-' 

    column_3 = board[2] == board[5] == board[8] != '-' 

    # if column does have a match
    if column_1 or column_2 or column_3:
        game_still_going= False
    # return winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


#check diagonals
def check_diagonals():
     # setup global variable
    global game_still_going

     #check if diagonals have same value and not empty 
    diag_1 = board[0] == board[4] == board[8] != '-' 

    diag_2 = board[2] == board[4] == board[6] != '-' 

    # if diagonal does have a match
    if diag_1 or diag_2 :
        game_still_going= False
    # return winner
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
   



# check tie / no winner
def check_if_tie():
    global game_still_going

    if  '-' not in board:
        game_still_going = False
    return

#flip player
def flip_player():

    # setup global variable
    global player 

    # switch player
    if player =='x':
        player = 'o'
    elif player =='o':
        player = 'x'
   


play_game()