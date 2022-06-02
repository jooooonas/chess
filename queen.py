from piece import Piece

class Queen(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def copy(self):
        return Queen(self.posX, self.posY, self.colour)

    def check_move(self, x, y, board):
        # check whether queen stays on chessboard
        return (super().check_move(x, y) and
        # valid straight move?
        (super().check_move_straight(x, y, board) or
            # or valid diagonale move?
            super().check_move_diagonale(x, y, board)))

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
        # left-up
        for i in range(min(posX, 7 - posY)):
            if board[posX - 1 - i][posY + i + 1] == None:
                res.add((posX - 1 - i, posY + i + 1))
            else:
                res.add((posX - 1 - i, posY + i + 1))
                break
        # right-up
        for i in range(min(7 - posX, 7 - posY)):
            if board[posX + i + 1][posY + i + 1] == None:
                res.add((posX + i + 1, posY + i + 1))
            else:
                res.add((posX + i + 1, posY + i + 1))
                break
        # right-down
        for i in range(min(7 - posX, posY)):
            if board[posX + i + 1][posY - i - 1] == None:
                res.add((posX + i + 1, posY - i - 1))
            else:
                res.add((posX + i + 1, posY - i - 1))
                break
        # left-down
        for i in range(min(posX, posY)):
            if board[posX - i - 1][posY - i - 1] == None:
                res.add((posX - i - 1, posY - i - 1))
            else:
                res.add((posX - i - 1, posY - i - 1))
                break
        return res
        
    def __repr__(self):
        return "Queen"