# Author: Emily Ho
# Github username: emxhh
# Date: 5/28/24
# Description: Atomic chess game

class Player:
    """
    A class to represent a player in the atomic chess game.
    Used by the ChessVar class.

    Attributes:
        name: A string that labels the player name
        color: A string that indicates if the player will be playing the white or black chess pieces
    """

    def __init__(self, name, color):
        """
        Initializes the instance based on name and color. All data members are private.

        Args:
            name: Defines the player's name
            color: Defines the color of the player's chess pieces of either white or black
        """
        self._name = name
        self._color = color


class ChessVar:
    """
    A class to represent a game of atomic chess, played by two players.
    Player 1 always starts first.
    Uses Player class for players' data
    """

    def __init__(self):
        """
        Initializes an instance of an atomic chess game.
        Takes no parameters.
        Initializes the board and places initial pieces in correct positions.
        All data members are private
        """
        self._board = []
        self._rows = 8
        self._columns = self._rows
        self._game_state = "UNFINISHED"
        self._chess_pieces = {}
        self.initialize_board()

    def initialize_board(self):
        """Initializes the game board and places the chess pieces in their starting positions."""
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
        """Prints the current state of the game board."""
        print("  a", "b", "c", "d", "e", "f", "g", "h")
        for row in range(self._rows, 0, -1):
            print(str(row) + " ", end="")
            for col in range(self._columns):
                position = self._board[row - 1][col]
                print(position if isinstance(position, str) else position._unicode, end="")
                if col < self._rows:
                    print("|", end="")
            if row <= self._rows:
                print("\n")

    def get_game_state(self):
        """Returns the game state to indicate if the game is unfinished or if black or white has won"""
        return self._game_state

    def is_valid_move(self, chess_piece, move_to):
        """Checks if the move_to coordinates are valid for the chess piece"""
        possible_moves = chess_piece.possible_moves()
        if move_to in possible_moves:
            return True
        else:
            return False

    def make_move(self, move_from, move_to):
        """Makes a move for the chess piece in the move_from coordinates to the move_to coordinates"""
        # if move_from does not have the player's piece, return false
        if move_from not in self._chess_pieces:
            return False
        # if the move is invalid, return false
        if not self.is_valid_move(self._chess_pieces[move_from], move_to):
            return False
        # if the game_state is won, return false
        if self.get_game_state() == "WHITE_WON" or self.get_game_state() == "BLACK_WON":
            return False
        # make the move
        # update chess_pieces dictionary
        self._chess_pieces[move_from].set_coordinates(move_to)
        self._chess_pieces[move_to] = self._chess_pieces[move_from]
        del self._chess_pieces[move_from]
        # update board with move
        col_coordinate = move_from[0]
        row_coordinate = move_from[1:]
        col_position = ord(col_coordinate) - 97
        row_position = row_coordinate - 1
        self._board[col_position][row_position] = " "
        col_coordinate = move_to[0]
        row_coordinate = move_to[1:]
        col_position = ord(col_coordinate) - 97
        row_position = row_coordinate - 1
        self._board[col_position][row_position] = self._chess_pieces[move_to]._unicode

        # remove exploded pieces
        # update game_state if necessary
        # return true
        return True


class ChessPiece:
    """
    A class to represent a chess piece in the atomic chess game. Used by ChessVar

    Attributes:
        name: A string that labels the name of the chess piece
        color: A string that labels the chess piece as white or black
        coordinates: A string that indicates the position of the chess piece on the game board
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece"""
        self._name = name
        self._color = color
        self._coordinates = coordinates

    def set_coordinates(self, coordinates):
        """Updates coordinates of the chess piece"""
        self._coordinates = coordinates


class Pawn(ChessPiece):
    """
    A class to represent a pawn chess piece.
    Inherits from Chess Piece
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece"""
        super().__init__(name, color, coordinates)
        self._move_count = 0
        self._unicode = "\u2659" if self._color == "white" else "\u265F"

    def possible_moves(self):
        """Returns a list of possible moves for the pawn from on its current position"""
        possible_moves = []
        row_position = self._coordinates[1:]
        col_position = self._coordinates[0]

        if self._color == "white":
            possible_moves.append(col_position + str(int(row_position) + 1))
        else:
            possible_moves.append(col_position + str(int(row_position) - 1))
        if self._move_count == 0:
            possible_moves.append((col_position + str(int(row_position) + 2)) if self._color == "white" else (
                    col_position + str(int(row_position) - 2)))
        return possible_moves


game = ChessVar()
# print(game._chess_pieces)
# print(game._chess_pieces["a7"]._coordinates)
# print(game._chess_pieces["a7"].possible_moves())
# game.print_board()
