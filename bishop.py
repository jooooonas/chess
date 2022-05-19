from piece import Piece

class Bishop(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def check_move(self, x, y, board):
        return super().check_move_diagonale(x, y, board) and super().check_move(x, y)
    
    def kick(self, x, y, board):
        print("I'm a stub")

    def covered_spots(self, board):
        res = set()
        # left-up
        for i in range(min(self.posX, 7 - self.posY)):
            if board[self.posX - 1 - i][self.posY + i + 1] == None:
                res.add((self.posX - 1 - i, self.posY + i + 1))
            else:
                res.add((self.posX - 1 - i, self.posY + i + 1))
                break
        # right-up
        for i in range(min(7 - self.posX, 7 - self.posY)):
            if board[self.posX + i + 1][self.posY + i + 1] == None:
                res.add((self.posX + i + 1, self.posY + i + 1))
            else:
                res.add((self.posX + i + 1, self.posY + i + 1))
                break
        # right-down
        for i in range(min(7 - self.posX, self.posY)):
            if board[self.posX + i + 1][self.posY - i - 1] == None:
                res.add((self.posX + i + 1, self.posY - i - 1))
            else:
                res.add((self.posX + i + 1, self.posY - i - 1))
                break
        # left-down
        for i in range(min(self.posX, self.posY)):
            if board[self.posX - i - 1][self.posY - i - 1] == None:
                res.add((self.posX - i - 1, self.posY - i - 1))
            else:
                res.add((self.posX - i - 1, self.posY - i - 1))
                break
        return res
        
    def __repr__(self):
        return "Bishop"