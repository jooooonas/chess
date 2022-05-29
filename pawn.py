from piece import Piece

class Pawn(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def check_move(self, x, y, board):
        if self.colour == 'w':
            if self.untouched:
                return x == self.posX and (y == 2 or y == 3) and board[x][2] == None
            else:
                return x == self.posX and y == self.posY + 1 and y <= 7
        else:
            if self.untouched:
                return x == self.posX and (y == 5 or y == 4) and board[x][5] == None
            else:
                return x == self.posX and y == self.posY - 1 and y >= 0

    def kick(self, x, y, board):
        # direction: white goes y + 1 but black goes y - 1
        direction = 1
        if self.colour == 'b':
            direction = -1
        # check if it is legitimate kicking move
        if ((x == self.posX - 1 or x == self.posX + 1) and
        y == self.posY + direction and super().check_move(x, y)):
            self.posX = x
            self.posY = y
            self.untouched = 0
            return True
        return False


    @staticmethod
    def covered_spots(posX, posY, board):
        # direction: white goes y + 1 but black goes y - 1
        direction = 1
        if board[posX][posY].colour == 'b':
            direction = -1
        if (posX == 0):
            return {(posX + 1, posY + direction)}
        elif (posX == 7):
            return {(posX - 1, posY + direction)}
        else:
            return {(posX + 1, posY + direction), (posX - 1, posY + direction)}

    def __repr__(self):
        return "Pawn"