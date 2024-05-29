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
        self._rows = 8
        self._columns = self._rows
        self._game_state = "UNFINISHED"
        self._chess_pieces = {}
        self.initialize_board()

    def initialize_board(self):
        """"""
        for row in range(self._rows):
            self._board.append([])
            for col in range(self._columns):
                self._board[row].append(" ")

        # initialize black pawns
        for col in range(self._columns):
            col_coordinate = chr(col + 97)
            row_coordinate = 7
            coordinates = col_coordinate + str(row_coordinate)
            pawn = Pawn("pawn", "black", coordinates)
            self._board[row_coordinate - 1][col] = pawn
            self._chess_pieces[coordinates] = pawn

        # initialize white pawns
        for col in range(self._columns):
            col_coordinate = chr(col + 97)
            row_coordinate = 2
            coordinates = col_coordinate + str(row_coordinate)
            pawn = Pawn("pawn", "white", coordinates)
            self._board[row_coordinate - 1][col] = pawn
            self._chess_pieces[coordinates] = pawn

    def print_board(self):
        """"""
        print("  a", "b", "c", "d", "e", "f", "g", "h")
        for row in range(self._rows, 0, -1):
            print(str(row) + " ", end="")
            for col in range(self._columns):
                position = self._board[row-1][col]
                print(position if isinstance(position, str) else position._unicode, end="")
                if col < self._rows:
                    print("|", end="")
            if row <= self._rows:
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

    def __init__(self, name, color, coordinates):
        super().__init__(name, color)
        self._move_count = 0
        self._unicode = "\u2659" if self._color == "white" else "\u265F"
        self._coordinates = coordinates

    def valid_moves(self):
        """"""
        possible_moves = []
        print(self._coordinates)
        row_position = self._coordinates[1:]
        col_position = self._coordinates[0]
        print("row pos", row_position)
        if self._move_count == 0:
            possible_moves.append((col_position + str(int(row_position) + 1)) if self._color == "white" else (col_position + str(int(row_position) - 1)))
        return possible_moves


game = ChessVar()
# print(game._chess_pieces)
print(game._chess_pieces["a7"]._coordinates)
print(game._chess_pieces["a7"].valid_moves())
# game.print_board()