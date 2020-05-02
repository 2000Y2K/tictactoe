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
    cant_x = 0
    cant_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                cant_x += 1
            elif board[i][j] == O:
                cant_o += 1
    if cant_x > cant_o:
        return O
    else:
        return X
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tablero = copy.deepcopy(board)
    jugador = player(tablero)
    print(action)
    if tablero[action[0]][action[1]] != EMPTY:
        raise NameError("invalid input")
    else:
        tablero[action[0]][action[1]] = jugador
        return tablero

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range (3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
    
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
    if board[0][0]==X and board[1][1]==X and board[2][2]==X:
        return X
    elif board[0][0]== O and board[1][1]== O and board[2][2]== O:
        return O
    elif board[0][2]==X and board[1][1]==X and board[2][0]==X:
        return X
    elif board[0][2]==O and board[1][1]==O and board[2][0]==O:
        return O
    else:
        return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
         return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Alpha-Beta Pruning pseudocode9 I read on wikipedia https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    """
    play = None
    alpha = -(math.inf)
    beta = math.inf

    if player(board) == O:

        p = math.inf    
        for action in actions(board):
            i = maxi(result(board,action))
            beta = min(beta,i)
            if alpha >= beta:
                break
            if p > i:
                p = i
                play = action
    elif player(board) == X:
        
        p = -(math.inf)
        for action in actions(board):
            i = mini(result(board,action))
            alpha = max(alpha,i)
            if alpha >= beta:
                break
            if i > p:
                p = i
                play = action
    return play

def mini(board):
    """
    returns best move for O player
    """

    value = math.inf
    if terminal(board) == True:
        return utility(board)
    for action in actions(board):
        value = min(value,maxi(result(board,action)))
    return value



def maxi(board):
    """
    return best move for X player
    """
    value = -(math.inf)
    if terminal(board) == True:
        return utility(board)
    for action in actions(board):
        value = max(value,mini(result(board,action)))
    return value
