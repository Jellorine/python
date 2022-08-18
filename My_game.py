from IPython.display import clear_output

def display_board(board):
    clear_output() #Remember this only works in jupyter
    
    print('   |      |      |')
    print(''+ board[13]+'  |   '+board[14] +  '  |  '+ board[15]+ '  |  '+ board[16])
    print('   |      |      |')
    print('--------------------')
    print('   |      |      |')
    print(''+ board[9]+'  |   '+board[10] +  '  |  '+ board[11]+ '   |  '+ board[12])
    print('   |      |      |')
    print('--------------------')
    print('   |      |      |')
    print(''+ board[5]+'  |   '+board[6] +  '  |  '+ board[7]+ '   |  '+ board[8])
    print('   |      |      |')
    print('--------------------')
    print('   |      |      |')
    print(''+ board[1]+'  |   '+board[2] +  '  |  '+ board[3]+ '   |  '+ board[4])
    print('   |      |      |')


def player_input():
    marker = ''
    while not (marker=='X' or marker=='O'or marker=='H'):
        marker = input('Player 1: Do you want to be X or O or H?').upper()
    if marker == 'X':
        return ('X','O','H')
    elif marker == 'H':
        return ('H','X','O')    
    else:
        return ('O','X','H')

    
def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,mark):

    return ((board[13]==mark and board[14]==mark and board[15]==mark and board[16]==mark) or 
            (board[9]==mark and board[10]==mark and board[11]==mark and board[12]==mark) or
        (board[5]==mark and board[6]==mark and board[7]==mark and board[8]==mark) or
            (board[1]==mark and board[2]==mark and board[3]==mark and board[4]==mark) or
            (board[13]==mark and board[9]==mark and board[5]==mark and board[1]==mark) or
            (board[14]==mark and board[10]==mark and board[6]==mark and board[2]==mark) or
            (board[15]==mark and board[11]==mark and board[7]==mark and board[3]==mark) or
            (board[16]==mark and board[12]==mark and board[8]==mark and board[4]==mark))
    

   
import random

def choose_first():
    if random.randint(0,2) == 0:
        return 'Player 3'
    elif random.randint(0,2) == 1:
        return 'Player 2'     
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position] == ' ' 

def full_board_check(board):
    for i in range(1,17):
        if space_check(board,i):
            return False
    return True    


def player_choice(board,player):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] or not space_check(board,position):
        position = int(input(player +'Choose your next position: (1-16)'))
    return position    

def replay():
    
    return input('Do you want to play again? Enter Yes or No:').lower().startswith('y')


print('WELCOME to TIC TAC TOE!')

while True:
    #Reset the board
    theBoard = [' ']*17
    print(theBoard)
    player1_marker,player2_marker,player3_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0]== 'y':
        game_on = True
    else: 
        game_on = False
        
        
    while game_on:
        if turn == 'Player 1':
        #player1's turn
        
            display_board(theBoard)
            position = player_choice(theBoard, 'Player 1')
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'



        elif turn == 'Player 2':
        #player1's turn
        
            display_board(theBoard)
            position = player_choice(theBoard, 'Player 2')
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 3'
                       
                    
                    
        else:
            display_board(theBoard)
            position = player_choice(theBoard, 'Player 3')
            place_marker(theBoard,player3_marker,position)
            
            if win_check(theBoard,player3_marker):
                display_board(theBoard)
                print('Congratulations!Player 3 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'
                    
            
    
    if not replay():
        break    

