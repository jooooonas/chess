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

    @staticmethod
    def covered_spots(posX, posY, _):
        if (posX == 0):
            return {(posX + 1, posY)}
        elif (posX == 7):
            return {(posX - 1, posY)}
        else:
            return {(posX + 1, posY), (posX - 1, posY)}

    def __repr__(self):
        return "Pawn"