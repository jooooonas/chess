from pawn import Pawn
from piece import Piece
from rook import Rook
from queen import Queen
from king import King
from bishop import Bishop
from knight import Knight
from check import *

# global variables
running = 1
player = 0
colour = ['w', 'b']
player_names = ['Player one', 'Player two']

# set up board
board = [
    [Rook(0, 0, "w"), Pawn(0, 1, "w"), None, None, None, None, Pawn(0, 6, "b"), Rook(0, 7, "b")],
    [Knight(1, 0, "w"), Pawn(1, 1, "w"), None, None, None, None, Pawn(1, 6, "b"), Knight(1, 7, "b")],
    [Bishop(2, 0, "w"), Pawn(2, 1, "w"), None, None, None, None, Pawn(2, 6, "b"), Bishop(2, 7, "b")],
    [Queen(3, 0, "w"), Pawn(3, 1, "w"), None, None, None, None, Pawn(3, 6, "b"), Queen(3, 7, "b")],
    [King(4, 0, "w"), Pawn(4, 1, "w"), None, None, None, None, Pawn(4, 6, "b"), King(4, 7, "b")],
    [Bishop(5, 0, "w"), Pawn(5, 1, "w"), None, None, None, None, Pawn(5, 6, "b"), Bishop(5, 7, "b")],
    [Knight(6, 0, "w"), Pawn(6, 1, "w"), None, None, None, None, Pawn(6, 6, "b"), Knight(6, 7, "b")],
    [Rook(7, 0, "w"), Pawn(7, 1, "w"), None, None, None, None, Pawn(7, 6, "b"), Rook(7, 7, "b")]
]


def getCoordinates(string):
    values = string.split(", ")
    return (int(values[0]), int(values[1]))

def ask_move():
    while (1):
        piece = input(player_names[player] + ", it's your turn. Which piece do you want to move?\n")
        destination = input(player_names[player] + ", where do you want to move? To choose a different piece just press enter\n")
        try:
            position = getCoordinates(piece)
            dest = getCoordinates(destination)
            return (position, dest)
        except:
            print("Choose a different piece!")
    
def print_board(board):
    for temp in board:
        for temp2 in temp:
            print("|" + str(temp2), end='')
        print("|")
    print("\n")

def check(king):
    check_dict = create_check_dict(board, colour[player], 1)
    if check_dict[0].get((king.posX, king.posY)) != None:
        return check_mate(board, check_dict, colour[player], king)
    return False

def game_over():
    print("GAME OVER")
    print(player_names[player] + " has won! Congratulations!")
    exit()

print("Welcome to this beatiful game of chess!")
print("Player 1 is white and player 2 is black.")
print("To move a chesspiece just type the piece's coordinates followed by the new coordinates:")
print("For example '3, 4' + '7, 4'")
print("If you want to rechoose your piece just type nothing")
print("Have fun!\n")

while (running):

    print_board(board)
    kings = (board[4][0], board[4][7])
    
    while (1):
        res = ask_move()
        piece = board[res[0][0]][res[0][1]]
        piece_dest = board[res[1][0]][res[1][1]]
        # check if player moves his own colour:
        if piece == None or piece.colour != colour[player]:
            continue
        # kick or move?
        if piece_dest != None:
            # check for correct input
            if piece_dest.colour != colour[player]:
                piece.kick(res[1][0], res[1][1], board)
                board[res[0][0]][res[0][1]] = None
                board[res[1][0]][res[1][1]] = piece
                break
        else:
            # check for correct input
            if piece != None and piece.colour == colour[player] and piece.move(res[1][0], res[1][1], board):
                board[res[0][0]][res[0][1]] = None
                board[res[1][0]][res[1][1]] = piece
                break

    if not check(kings[player]):
        game_over()

    player = (player + 1) % 2


# check for checkmate