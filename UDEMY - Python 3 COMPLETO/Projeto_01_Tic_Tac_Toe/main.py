# Curso UDEMY - Python 3 COMPLETO
# Projeto 01 - TIC TAC TOE
# Artur C. Baldon - 2021

def display_board(board):
    print()
    print(f"\t  {board[7]} | {board[8]} | {board[9]} \tPlayer X")
    print("\t----|---|----")
    print(f"\t  {board[4]} | {board[5]} | {board[6]} \t7 8 9")
    print("\t----|---|---- \t4 5 6")
    print(f"\t  {board[1]} | {board[2]} | {board[3]} \t1 2 3")
    print()


def player_turn(turn):
    if turn % 2 != 0:
        player = 'X'
    else:
        player = 'O'
    return player


progress = True
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
position = 0

while progress:
    for i in range(9):
        display_board(board)
        position = int(input("Qual posição? "))
        board[position] = player_turn(i)
        display_board(board)
    progress = False
