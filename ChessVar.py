# Author: Emily Ho
# Github username: emxhh
# Date: 5/28/24
# Description: Atomic chess game

def convert_coordinates_to_board_index(coordinates):
    """Converts algebraic coordinates to board grid list index positions"""
    column_dict = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    row_index = int(coordinates[1]) - 1
    col_index = column_dict[coordinates[0]]
    board_index_position = [row_index, col_index]
    return board_index_position


def convert_board_index_to_coordinates(board_index):
    """Converts board index to algebraic coordinates"""
    column_dict = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }
    col_coordinate = column_dict[board_index[1]]
    row_coordinate = str(board_index[0] + 1)
    coordinates = col_coordinate + row_coordinate
    return coordinates


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
        Initializes an instance of an atomic chess game. Takes no parameters.
        """
        self._board = []
        self._rows = 8
        self._columns = self._rows
        self._game_state = "UNFINISHED"
        self._chess_pieces = {}
        self._players = {}
        self._current_player = "white"
        self.initialize_board()
        self.initialize_players()

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

        # initialize rooks
        rook = Rook("rook", "white", "a1")
        self._board[0][0] = rook
        self._chess_pieces[rook.get_coordinates()] = rook
        rook = Rook("rook", "white", "h1")
        self._board[0][7] = rook
        self._chess_pieces[rook.get_coordinates()] = rook
        rook = Rook("rook", "black", "a8")
        self._board[7][0] = rook
        self._chess_pieces[rook.get_coordinates()] = rook
        rook = Rook("rook", "black", "h8")
        self._board[7][7] = rook
        self._chess_pieces[rook.get_coordinates()] = rook

    def print_board(self):
        """Prints the current state of the game board."""
        print("  a", "b", "c", "d", "e", "f", "g", "h")
        for row in range(self._rows, 0, -1):
            print(str(row) + " ", end="")
            for col in range(self._columns):
                position = self._board[row - 1][col]
                print(position if isinstance(position, str) else position.get_unicode(), end="")
                if col < self._rows:
                    print("|", end="")
            if row <= self._rows:
                print()

    def get_game_state(self):
        """Returns the game state to indicate if the game is unfinished or if black or white has won."""
        return self._game_state

    def create_player(self, player_name, color):
        """Creates a Player instance and stores it in the players dictionary."""
        player = Player(player_name, color)
        self._players[player_name] = player

    def initialize_players(self):
        """Creates the two players for the game."""
        self.create_player("Player 1", "white")
        self.create_player("Player 2", "black")

    def switch_turns(self):
        """Switches the current player to the opposing player."""
        if self._current_player == "white":
            self._current_player = "black"
        else:
            self._current_player = "white"

    def is_valid_move(self, chess_piece, move_to):
        """
        Checks if the move_to coordinates are valid for the chess piece.
        Uses ChessPiece subclasses to get the possible moves.
        """
        possible_moves = chess_piece.possible_moves(self._board)
        if move_to in possible_moves:
            return True
        else:
            return False

    def update_board(self, move_from, move_to):
        """Updates board with newly made move"""
        current_position = convert_coordinates_to_board_index(move_from)
        self._board[current_position[0]][current_position[1]] = " "
        new_position = convert_coordinates_to_board_index(move_to)
        self._board[new_position[0]][new_position[1]] = self._chess_pieces[move_to]

    def remove_exploded_pieces(self, captured_piece):
        """Removes exploded chess pieces"""
        surrounding_squares = []
        captured_piece_position = convert_coordinates_to_board_index(captured_piece.get_coordinates())
        surrounding_squares.append([captured_piece_position[0] + 1, captured_piece_position[1] - 1])
        surrounding_squares.append([captured_piece_position[0] + 1, captured_piece_position[1]])
        surrounding_squares.append([captured_piece_position[0] + 1, captured_piece_position[1] + 1])
        surrounding_squares.append([captured_piece_position[0] - 1, captured_piece_position[1] - 1])
        surrounding_squares.append([captured_piece_position[0] - 1, captured_piece_position[1]])
        surrounding_squares.append([captured_piece_position[0] - 1, captured_piece_position[1] + 1])

        for square in surrounding_squares:
            square_is_occupied = (self._board[square[0]][square[1]] != " ")
            if square_is_occupied:
                square_is_not_pawn = self._board[square[0]][square[1]].get_name() != "pawn"
                if square_is_not_pawn:
                    self._board[square[0]][square[1]] = " "
                    coordinates = convert_board_index_to_coordinates(square)
                    del self._chess_pieces[coordinates]

    def make_move(self, move_from, move_to):
        """
        Makes a move for the chess piece in the move_from coordinates to the move_to coordinates.
        Uses ChessPiece to update coordinates.
        """
        # print("chess dict", self._chess_pieces)
        # if move_from does not contain a piece belonging to current player, return false
        if self._chess_pieces[move_from].get_color() != self._current_player:
            return False
        if move_from not in self._chess_pieces:
            return False
        # if the move is invalid, return false
        if not self.is_valid_move(self._chess_pieces[move_from], move_to):
            print('invalid move')
            return False
        # if the game_state is won, return false
        if self.get_game_state() == "WHITE_WON" or self.get_game_state() == "BLACK_WON":
            return False
        # make the move
        # if captured piece is the opposing color, then remove exploded pieces
        if move_to in self._chess_pieces and self._chess_pieces[move_to].get_color() != self._current_player:
            self.remove_exploded_pieces(self._chess_pieces[move_to])

        # update chess_pieces dictionary
        self._chess_pieces[move_from].set_coordinates(move_to)
        self._chess_pieces[move_to] = self._chess_pieces[move_from]
        del self._chess_pieces[move_from]
        # update board with move
        self.update_board(move_from, move_to)

        # update game_state if necessary
        # switch turns
        self.switch_turns()
        # return true
        return True

    def return_winner(self):
        """Determines and returns the winner of the game based on the current board state."""
        pass

    def is_game_over(self):
        """Checks if the game is over."""
        pass


class ChessPiece:
    """
    A class to represent a chess piece in the atomic chess game. Used by ChessVar.

    Attributes:
        name: A string that labels the name of the chess piece
        color: A string that labels the chess piece as white or black
        coordinates: A string that indicates the position of the chess piece on the game board
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        self._name = name
        self._color = color
        self._coordinates = coordinates
        self._unicode = ""

    def get_name(self):
        """Returns the name of the chess piece"""
        return self._name

    def get_color(self):
        """Returns the color of the chess piece"""
        return self._color

    def get_unicode(self):
        """Returns unicode of chess piece"""
        return self._unicode

    def get_coordinates(self):
        """Returns chess piece coordinates"""
        return self._coordinates

    def set_coordinates(self, coordinates):
        """Updates coordinates of the chess piece."""
        self._coordinates = coordinates


class Pawn(ChessPiece):
    """
    A class to represent a pawn chess piece.
    Inherits from Chess Piece.
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        super().__init__(name, color, coordinates)
        self._move_count = 0
        self._unicode = "\u2659" if self._color == "white" else "\u265F"

    def set_coordinates(self, coordinates):
        """Updates coordinates of the chess piece."""
        self._coordinates = coordinates
        self._move_count += 1

    def possible_moves(self, board):
        """Returns a list of possible moves for the pawn from on its current position."""
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)

        # add all possible moves
        if self._color == "white":
            # 1 square forward
            forward_coordinates = convert_board_index_to_coordinates([current_position[0] + 1, current_position[1]])
            possible_moves.append(forward_coordinates)
            # check diagonal up left
            diagonal_left = [current_position[0] + 1, current_position[1] - 1]
            square_is_occupied = (board[diagonal_left[0]][diagonal_left[1]] != " ")
            if square_is_occupied:
                diagonal_left_coordinates = convert_board_index_to_coordinates(diagonal_left)
                possible_moves.append(diagonal_left_coordinates)
            # check diagonal up right
            diagonal_right = [current_position[0] + 1, current_position[1] + 1]
            square_is_occupied = (board[diagonal_right[0]][diagonal_right[1]] != " ")
            if square_is_occupied:
                diagonal_right_coordinates = convert_board_index_to_coordinates(diagonal_right)
                possible_moves.append(diagonal_right_coordinates)
        if self._color == "black":
            # 1 square forward
            forward_coordinates = convert_board_index_to_coordinates([current_position[0] - 1, current_position[1]])
            possible_moves.append(forward_coordinates)
            # check diagonal down left
            diagonal_left = [current_position[0] - 1, current_position[1] - 1]
            square_is_occupied = (board[diagonal_left[0]][diagonal_left[1]] != " ")
            if square_is_occupied:
                diagonal_left_coordinates = convert_board_index_to_coordinates(diagonal_left)
                possible_moves.append(diagonal_left_coordinates)
            # check diagonal down right
            diagonal_right = [current_position[0] - 1, current_position[1] + 1]
            if diagonal_right[1] < 8:
                square_is_occupied = (board[diagonal_right[0]][diagonal_right[1]] != " ")
                if square_is_occupied:
                    diagonal_right_coordinates = convert_board_index_to_coordinates(diagonal_right)
                    possible_moves.append(diagonal_right_coordinates)

        if self._move_count == 0:
            if self._color == "white":
                # 2 squares forward
                forward_coordinates = convert_board_index_to_coordinates([current_position[0] + 2, current_position[1]])
                possible_moves.append(forward_coordinates)
            if self._color == "black":
                forward_coordinates = convert_board_index_to_coordinates([current_position[0] - 2, current_position[1]])
                possible_moves.append(forward_coordinates)

        # check in possible moves if there is a chess piece in front of the current chess piece
        # print('all poss moves', self._coordinates, self._color, possible_moves)
        for possible_next_move in possible_moves:
            possible_next_move_position = convert_coordinates_to_board_index(possible_next_move)
            if self._color == "white":
                chess_piece_in_front_position = [current_position[0] + 1, current_position[1]]
                square_in_front_is_occupied = (
                        board[chess_piece_in_front_position[0]][chess_piece_in_front_position[1]] != " ")
                if possible_next_move_position == chess_piece_in_front_position and square_in_front_is_occupied:
                    possible_moves.remove(possible_next_move)
            if self._color == "black":
                chess_piece_in_front_position = [current_position[0] - 1, current_position[1]]
                square_in_front_is_occupied = (
                        board[chess_piece_in_front_position[0]][chess_piece_in_front_position[1]] != " ")
                if possible_next_move_position == chess_piece_in_front_position and square_in_front_is_occupied:
                    possible_moves.remove(possible_next_move)
        # print('new poss moves', self._coordinates, self._color, possible_moves)

        return possible_moves


class Bishop(ChessPiece):
    """
    A class to represent a bishop chess piece.
    Inherits from Chess Piece.
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        super().__init__(name, color, coordinates)

    def possible_moves(self):
        """Returns a list of possible moves for the bishop from on its current position."""
        possible_moves = []


class Knight(ChessPiece):
    """
    A class to represent a knight chess piece.
    Inherits from Chess Piece.
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        super().__init__(name, color, coordinates)

    def possible_moves(self):
        """Returns a list of possible moves for the knight from on its current position."""
        possible_moves = []


class Rook(ChessPiece):
    """
    A class to represent a rook chess piece.
    Inherits from Chess Piece.
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        super().__init__(name, color, coordinates)
        self._unicode = "\u2656" if self._color == "white" else "\u265C"

    def possible_moves(self, board):
        """Returns a list of possible moves for the rook from on its current position."""
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)

        # move left
        left_moves = []
        left_square = [current_position[0], current_position[1] - 1]
        if left_square[1] >= 0:
            square_is_empty = board[left_square[0]][left_square[1]] == " "
            while square_is_empty:
                left_moves.append(convert_board_index_to_coordinates(left_square))
                left_square[1] -= 1
                square_is_empty = board[left_square[0]][left_square[1]] == " "
            left_moves.append(convert_board_index_to_coordinates(left_square))
        possible_moves += left_moves

        # move right
        right_moves = []
        right_square = [current_position[0], current_position[1] + 1]
        if right_square[1] < 8:
            square_is_empty = board[right_square[0]][right_square[1]] == " "
            while square_is_empty:
                right_moves.append(convert_board_index_to_coordinates(right_square))
                right_square[1] += 1
                square_is_empty = board[right_square[0]][right_square[1]] == " "
            right_moves.append(convert_board_index_to_coordinates(right_square))
        possible_moves += right_moves

        # move up
        up_moves = []
        up_square = [current_position[0] + 1, current_position[1]]
        if up_square[0] < 8:
            square_is_empty = board[up_square[0]][up_square[1]] == " "
            while square_is_empty:
                up_moves.append(convert_board_index_to_coordinates(up_square))
                up_square[0] += 1
                square_is_empty = board[up_square[0]][up_square[1]] == " "
            up_moves.append(convert_board_index_to_coordinates(up_square))
        possible_moves += up_moves

        # move down
        down_moves = []
        down_square = [current_position[0] - 1, current_position[1]]
        if down_square[0] >= 0:
            square_is_empty = board[down_square[0]][down_square[1]] == " "
            while square_is_empty:
                down_moves.append(convert_board_index_to_coordinates(down_square))
                down_square[0] -= 1
                square_is_empty = board[down_square[0]][down_square[1]] == " "
            down_moves.append(convert_board_index_to_coordinates(down_square))
        possible_moves += down_moves

        print(possible_moves)
        return possible_moves



class Queen(ChessPiece):
    """
    A class to represent a queen chess piece.
    Inherits from Chess Piece.
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        super().__init__(name, color, coordinates)

    def possible_moves(self):
        """Returns a list of possible moves for the queen from on its current position."""
        possible_moves = []


class King(ChessPiece):
    """
    A class to represent a king chess piece.
    Inherits from Chess Piece.
    """

    def __init__(self, name, color, coordinates):
        """Initializes the instance based on name, color, and coordinates of the chess piece."""
        super().__init__(name, color, coordinates)

    def possible_moves(self):
        """Returns a list of possible moves for the king from on its current position"""
        possible_moves = []


# game = ChessVar()
# game.make_move("a2", "a4")  # white
# game.make_move("h7", "h5")  # black
# game.make_move("c2", "c4")  # white
# game.make_move("h5", "h4")  # black
# game.make_move("d2", "d4")  # white
# game.make_move("b7", "b5")  # black
# game.make_move("a1", "a3")  # white
# game.make_move("h8", "h6")  # black
# game.make_move("a3", "b3")  # white
# game.print_board()
