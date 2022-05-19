from piece import Piece

class Pawn(Piece):
    # 0: pawn has moved
    # 1: pawn hasn't moved yet
    untouched = 1

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def check_move(self, x, y, board):
        if self.colour == 'w':
            if self.untouched:
                return x == self.posX and (y == 2 or y == 3) and board[x][2] == None
            else:
                result = x == self.posX and y == self.posY + 1 and y <= 7
                if result:
                    self.untouched = 0
                    return result
        else:
            if self.untouched:
                return x == self.posX and (y == 5 or y == 4) and board[x][5] == None
            else:
                result = x == self.posX and y == self.posY - 1 and y >= 0
                if result:
                    self.untouched = 0
                    return result
    
    def kick(self, x, y, board):
        print("I'm a stub")

    def covered_spots(self, _):
        if (self.posX == 0):
            return {(self.posX + 1, self.posY)}
        elif (self.posX == 7):
            return {(self.posX - 1, self.posY)}
        else:
            return {(self.posX + 1, self.posY), (self.posX - 1, self.posY)}

    def __repr__(self):
        return "Pawn"