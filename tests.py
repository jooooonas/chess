from pawn import Pawn
from piece import Piece
from rook import Rook
from queen import Queen
from king import King
from bishop import Bishop
from knight import Knight
from check import *

def print_board(board):
    for temp in board:
        for temp2 in temp:
            print("|" + str(temp2), end='')
        print("|")
    print("\n")

board_start = [
    [Rook(0, 0, "w"), Pawn(0, 1, "w"), None, None, None, None, Pawn(0, 6, "b"), Rook(0, 7, "b")],
    [Knight(1, 0, "w"), Pawn(1, 1, "w"), None, None, None, None, Pawn(1, 6, "b"), Knight(1, 7, "b")],
    [Bishop(2, 0, "w"), Pawn(2, 1, "w"), None, None, None, None, Pawn(2, 6, "b"), Bishop(2, 7, "b")],
    [Queen(3, 0, "w"), Pawn(3, 1, "w"), None, None, None, None, Pawn(3, 6, "b"), Queen(3, 7, "b")],
    [King(4, 0, "w"), Pawn(4, 1, "w"), None, None, None, None, Pawn(4, 6, "b"), King(4, 7, "b")],
    [Bishop(5, 0, "w"), Pawn(5, 1, "w"), None, None, None, None, Pawn(5, 6, "b"), Bishop(5, 7, "b")],
    [Knight(6, 0, "w"), Pawn(6, 1, "w"), None, None, None, None, Pawn(6, 6, "b"), Knight(6, 7, "b")],
    [Rook(7, 0, "w"), Pawn(7, 1, "w"), None, None, None, None, Pawn(7, 6, "b"), Rook(7, 7, "b")]
]

board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, King(1, 3, 'b'), None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, King(3, 3, 'w'), None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]
]

board_kick = [
    [None, None, Pawn(0, 2, 'w'), None, None, None, None, None],
    [None, None, None, Rook(1, 3, 'b'), None, None, None, None],
    [None, None, Queen(2, 2, 'w'), None, None, None, None, None],
    [None, Pawn(3, 1, 'w'), None, None, None, None, None, Knight(3, 7, 'w')],
    [None, None, None, None, None, Knight(4, 5, 'b'), None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, Bishop(6, 3, 'w'), None, None, None, None],
    [None, None, None, King(7, 3, 'b'), None, King(7, 4, 'w'), None, None]
]

def test_board_consistency(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != None and (board[i][j].posX != i or board[i][j].posY != j):
                print(str(board[i][j]) + " on position x = " + str(i) + ", y = " +
                str(j) + "is not consitent to posX and posY: " + str(board[i][j].posX)
                + ", " + str(board[i][j].posY))
                return False

def test_check_mate():
    covered_spots = create_check_dict(board, 'w', 1)
    return check_mate(board, covered_spots, 'w', board[1][3])

def get_covered_spots():
    print(create_check_dict(board, 'w', 1))

def test_kick():
    board_copy = board_kick.copy()
    result = board_copy[1][3].kick(6, 3, board_copy)
    if (result == False):
        print("1st test failed")

    board_copy = board_kick.copy()
    result = board_copy[0][2].kick(1, 3, board_copy)
    if (result == False):
        print("2nd test failed")
        
    board_copy = board_kick.copy()
    result = board_copy[2][2].kick(1, 3, board_copy)
    if (result == False):
        print("3rd test failed")
        
    board_copy = board_kick.copy()
    result = board_copy[4][5].kick(3, 7, board_copy)
    if (result == False):
        print("4th test failed")
        
    board_copy = board_kick.copy()
    result = board_copy[3][7].kick(4, 5, board_copy)
    if (result == False):
        print("5th test failed")
        
    board_copy = board_kick.copy()
    result = board_copy[6][3].kick(4, 5, board_copy)
    if (result == False):
        print("6th test failed")
        
    board_copy = board_kick.copy()
    result = board_copy[7][3].kick(6, 3, board_copy)
    if (result == False):
        print("7th test failed")
        
    board_copy = board_kick.copy()
    result = board_copy[1][3].kick(2, 2, board_copy)
    if (result == True):
        print("8th test failed")
