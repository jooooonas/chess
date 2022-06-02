from piece import Piece

class Knight(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def copy(self):
        return Knight(self.posX, self.posY, self.colour)

    def check_move(self, x, y, board):
        return (((abs(x - self.posX) == 1 and abs(y - self.posY) == 2)
        or (abs(x - self.posX) == 2 and abs(y - self.posY) == 1)) and
        super().check_move(x, y))

    @staticmethod
    def covered_spots(posX, posY, board):
        # add all coordinates and remove the ones out of the board or the one covering your team
        res = {(posX - 2, posY + 1), (posX - 1, posY + 2),
        (posX + 1, posY + 2), (posX + 2, posY + 1),
        (posX + 2, posY - 1), (posX + 1, posY - 2),
        (posX - 1, posY - 2), (posX - 2, posY - 1)}
        # now remove the invalid ones
        for tmp in res.copy():
            if (tmp[0] < 0 or tmp[0] > 7 or tmp[1] < 0 or tmp[1] > 7):
                res.remove(tmp)
        return res
        
    def __repr__(self):
        return "Knight"