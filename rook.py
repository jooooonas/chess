from piece import Piece

class Rook(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def __repr__(self):
        return "Rook"

    def check_move(self, x, y, board):
        # check whether rook stays on chessboard
        return super().check_move(x, y) and super().check_move_straight(x, y, board)
    
    def kick(self, x, y, board):
        print("I'm a stub")

    def covered_spots(self, board):
        res = set()
        # left direction
        for i in range(self.posX):
            if board[self.posX - i - 1][self.posY] == None:
                res.add((self.posX - i - 1, self.posY))
            elif board[self.posX - i - 1][self.posY].colour == self.colour:
                break
            else:
                res.add((self.posX - i - 1, self.posY))
                break
        # right direction
        for i in range(7 - self.posX):
            if board[self.posX + i + 1][self.posY] == None:
                res.add((self.posX + i + 1, self.posY))
            elif board[self.posX + i + 1][self.posY].colour == self.colour:
                break
            else:
                res.add((self.posX + i + 1, self.posY))
                break
        # down
        for i in range(self.posY):
            if board[self.posX][self.posY - i - 1] == None:
                res.add((self.posX, self.posY - i - 1))
            elif board[self.posX][self.posY - i - 1].colour == self.colour:
                break
            else:
                res.add((self.posX, self.posY - i - 1))
                break
        # up
        for i in range(7 - self.posY):
            if board[self.posX][self.posY + i + 1] == None:
                res.add((self.posX, self.posY + i + 1))
            elif board[self.posX][self.posY + i + 1].colour == self.colour:
                break
            else:
                res.add((self.posX, self.posY + i + 1))
                break
        return res

