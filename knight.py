from piece import Piece

class Knight(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def check_move(self, x, y, board):
        return (((abs(x - self.posX) == 1 and abs(y - self.posY) == 2)
        or (abs(x - self.posX) == 2 and abs(y - self.posY) == 1)) and
        super().check_move(x, y))
    
    def kick(self, x, y, board):
        print("I'm a stub")

    def covered_spots(self, board):
        # add all coordinates and remove the ones out of the board or the one covering your team
        res = {(self.posX - 2, self.posY + 1), (self.posX - 1, self.posY + 2),
        (self.posX + 1, self.posY + 2), (self.posX + 2, self.posY + 1),
        (self.posX + 2, self.posY - 1), (self.posX + 1, self.posY - 2),
        (self.posX - 1, self.posY - 2), (self.posX - 2, self.posY - 1)}
        # now remove the invalid ones
        for tmp in res:
            if (tmp[0] < 0 or tmp[0] > 7 or tmp[1] < 0 or tmp[1] > 7 or
                (board[tmp[0]][tmp[1]] != None and board[tmp[0]][tmp[1]].colour == self.colour)):
                res.remove(tmp)
        return res
        
    def __repr__(self):
        return "Knight"