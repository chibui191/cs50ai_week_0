"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    # Access each row in board list & count the number of X's and O's
    if not terminal(board):
      for i in range(0,3):
        for j in range(0,3):
          if board[i][j] == X:
            count_X += 1
          elif board[i][j] == O:
            count_O += 1
      return X if count_X == count_O else O
    else:
      return 2
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    if not terminal(board):
      for i in range(0,3):
        for j in range(0,3):
          if board[i][j] is EMPTY:
            possible_moves.append((i, j))
      return possible_moves
    else:
      return 2



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if action is valid for the board
    if action in actions(board):
        # Check whose turn it is
        symbol = player(board)
        # Make deep copy of the original board
        copied = copy.deepcopy(board)
        # Update cell in copied version of the board
        i, j = action
        copied[i][j] = symbol
        return copied
    else:
        raise Exception("Invalid Action") 



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winnning_combos = [[(0,0), (0,1), (0,2)],
                       [(1,0), (1,1), (1,2)],
                       [(2,0), (2,1), (2,2)],
                       [(0,0), (1,0), (2,0)],
                       [(0,1), (1,1), (2,1)],
                       [(1,0), (1,1), (1,2)],
                       [(0,0), (1,1), (2,2)],
                       [(0,2), (1,1), (2,0)]]
    # Log all X's cells:
    moves_X = []
    moves_O = []
    for i in range(0,3):
      for j in range(0,3):
        if board[i][j] == X:
          moves_X.append((i,j))
        elif board[i][j] == O:
          moves_O.append((i,j))
    
    set_moves_X = set(moves_X)
    set_moves_O = set(moves_O)

    # Check if either moves_X or moves_O contains a winning combo
    for win in winnning_combos:
      set_win = set(win)
      if set_win.issubset(set_moves_X):
        return X
      elif set_win.issubset(set_moves_O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if anybody has won the game
    if not winner(board) is None:
      return True
    else:
      for i in range(0,3):
        for j in range(0,3):
          if board[i][j] == EMPTY:
            return False
      return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p = winner(board)
    if p == X:
      return 1
    elif p == O:
      return -1
    else:
      return 0

    
# minimax_value with alpha-beta pruning
def minimax_value(board):
    if terminal(board):
        return utility(board), None

    alpha = float("-inf")
    beta = float("inf")
    p = player(board)
    best_move = None

    if p == X:  
        for action in actions(board):
            value = minimax_value(result(board, action))[0]
            if value > alpha:
              alpha = value
              best_move = action
            if beta <= alpha:
                break
        return alpha, best_move

    elif p == O:
        for action in actions(board):
            value = minimax_value(result(board, action))[0]
            if value < beta:
              beta = value
              best_move = action
            if beta <= alpha:
                break
        return beta, best_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        return minimax_value(board)[1]