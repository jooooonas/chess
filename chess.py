from pawn import Pawn
from piece import Piece
from rook import Rook
from queen import Queen
from king import King
from bishop import Bishop
from knight import Knight
from check import *
from tests import *


# set up board
# board = [
#     [Rook(0, 0, "w"), Pawn(0, 1, "w"), None, None, None, None, Pawn(0, 6, "b"), Rook(0, 7, "b")],
#     [Knight(1, 0, "w"), Pawn(1, 1, "w"), None, None, None, None, Pawn(1, 6, "b"), Knight(1, 7, "b")],
#     [Bishop(2, 0, "w"), Pawn(2, 1, "w"), None, None, None, None, Pawn(2, 6, "b"), Bishop(2, 7, "b")],
#     [Queen(3, 0, "w"), Pawn(3, 1, "w"), None, None, None, None, Pawn(3, 6, "b"), Queen(3, 7, "b")],
#     [King(4, 0, "w"), Pawn(4, 1, "w"), None, None, None, None, Pawn(4, 6, "b"), King(4, 7, "b")],
#     [Bishop(5, 0, "w"), Pawn(5, 1, "w"), None, None, None, None, Pawn(5, 6, "b"), Bishop(5, 7, "b")],
#     [Knight(6, 0, "w"), Pawn(6, 1, "w"), None, None, None, None, Pawn(6, 6, "b"), Knight(6, 7, "b")],
#     [Rook(7, 0, "w"), Pawn(7, 1, "w"), None, None, None, None, Pawn(7, 6, "b"), Rook(7, 7, "b")]
# ]
board = [
    [Rook(0, 0, "w"), Pawn(0, 1, "w"), None, None, None, None, Pawn(0, 6, "b"), Rook(0, 7, "b")],
    [None, Pawn(1, 1, "w"), None, None, None, None, Pawn(1, 6, "b"), None],
    [None, Pawn(2, 1, "w"), None, None, None, None, Pawn(2, 6, "w"), None],
    [None, None, None, None, None, None, None, Queen(3, 7, "b")],
    [King(4, 0, "w"), None, None, None, None, None, Pawn(4, 6, "b"), King(4, 7, "b")],
    [Bishop(5, 0, "w"), Pawn(5, 1, "w"), None, None, None, None, Pawn(5, 6, "b"), Bishop(5, 7, "b")],
    [Knight(6, 0, "w"), Pawn(6, 1, "w"), None, None, None, None, Pawn(6, 6, "b"), Knight(6, 7, "b")],
    [Rook(7, 0, "w"), Pawn(7, 1, "w"), None, None, None, None, Pawn(7, 6, "b"), Rook(7, 7, "b")]
]

# global variables
running = 1
player = 0
colour = ['w', 'b']
player_names = ['Player one', 'Player two']
kings = (board[4][0], board[4][7])

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
            if temp2 == None:
                print("\033[0;30m" + "|" + str(temp2), end='')
            elif temp2.colour == 'b':
                print("|" + "\033[1;30m" + str(temp2) + "\033[0;30m", end='')
            else:
                print("|" + "\033[1;37m" + str(temp2) + "\033[0;30m", end='')
        print("|")
    print("\033[0;37m" + "\n")

def single_turn():
    while (1):
        print("\nConsistency-test: " + str(test_board_consistency(board, kings)) + "\n")
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
                tmp = board[res[0][0]][res[0][1]]
                board[res[0][0]][res[0][1]] = None
                board[res[1][0]][res[1][1]] = tmp
                break
        else:
            # check for correct input
            if piece != None and piece.colour == colour[player] and piece.move(res[1][0], res[1][1], board):
                tmp = board[res[0][0]][res[0][1]]
                board[res[0][0]][res[0][1]] = None
                board[res[1][0]][res[1][1]] = tmp
                print(piece, piece.posX, piece.posY, res[1][0], res[1][1])
                break

def board_copy(board):
    copy = [[], [], [], [], [], [], [], []]
    for i in range(8):
        for j in range(8):
            if board[i][j] == None:
                copy[i].append(board[i][j])
            else:
                copy[i].append(board[i][j].copy())
    return copy


def check(king, col):
    global player
    global board
    check_dict = create_check_dict(board, col, 1)
    print(king.posX, king.posY, king.colour)
    print(check_dict[0].get((king.posX, king.posY)))
    if check_dict[0].get((king.posX, king.posY)) != None:
        # Just check for checkmate if we are checking enemy's king
        if king.colour != colour[player] and check_mate(board, check_dict, col, king):
            game_over()
        print("Check! Safe your king!")
        return True
    return False

def game_over():
    print("GAME OVER")
    print(player_names[player] + " has won! Congratulations!")
    exit()

def find_kings(board):
    for x in board:
        for piece in x:
            if type(piece) == King:
                if piece.colour == 'w':
                    king_w = piece
                elif piece.colour == 'b':
                    king_b = piece
    return (king_w, king_b)

print("Welcome to this beatiful game of chess!")
print("Player 1 is white and player 2 is black.")
print("To move a chesspiece just type the piece's coordinates followed by the new coordinates:")
print("For example '3, 4' + '7, 4'")
print("If you want to rechoose your piece just type nothing")
print("Have fun!\n")

while (running):

    print_board(board)
    
    copy = board_copy(board)

    while (True):
        print_board(board)
        single_turn()
        result = not check(kings[player], colour[(player + 1) % 2])
        print(result)
        if result:
            break
        else:
            board = board_copy(copy)
            kings = find_kings(board)

    check(kings[(player + 1) % 2], colour[player])

    player = (player + 1) % 2