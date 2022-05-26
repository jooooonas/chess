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
                    res.add(posX + 1 - i, posY + 1 - j)
            # remove spot where king is on
            res.remove(posX, posY)
        return res
        
    def __repr__(self):
        return "King"