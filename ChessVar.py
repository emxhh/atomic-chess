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
        self._rows = 8
        self._columns = self._rows
        self._game_state = "UNFINISHED"
        self.initialize_board()

    def initialize_board(self):
        """"""
        for m in range(self._rows):
            self._board.append([])
            for n in range(self._columns):
                self._board[m].append(" ")

        # create black pawns
        for i in range(self._rows):
            pawn = Pawn("pawn", "black")
            self._board[1][i] = pawn

    def print_board(self):
        """"""
        print("  a", "b", "c", "d", "e", "f", "g", "h")
        for row in range(self._rows):
            print(str(row + 1) + " ", end="")
            for col in range(self._columns):
                position = self._board[row][col]
                print(position if isinstance(position, str) else position._unicode, end="")
                if col < self._rows:
                    print("|", end="")
            if row < self._rows:
                print("\n")

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
        self._unicode = "\u2659" if self._color == "white" else "\u265F"

    def is_valid_move(self, color, position):
        """"""
        pass


game = ChessVar()
game.print_board()