from pawn import Pawn
from piece import Piece
from rook import Rook
from queen import Queen
from bishop import Bishop
from knight import Knight

# creating a dict mapping from field to piece, whenever the piece covers this field
# board: chess board from which the dict is created
# colour: colour of attacker
# oneOrTwo: if this integer is zero -> function only return dict for attacking player
#           if this integer is one -> function returns both dicts
# return value: tuple of dict for attacking player and dict for defending player
def create_check_dict(board, colour, oneOrTwo):
    dict1 = {}
    dict2 = {}
    for i in range(8):
        for j in range(8):
            if board[j][i] != None and board[j][i].colour == colour:
                set = board[j][i].covered_spots(j, i, board)
                for field in set:
                    try:
                        dict1.update({field: dict1.get(field).union({board[j][i]})})
                    except AttributeError:
                        dict1.update({field: {board[j][i]}})
            elif oneOrTwo and board[j][i] != None and board[j][i].colour != colour:
                set = board[j][i].covered_spots(j, i, board)
                for field in set:
                    try:
                        dict2.update({field: dict2.get(field).union({board[j][i]})})
                    except AttributeError:
                        dict2.update({field: {board[j][i]}})
    return (dict1, dict2) if oneOrTwo else dict1

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
            check_dict.update({(oldX - i - 1, oldY - i - 1): covered_by})
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
    # FUNKTIONIERT DAS? COVERED_SPOTS IST STATIC ABER AUFRUF DURCH "p.cove..." FINDET DAS DIE RICHTIGE KLASSE?
    # first remove old covered spots
    covered_spots = piece.covered_spots(oldX, oldY, board)
    for spot in covered_spots:
        check_dict[0].update({spot: (check_dict[0].get(spot)).discard(p)})
    # second add new covered spots
    covered_spots = piece.covered_spots(piece.posX, piece.posY, board)
    for spot in covered_spots:
        check_dict[0].update({spot: check_dict[0].get(spot).union(p)})
    # check if moved piece is defending some spots
    for piece in check_dict[0].get((piece.posX, piece.posY)):
        print("TODO")
    for piece in check_dict[1].get((piece.posX, piece.posY)):
        print("TODO")


# chess_board: 2D array of chesspieces
# check_board: 2D array of all spots which are covered
# colour: colour of attacking player
# king: king of defending player
def check_mate(chess_board, check_dict, colour, king):
    for (x, y) in check_dict[1]:
        for piece in check_dict[1].get((x, y)):
            # Pawn is only allowed to go diagonale if there is something to kick or "en passant"
            # ==> otherwise continue
            if ((type(piece) == Pawn and chess_board[x][y] == None) or 
            (chess_board[x][y] != None and chess_board[x][y].colour != colour)):
                continue
            tmp = chess_board[x][y]
            oldX = piece.posX
            oldY = piece.posY
            chess_board[piece.posX][piece.posY] = None
            chess_board[x][y] = piece
            piece.posY = y
            piece.posX = x
            new_dict = create_check_dict(chess_board, colour, 0)
            chess_board[x][y] = tmp
            chess_board[oldX][oldY] = piece
            if new_dict.get((king.posX, king.posY)) == None:
                # dont change posY and posX earlier because if piece is king then king.posX in line above is leading to failure
                piece.posY = oldY
                piece.posX = oldX
                return False
            piece.posY = oldY
            piece.posX = oldX
    return True
    # also check if a pawn can prevent check mate by going straight
    # straight moves for pawn are not added to check_dict
