# Author: Emily Ho
# Github username: emxhh
# Date: 5/28/24
# Description: Atomic chess game

class Player:
    """"""

    def __init__(self, name, color):
        self._name = name
        self._color = color


class ChessVar:
    """"""

    def __init__(self):
        self._board = []
        # setup initial board with pieces
        for m in range(8):
            self._board.append([])
            for n in range(8):
                self._board[n].append("")

        self._game_state = "UNFINISHED"

    def get_game_state(self):
        """"""
        return self._game_state

    def make_move(self, move_from, move_to):
        """"""
        # if move_from does not have the player's piece, return false
        # if the move is invalid, return false
        # if the game_state is won, return false

        # else make the move
        # remove exploded pieces
        # update game_state if necessary
        # return true

    def print_board(self):
        """"""
        # print game board


class ChessPiece:
    """"""

    def __init__(self, name, color):
        self._name = name
        self._color = color


class Pawn(ChessPiece):
    """"""

    def __init__(self, name, color):
        super().__init__(name, color)
        self._move_count = 0

    def is_valid_move(self, color, position):
        """"""
        pass

