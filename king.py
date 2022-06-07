from piece import Piece
from check import *

class King(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def copy(self):
        return King(self.posX, self.posY, self.colour)

    # returns the enemies' colour
    def enemy_colour(self):
        if self.colour == 'w':
            return 'b'
        else:
            return 'w'

    def no_cuddling(self, x, y, board):
        for row in board:
            for piece in row:
                if type(piece) == King and piece != self:
                    return abs(piece.posX - x) > 1 or abs(piece.posY - y) > 1


    def check_move(self, x, y, board):
        # check castling
        if ((x == 2 or x == 6) and self.untouched == 1 and
        (y == 0 or y == 7) and y == self.posY and self.posX == 4):
            dict = create_check_dict(board, self.enemy_colour(), 0)
            if self.posX - 2 == x:
                for i in range(5):
                    if dict.get((i, y)) != None:
                        return False
                if (board[self.posX - 1][y] != None or board[self.posX - 2][y] != None or board[self.posX - 3][y] != None
                or self.untouched != 1 or type(board[0][y]) != Rook or board[0][y].untouched != 1):
                    return False
                self.posX = x
                self.posY = y
                self.untouched = board[0][y].untouched = 0
                board[0][y].posX = 3
                board[3][y] = board[0][y]
                board[0][y] = None
                return True
            else:
                for i in range(5):
                    if dict.get((7 - i, y)) != None:
                        return False
                if (board[6][y] != None or board[5][y] != None or self.untouched != 1 or
                type(board[7][y]) != Rook or board[7][y].untouched != 1):
                    return False
                self.posX = x
                self.posY = y
                self.untouched = board[7][y].untouched = 0
                board[7][y].posX = 5
                board[5][y] = board[7][y]
                board[7][y] = None
                return True
        # maximum distance: 1
        return (abs(x - self.posX) <= 1 and abs(y - self.posY) <= 1
        and super().check_move(x, y) and self.no_cuddling(x, y, board))

    @staticmethod
    def covered_spots(posX, posY, board):
        res = set()
        if posX == 7 and posY == 7:
            res = {(6, 7), (6, 6), (7, 6)}
        elif posX == 7 and posY == 0:
            res = {(6, 0), (6, 1), (7, 1)}
        elif posX == 0 and posY == 7:
            res = {(1, 7), (1, 6), (0, 6)}
        elif posX == 0 and posY == 0:
            res = {(1, 0), (1, 1), (0, 1)}
        elif posX == 7:
            res = {(7, posY - 1), (7, posY + 1), (6, posY - 1), (6, posY), (6, posY + 1)}
        elif posX == 0:
            res = {(0, posY - 1), (0, posY + 1), (1, posY - 1), (1, posY), (1, posY + 1)}
        elif posY == 7:
            res = {(posX - 1, 7), (posX + 1, 7), (posX - 1, 6), (posX, 6), (posX + 1, 6)}
        elif posY == 0:
            res = {(posX - 1, 0), (posX + 1, 0), (posX - 1, 1), (posX, 1), (posX + 1, 1)}
        else:
            for i in range(3):
                for j in range(3):
                    res.add((posX + 1 - i, posY + 1 - j))
            # remove spot where king is on
            res.remove((posX, posY))
        # remove spots where king would cuddle
        for (x, y) in res.copy():
            if not board[posX][posY].no_cuddling(x, y, board):
                res.remove((x, y))
        return res
        
    def __repr__(self):
        return "King"