from pawn import Pawn
from piece import Piece
from rook import Rook
from queen import Queen
from king import King
from bishop import Bishop
from knight import Knight

# creating a dict mapping from field to piece, whenever the piece covers this field
# board: chess board from which the dict is created
# colour: colour of attacker
# return value: tuple of dict for attacking player and dict for defending player
def create_check_dict(board, colour):
    dict1 = {}
    dict2 = {}
    for i in range(7):
        for j in range(7):
            if board[j][i] != None and board[j][i].colour == colour:
                set = board[j][i].covered_spots(j, i, board)
                for field in set:
                    dict1.update({field: dict1.get(field).union(board[j][i])})
            elif board[j][i] != None and board[j][i].colour != colour:
                set = board[j][i].covered_spots(j, i, board)
                for field in set:
                    dict2.update({field: dict2.get(field).union(board[j][i])})
    return (dict1, dict2)

def update_helper_straight(board, oldX, oldY, check_dict, p):
    if oldX == p.posX:
        if oldY < p.posY:
            for i in range(oldY):
                covered_by = check_dict.get((oldX, oldY - i - 1)).union(p)
                check_dict.update({(oldX, oldY - i - 1): covered_by})
                if board[oldX][oldY - i - 1] != None:
                    break
        else:
            for i in range(7 - oldY):
                covered_by = check_dict.get((oldX, oldY + i + 1)).union(p)
                check_dict.update({(oldX, oldY + i + 1): covered_by})
                if board[oldX][oldY + i + 1] != None:
                    break
    elif oldY == p.posY:
        if oldX < p.posX:
            for i in range(oldX):
                covered_by = check_dict.get((oldX - i - 1, oldY)).union(p)
                check_dict.update({(oldX - i - 1, oldY): covered_by})
                if board[oldX - i - 1][oldY] != None:
                    break
        else:
            for i in range(7 - oldX):
                covered_by = check_dict.get((oldX + i + 1, oldY)).union(p)
                check_dict.update({(oldX + i + 1, oldY): covered_by})
                if board[oldX + i + 1][oldY] != None:
                    break

def update_helper_diagonale(board, oldX, oldY, check_dict, p):
    if oldX < p.posX and oldY < p.posY:
        for i in range(min(oldX, oldY)):
            covered_by = check_dict.get((oldX - i - 1, oldY - i - 1)).union(p)
            check_dict.update({(oldX - i - 1 oldY - i - 1): covered_by})
            if board[oldX - i - 1][oldY - i - 1] != None:
                break
    elif oldX < p.posX and oldY > p.posY:
        for i in range(min(oldX, 7 - oldY)):
            covered_by = check_dict.get((oldX - i - 1, oldY + i + 1)).union(p)
            check_dict.update({(oldX - i - 1, oldY + i + 1): covered_by})
            if board[oldX - i - 1][oldY + i + 1] != None:
                break
    elif oldX > p.posX and oldY > p.posY:
        for i in range(min(7 - oldX, 7 - oldY)):
            covered_by = check_dict.get((oldX + i + 1, oldY + i + 1)).union(p)
            check_dict.update({(oldX + i + 1, oldY + i + 1): covered_by})
            if board[oldX + i + 1][oldY + i + 1] != None:
                break
    elif oldX > p.posX and oldY > p.posY:
        for i in range(min(oldX, oldY)):
            covered_by = check_dict.get((oldX + i + 1, oldY - i - 1)).union(p)
            check_dict.update({(oldX + i + 1, oldY - i - 1): covered_by})
            if board[oldX + i + 1][oldY - i - 1] != None:
                break



# Dont forget to delete piece from dict when kicking
# check_dict: tuple of two dicts of all covered spots. First one contains
# all spots covered by attacking colour (= colour of piece)
def update_dict(board, piece, oldX, oldY, check_dict):
    set_of_attackers = check_dict[0].get(oldX, oldY)
    set_of_defenders = check_dict[1].get(oldX, oldY)
    for p in set_of_attackers:
        if type(p) == Rook:
            update_helper_straight(board, oldX, oldY, check_dict[0], p)
        elif type(p) == Bishop:
            update_helper_diagonale(board, oldX, oldY, check_dict[0], p)
        elif type(p) == Queen:
            update_helper_diagonale(board, oldX, oldY, check_dict[0], p)
            update_helper_straight(board, oldX, oldY, check_dict[0], p)
    for p in set_of_defenders:
        if type(p) == Rook:
            update_helper_straight(board, oldX, oldY, check_dict[1], p)
        elif type(p) == Bishop:
            update_helper_diagonale(board, oldX, oldY, check_dict[1], p)
        elif type(p) == Queen:
            update_helper_diagonale(board, oldX, oldY, check_dict[1], p)
            update_helper_straight(board, oldX, oldY, check_dict[1], p)
    # update the spots covered by moved piece as well
    # FUNKTIONIERT DAS? COVERED_SPOTS IST STATIC ABER AUFRUF DURCH "p.cove..." FINDER DAS DIE RICHTIGE KLASSE?
    # first remove old covered spots
    covered_spots = p.covered_spots(oldX, oldY, board)
    for spot in covered_spots:
        check_dict[0].update({spot: (check_dict[0].get(spot)).discard(p)})
    # second add new covered spots
    covered_spots = p.covered_spots(p.posX, p.posY, board)
    for spot in covered_spots:
        check_dict[0].update({spot: check_dict[0].get(spot).union(p)})

# chess_board: 2D array of chesspieces
# check_board: 2D array of all spots which are covered
# colour: colour of attacking player
def check_mate(chess_board, check_dict, colour):

