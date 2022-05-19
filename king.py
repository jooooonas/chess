from piece import Piece

class King(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def check_move(self, x, y, board):
        # maximum distance: 1
        return (abs(x - self.posX) <= 1 and abs(y - self.posY) <= 1
        and super().check_move(x, y))
    
    def kick(self, x, y, board):
        print("I'm a stub")

    def covered_spots(self, board):
        res = set()
        if self.posX == 7 and self.posY == 7:
            res = {(6, 7), (6, 6), (7, 6)}
        elif self.posX == 7 and self.posY == 0:
            res = {(6, 0), (6, 1), (7, 1)}
        elif self.posX == 0 and self.posY == 7:
            res = {(1, 7), (1, 6), (0, 6)}
        elif self.posX == 0 and self.posY == 0:
            res = {(1, 0), (1, 1), (0, 1)}
        elif self.posX == 7:
            res = {(7, self.posY - 1), (7, self.posY + 1), (6, self.posY - 1), (6, self.posY), (6, self.posY - 1)}
        elif self.posX == 0:
            res = {(0, self.posY - 1), (0, self.posY + 1), (1, self.posY - 1), (1, self.posY), (1, self.posY - 1)}
        elif self.posY == 7:
            res = {(self.posX - 1, 7), (self.posX + 1, 7), (self.posX - 1, 6), (self.posX, 6), (self.posX + 1, 6)}
        elif self.posY == 0:
            res = {(self.posX - 1, 0), (self.posX + 1, 0), (self.posX - 1, 1), (self.posX, 1), (self.posX + 1, 1)}
        else:
            for i in range(3):
                for j in range(3):
                    res.add(self.posX + 1 - i, self.posY + 1 - j)
            # remove spot where king is on
            res.remove(self.posX, self.posY)
        return res
        
    def __repr__(self):
        return "King"