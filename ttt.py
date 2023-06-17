board = [[" "," "," "],[" ", " ", " "],[" "," "," "]]
turnP1 = True
game = True

def printBoard(board):
    for i in board:
        print(i)

printBoard(board)

def turn(turnP1):
    if (turnP1): print("Player 1's Turn")
    else: print("Player 2's Turn")

def move(turnP1,row, col):
    row = int(row)
    col = int(col)
    if (turnP1): choice = 'X'
    else: choice = 'O'
    board[row][col] = choice
    if (row>2 or row<0 or col>2 or col<0): return False
    else: return True

turn(turnP1)

while(game):
    row = input("Please enter desired row: ")
    col = input("Please enter desired column: ")
    if (move(turnP1,row,col)==True):
        printBoard(board)
        if(turnP1): turnP1 = False
        else: turnP1 = True
        turn(turnP1)

 
move(choice, row, col)
printBoard(board)