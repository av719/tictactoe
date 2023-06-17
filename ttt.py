board = [[" "," "," "],[" ", " ", " "],[" "," "," "]]
turnP1 = True
game = True
winner = ''

def printBoard(board):
    for i in board:
        print(i)

printBoard(board)

def win(board):
    for x in range(3):
        for y in range(3):
            if((board[0][y]=='X' and board[1][y]=='X' and board[2][y]=='X') or (board[x][0]=='X' and board[x][1]=='X' and board[x][2]=='X') or (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X')): 
                print("Winner is Player 1!")
                return True
            elif((board[0][y]=='X' and board[1][y]=='X' and board[2][y]=='X') or (board[x][0]=='X' and board[x][1]=='X' and board[x][2]=='X') or (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X')): 
                print("Winner is Player 2!")
                return True

def turn(turnP1):
    if (turnP1): print("Player 1's Turn")
    else: print("Player 2's Turn")

def move(turnP1,row, col):
    row = int(row)
    col = int(col)
    if (board[row][col]!=' '): 
        print('\nPlease enter a valid spot.\n')
        return False
    if (turnP1): choice = 'X'
    else: choice = 'O'
    if (row>2 or row<0 or col>2 or col<0): 
        print("\nPlease enter a valid spot.\n")
        return False
    else: 
        board[row][col] = choice
        return True

turn(turnP1)

while(game):
    row = input("Please enter desired row: ")
    col = input("Please enter desired column: ")
    if (move(turnP1,row,col)):
        printBoard(board)
        if(turnP1): turnP1 = False
        else: turnP1 = True
        if (win(board)): 
            game = False
            break
    turn(turnP1)
 