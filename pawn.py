from piece import Piece
from queen import Queen
from knight import Knight
from bishop import Bishop
from rook import Rook

class Pawn(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def copy(self):
        return Pawn(self.posX, self.posY, self.colour)

    def promote(self, x, y, board):
        print("Choose which piece you would like to replace your pawn with:")
        print("Q -> queen; R -> rook; B -> bishop; K -> knight")
        while (1):
            choice = input()
            if choice == 'Q':
                prom = Queen(x, y, self.colour)
                break
            elif choice == 'R':
                prom = Rook(x, y, self.colour)
                break
            elif choice == 'B':
                prom = Bishop(x, y, self.colour)
                break
            elif choice == 'K':
                prom = Knight(x, y, self.colour)
                break
            print("Something went wrong. Choose again")
        board[self.posX][self.posY] = prom
        return True

    def check_move(self, x, y, board):
        if self.colour == 'w':
            if self.untouched:
                return x == self.posX and (y == 2 or y == 3) and board[x][2] == None
            else:
                res = x == self.posX and y == self.posY + 1 and y <= 7
                # promotion
                if res and y == 7:
                    return self.promote(x, y, board)
                return res
        else:
            if self.untouched:
                return x == self.posX and (y == 5 or y == 4) and board[x][5] == None
            else:
                res = x == self.posX and y == self.posY - 1 and y >= 0
                # promotion
                if res and y == 0:
                    return self.promote(x, y, board)
                return res

    def kick(self, x, y, board):
        # direction: white goes y + 1 but black goes y - 1
        direction = 1
        if self.colour == 'b':
            direction = -1
        # check if it is legitimate kicking move
        if ((x == self.posX - 1 or x == self.posX + 1) and
        y == self.posY + direction and super().check_move(x, y)):
            # check promotion
            if y == 0 or y == 7:
                return self.promote(x, y, board)
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