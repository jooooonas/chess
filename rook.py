from piece import Piece

class Rook(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def __repr__(self):
        return "Rook"

    def check_move(self, x, y, board):
        # check whether rook stays on chessboard
        return super().check_move(x, y) and super().check_move_straight(x, y, board)

    @staticmethod
    def covered_spots(posX, posY, board):
        res = set()
        # left direction
        for i in range(posX):
            if board[posX - i - 1][posY] == None:
                res.add((posX - i - 1, posY))
            else:
                res.add((posX - i - 1, posY))
                break
        # right direction
        for i in range(7 - posX):
            if board[posX + i + 1][posY] == None:
                res.add((posX + i + 1, posY))
            else:
                res.add((posX + i + 1, posY))
                break
        # down
        for i in range(posY):
            if board[posX][posY - i - 1] == None:
                res.add((posX, posY - i - 1))
            else:
                res.add((posX, posY - i - 1))
                break
        # up
        for i in range(7 - posY):
            if board[posX][posY + i + 1] == None:
                res.add((posX, posY + i + 1))
            else:
                res.add((posX, posY + i + 1))
                break
        return res

