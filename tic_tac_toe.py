#----------------------the-game-function---------------------------------
from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]]

def display_board(board):
    print('+-------+-------+-------+')
    for row in board:
        print('|       |       |       |')
        print(f'|   {row[0]}   |   {row[1]}   |   {row[2]}   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Enter a number between 1 and 9.")
                continue
            for row_in in range(3):
                for col_in in range(3):
                    if board[row_in][col_in] == move:
                        board[row_in][col_in] = "O"
                        return
            print("That square is already taken.")
        except ValueError:
            print("Numbers only please.")

def free_space(board):
    free = []
    for row_in in range(3):
        for col_in in range(3):
            if board[row_in][col_in] != "O" and board[row_in][col_in] != "X":
                free.append((row_in, col_in))  # 2. collect free squares as tuples
    return free

def draw_move(board):
    free = free_space(board)
    pick = free[randrange(len(free))]   # random index from the list
    board[pick[0]][pick[1]] = "X"

def victory_for(board, sign):
    #----------------------cas1-------------------------
    # 1
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    # 2
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    # 3
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    #---------------------------cas2-------------------------
    # 1
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    # 2
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    #--------------------------cas3--------------------------------------
    # 1
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    # 2
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    # 3
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    return False

#----------------------------the-game-programe-----------------------------------#
print("let's play huuman  !!!")
board[1][1] = "X"
display_board(board)

while True:
    if victory_for(board, "X"):
        print("I win HAHA")
        break
    if len(free_space(board)) == 0:
        print("YOU.... BasT###")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("i was easy on you hmfffff")
        break
    draw_move(board)
    display_board(board)