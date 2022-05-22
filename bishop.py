from piece import Piece

class Bishop(Piece):

    def __init__(self, x, y, c):
        super().__init__(x, y, c)

    def check_move(self, x, y, board):
        return super().check_move_diagonale(x, y, board) and super().check_move(x, y)
    
    def kick(self, x, y, board):
        print("I'm a stub")

    @staticmethod
    def covered_spots(posX, posY, board):
        res = set()
        # left-up
        for i in range(min(posX, 7 - posY)):
            if board[posX - 1 - i][posY + i + 1] == None:
                res.add((posX - 1 - i, posY + i + 1))
            else:
                res.add((posX - 1 - i, posY + i + 1))
                break
        # right-up
        for i in range(min(7 - posX, 7 - posY)):
            if board[posX + i + 1][posY + i + 1] == None:
                res.add((posX + i + 1, posY + i + 1))
            else:
                res.add((posX + i + 1, posY + i + 1))
                break
        # right-down
        for i in range(min(7 - posX, posY)):
            if board[posX + i + 1][posY - i - 1] == None:
                res.add((posX + i + 1, posY - i - 1))
            else:
                res.add((posX + i + 1, posY - i - 1))
                break
        # left-down
        for i in range(min(posX, posY)):
            if board[posX - i - 1][posY - i - 1] == None:
                res.add((posX - i - 1, posY - i - 1))
            else:
                res.add((posX - i - 1, posY - i - 1))
                break
        return res
        
    def __repr__(self):
        return "Bishop"