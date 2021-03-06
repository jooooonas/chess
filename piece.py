from abc import abstractmethod, ABC


class Piece(ABC):
    # 0: piece has moved
    # 1: piece hasn't moved yet
    untouched = 1

    # x, y defines starting position of chesspiece
    # c defines colour (black|white)
    @abstractmethod
    def __init__(self, x, y, c):
        self.posX = x
        self.posY = y
        self.colour = c
        return

    # returns a copy of the piece
    @abstractmethod
    def copy(self):
        pass

    # checks if move is valid for this type of chesspiece
    def check_move(self, x, y):
        # Check whether piece stays on chessboard and whether it actually moves
        return x >= 0 and x <= 7 and y >= 0 and y <= 7  and (self.posX != x or self.posY != y)

    # moves the piece to position x, y and calls check_move
    def move(self, x, y, board):
        if self.check_move(x, y, board):
            self.posX = x
            self.posY = y
            self.untouched = 0
            return True
        else:
            self.print_error(self.__class__.__name__, x, y)
            return False

    # moves piece to position x, y if valid move for kicking
    def kick(self, x, y, board):
        return self.move(x, y, board)

    # helper function for straight moving pieces
    def check_move_straight(self, x, y, board):
        # check whether no piece is in the way
        if y == self.posY and x - self.posX < 0: # left
            for i in range(self.posX - x - 1):
                if board[x + i + 1][y] != None:
                    return False
        elif y == self.posY: # right
            for i in range(x - self.posX - 1):
                if board[x - i - 1][y] != None:
                    return False
        elif x == self.posX and y - self.posY < 0: # down
            for i in range(self.posY - y - 1):
                if board[x][y + i + 1] != None:
                    return False
        elif x == self.posX: # up
            for i in range(y - self.posY - 1):
                if board[x][y - i - 1] != None:
                    return False
        else:
            return False
        return True

    # helper function for diagonale moving pieces
    def check_move_diagonale(self, x, y, board):
        if x - self.posX == y - self.posY and x - self.posX < 0: # direction: left - down
            for i in range(self.posX - x - 1):
                if board[x + i + 1][y + i + 1] != None:
                    return False
        elif x - self.posX == y - self.posY and x - self.posX > 0: # direction: right - up
            for i in range(x - self.posX - 1):
                if board[x - i - 1][y - i - 1] != None:
                    return False
        elif x - self.posX == self.posY - y and x - self.posX < 0: # direction left - up
            for i in range(self.posX - x - 1):
                if board[x + i + 1][y - i - 1] != None:
                    return False
        elif x - self.posX == self.posY - y: # direction right - down
            for i in range(x - self.posX - 1):
                if board[x - i - 1][y + i + 1] != None:
                    return False
        else:
            return False
        return True

    # returns set of coordinates of spots that are covered by this piece
    @abstractmethod
    def covered_spots(posX, posY, board):
        pass

    @staticmethod
    def print_error(classname, x, y):
        print(classname + " is not able to move to x: " + str(x) + " and y: " + str(y))

    @abstractmethod
    def __repr__(self):
        pass
