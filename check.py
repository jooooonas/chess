from piece import covered_spots

def create_check_dict(board, colour):
    dict1 = {}
    dict2 = {}
    for i in range(7):
        for j in range(7):
            if board[j][i] != None and board[j][i].colour == colour:
                set = board[j][i].covered_spots(board)
                dict1.update({board[j][i], dict1.get(board[j][i]).union(set)})
            elif board[j][i] != None and board[j][i].colour != colour:
                set = board[j][i].covered_spots(board)
                dict2.update({board[j][i], dict2.get(board[j][i]).union(set)})
    return (dict1, dict2)

def update_dict(board, piece)

# chess_board: 2D array of chesspieces
# check_board: 2D array of all spots which are covered
# colour: colour of attacking player
def check_mate(chess_board, check_dict, colour):

