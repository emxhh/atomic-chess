from typing import Union


def convert_coordinates_to_board_index(coordinates):
    """Converts algebraic coordinates to board grid index position"""
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
    """Converts board grid index position to algebraic coordinates"""
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
    """A class to represent a player in the atomic chess game.
    Used by the ChessVar class.

    Attributes:
        name: A string that defines the player's name as either Player 1 or Player 2
        color: A string that indicates if the player will be playing white or black chess pieces
    """

    def __init__(self, name: str, color: str):
        """Initializes the instance based on name and color. All data members are private."""
        self._name = name
        self._color = color


class ChessVar:
    """A class to represent a game of atomic chess, played by two players.
    Player 1 always starts first.
    Uses Player class for players' data.
    Uses ChessPiece subclasses to initialize chess pieces on the board.

    Attributes:
        board: A list of lists that each represent a row on the game board.
            Each row list contains list items ordered based on their column on the board.
            The list items are either an empty string to represent an empty square
            or the unicode of a chess piece.
        rows: An integer count of how many rows the board has.
        columns: An integer count of how many columns the board has.
        game_state: A string indicating the current status of the game.
        chess_pieces: A dictionary of all chess pieces currently on the board.
            The keys are algebraic coordinates and the values are the ChessPiece instances.
        players: A dictionary of the 2 players of the game.
        current_player: A string that indicates the color of the current player.
    """

    def __init__(self):
        """Initializes an instance of an atomic chess game. All data members are private.
        Takes no parameters.
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

    def initialize_board(self) -> None:
        """Initializes the game board, places the chess pieces in their starting positions,
        and adds the chess pieces to the chess pieces dictionary.
        """

        # generate blank board
        for row in range(self._rows):
            self._board.append([])
            for col in range(self._columns):
                self._board[row].append(" ")

        # initialize white pawns
        for col in range(self._columns):
            row_index = 1
            coordinates = convert_board_index_to_coordinates([row_index, col])
            pawn = Pawn("pawn", "white", coordinates)
            self._board[row_index][col] = pawn
            self._chess_pieces[coordinates] = pawn

        # initialize black pawns
        for col in range(self._columns):
            row_index = 6
            coordinates = convert_board_index_to_coordinates([row_index, col])
            pawn = Pawn("pawn", "black", coordinates)
            self._board[row_index][col] = pawn
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

        # initialize bishops
        bishop = Bishop("bishop", "white", "c1")
        self._board[0][2] = bishop
        self._chess_pieces[bishop.get_coordinates()] = bishop
        bishop = Bishop("bishop", "white", "f1")
        self._board[0][5] = bishop
        self._chess_pieces[bishop.get_coordinates()] = bishop
        bishop = Bishop("bishop", "black", "c8")
        self._board[7][2] = bishop
        self._chess_pieces[bishop.get_coordinates()] = bishop
        bishop = Bishop("bishop", "black", "f8")
        self._board[7][5] = bishop
        self._chess_pieces[bishop.get_coordinates()] = bishop

        # initialize knights
        knight = Knight("knight", "white", "b1")
        self._board[0][1] = knight
        self._chess_pieces[knight.get_coordinates()] = knight
        knight = Knight("knight", "white", "g1")
        self._board[0][6] = knight
        self._chess_pieces[knight.get_coordinates()] = knight
        knight = Knight("knight", "black", "b8")
        self._board[7][1] = knight
        self._chess_pieces[knight.get_coordinates()] = knight
        knight = Knight("knight", "black", "g8")
        self._board[7][6] = knight
        self._chess_pieces[knight.get_coordinates()] = knight

        # initialize queens
        queen = Queen("queen", "white", "d1")
        self._board[0][3] = queen
        self._chess_pieces[queen.get_coordinates()] = queen
        queen = Queen("queen", "black", "d8")
        self._board[7][3] = queen
        self._chess_pieces[queen.get_coordinates()] = queen

        # initialize kings
        king = King("king", "white", "e1")
        self._board[0][4] = king
        self._chess_pieces[king.get_coordinates()] = king
        king = King("king", "black", "e8")
        self._board[7][4] = king
        self._chess_pieces[king.get_coordinates()] = king

    def print_board(self) -> None:
        """Prints a display of the current state of the game board."""
        print("  a", "b", "c", "d", "e", "f", "g", "h")
        for row in range(self._rows, 0, -1):
            print(str(row) + " ", end="")
            for col in range(self._columns):
                square = self._board[row - 1][col]
                print(square if isinstance(square, str) else square.get_unicode(), end="")
                if col < self._rows:
                    print("|", end="")
            if row <= self._rows:
                print()

    def get_game_state(self) -> str:
        """Returns the game state to indicate if the game is unfinished or if black or white has won."""
        return self._game_state

    def create_player(self, player_name: str, color: str) -> None:
        """Creates a Player instance and stores it in the players dictionary."""
        player = Player(player_name, color)
        self._players[player_name] = player

    def initialize_players(self) -> None:
        """Creates the two players for the game."""
        self.create_player("Player 1", "white")
        self.create_player("Player 2", "black")

    def switch_turns(self) -> None:
        """Switches the current player to the opposing player."""
        if self._current_player == "white":
            self._current_player = "black"
        else:
            self._current_player = "white"

    def is_valid_move(self, chess_piece: "ChessPiece", move_to: str) -> bool:
        """Checks if the move_to coordinates are valid for the chess piece.
        Uses ChessPiece subclasses to get the possible moves.

        Args:
            chess_piece: The ChessPiece instance that we are checking if the move is valid for
            move_to: A string that represents the coordinates of the square moved to
        Returns:
            A boolean to indicate if the move_to square is a valid move
        """
        possible_moves = chess_piece.possible_moves(self._board)
        if move_to in possible_moves:
            return True
        else:
            return False

    def update_board(self, move_from: str, move_to: str) -> None:
        """Updates board with newly made move"""
        current_position = convert_coordinates_to_board_index(move_from)
        self._board[current_position[0]][current_position[1]] = " "
        new_position = convert_coordinates_to_board_index(move_to)
        self._board[new_position[0]][new_position[1]] = self._chess_pieces[move_to]

    def both_kings_killed(self, captured_piece: "ChessPiece") -> bool:
        """Checks if a move would kill both kings in one step"""
        kings_killed = 0
        for square in self.get_surrounding_squares(captured_piece):
            square_is_occupied = (self._board[square[0]][square[1]] != " ")
            if square_is_occupied:
                if self._board[square[0]][square[1]].get_name() == "king":
                    kings_killed += 1
        if captured_piece.get_name() == "king":
            kings_killed += 1
        if kings_killed > 1:
            return True
        else:
            return False

    def remove_battle_pieces(self, attacking_piece: "ChessPiece", captured_piece: "ChessPiece") -> None:
        """Removes attacking and captured pieces"""
        # remove attacking piece
        attacking_piece_position = convert_coordinates_to_board_index(attacking_piece.get_coordinates())
        self._board[attacking_piece_position[0]][attacking_piece_position[1]] = " "
        coordinates = attacking_piece.get_coordinates()
        del self._chess_pieces[coordinates]

        # remove captured piece
        captured_piece_position = convert_coordinates_to_board_index(captured_piece.get_coordinates())
        self._board[captured_piece_position[0]][captured_piece_position[1]] = " "
        coordinates = captured_piece.get_coordinates()

        # if king is captured
        if self._chess_pieces[coordinates].get_name() == "king":
            if self._current_player == "white":
                self._game_state = "WHITE_WON"
            else:
                self._game_state = "BLACK_WON"
        del self._chess_pieces[coordinates]

    @staticmethod
    def get_surrounding_squares(captured_piece) -> list[list[int]]:
        """Returns a list of the surrounding squares of the captured piece"""
        surrounding_squares = []
        captured_piece_position = convert_coordinates_to_board_index(captured_piece.get_coordinates())
        # top 3 squares
        if captured_piece_position[1] - 1 >= 0 and captured_piece_position[0] + 1 < 8:
            surrounding_squares.append([captured_piece_position[0] + 1, captured_piece_position[1] - 1])
        if captured_piece_position[0] + 1 < 8:
            surrounding_squares.append([captured_piece_position[0] + 1, captured_piece_position[1]])
        if captured_piece_position[0] + 1 < 8 and captured_piece_position[1] + 1 < 8:
            surrounding_squares.append([captured_piece_position[0] + 1, captured_piece_position[1] + 1])
        # bottom 3 squares
        if captured_piece_position[0] - 1 >= 0 and captured_piece_position[1] - 1 >= 0:
            surrounding_squares.append([captured_piece_position[0] - 1, captured_piece_position[1] - 1])
        if captured_piece_position[0] - 1 >= 0:
            surrounding_squares.append([captured_piece_position[0] - 1, captured_piece_position[1]])
        if captured_piece_position[0] - 1 >= 0 and captured_piece_position[1] + 1 < 8:
            surrounding_squares.append([captured_piece_position[0] - 1, captured_piece_position[1] + 1])
        # left square
        if captured_piece_position[1] - 1 >= 0:
            surrounding_squares.append([captured_piece_position[0], captured_piece_position[1] - 1])
        # right square
        if captured_piece_position[1] + 1 < 8:
            surrounding_squares.append([captured_piece_position[0], captured_piece_position[1] + 1])
        return surrounding_squares

    def remove_exploded_pieces(self, captured_piece) -> None:
        """Removes exploded chess pieces"""
        surrounding_squares = self.get_surrounding_squares(captured_piece)
        for square in surrounding_squares:
            square_is_occupied = (self._board[square[0]][square[1]] != " ")
            if square_is_occupied:
                square_is_not_pawn = self._board[square[0]][square[1]].get_name() != "pawn"
                if square_is_not_pawn:
                    # if a king is exploding
                    if self._board[square[0]][square[1]].get_name() == "king":
                        if self._current_player == "white":
                            self._game_state = "WHITE_WON"
                        else:
                            self._game_state = "BLACK_WON"
                        self.return_winner()

                    # remove exploding chess pieces
                    self._board[square[0]][square[1]] = " "
                    coordinates = convert_board_index_to_coordinates(square)
                    del self._chess_pieces[coordinates]

    def make_move(self, move_from: str, move_to: str) -> bool:
        """Makes a move for the chess piece in the move_from coordinates to the move_to coordinates.
        Uses ChessPiece to update coordinates.
        """
        # if move_from does not contain a piece belonging to current player, return false
        if move_from not in self._chess_pieces:
            print(f"No chess piece at move_from: {move_from}")
            return False
        if self._chess_pieces[move_from].get_color() != self._current_player:
            print(f"Not current player's piece: {move_from}")
            return False
        # if the move is invalid, return false
        if not self.is_valid_move(self._chess_pieces[move_from], move_to):
            print(f"Invalid move: {move_from} to {move_to}")
            return False
        # if the game_state is won, return false
        if self.get_game_state() == "WHITE_WON" or self.get_game_state() == "BLACK_WON":
            return False

        # make the move
        # if captured piece is the opposing color, remove exploded surrounding pieces and attacking/capturing pieces
        if move_to in self._chess_pieces and self._chess_pieces[move_to].get_color() != self._current_player:
            captured_piece = self._chess_pieces[move_to]
            if self.both_kings_killed(captured_piece):
                return False
            self.remove_battle_pieces(self._chess_pieces[move_from], captured_piece)
            self.remove_exploded_pieces(captured_piece)
        else:
            # update chess_pieces dictionary
            self._chess_pieces[move_from].set_coordinates(move_to)
            self._chess_pieces[move_to] = self._chess_pieces[move_from]
            del self._chess_pieces[move_from]
            # update board with move
            self.update_board(move_from, move_to)
        # switch turns
        self.switch_turns()
        # return true
        return True

    def return_winner(self) -> None:
        """Prints a message indicating the winner of the game."""
        if self._game_state == "WHITE_WON":
            print("Player 1 wins!")
        if self._game_state == "BLACK_WON":
            print("Player 2 wins!")

    def is_game_over(self) -> None:
        """Checks if the game is over."""
        if self._game_state == "UNFINISHED":
            print("Game is unfinished")
        if self._game_state == "WHITE_WON" or self._game_state == "BLACK_WON":
            self.return_winner()


class ChessPiece:
    """A class to represent a chess piece in the atomic chess game. Used by ChessVar.

    Attributes:
        name: A string that labels the name of the chess piece.
        color: A string that labels the chess piece as white or black.
        coordinates: A string that indicates the position of the chess piece on the game board.
        unicode: A string labeling the unicode to represent the chess piece type and color.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, and unicode of the chess piece."""
        self._name = name
        self._color = color
        self._coordinates = coordinates
        self._unicode = ""

    def get_name(self) -> str:
        """Returns the name of the chess piece."""
        return self._name

    def get_color(self) -> str:
        """Returns the color of the chess piece."""
        return self._color

    def get_unicode(self) -> str:
        """Returns unicode of chess piece."""
        return self._unicode

    def get_coordinates(self) -> str:
        """Returns coordinates of chess piece."""
        return self._coordinates

    def set_coordinates(self, coordinates: str) -> None:
        """Updates coordinates of the chess piece."""
        self._coordinates = coordinates

    @staticmethod
    def square_is_empty(board: list[list[[Union[str, "ChessPiece"]]]], square: list[int]):
        """Returns true or false depending on if the square is empty"""
        if board[square[0]][square[1]] == " ":
            return True
        else:
            return False


class Pawn(ChessPiece):
    """A class to represent a pawn chess piece.
    Inherits from ChessPiece.

    Additional Attributes:
        first_move: A boolean determining if it is the Pawn's first move or not.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, unicode,
        and if this is the instance's first move of the chess piece.
        """
        super().__init__(name, color, coordinates)
        self._unicode = "\u2659" if self._color == "white" else "\u265F"
        self._first_move = True

    def set_coordinates(self, coordinates: str) -> None:
        """Updates coordinates and first_move boolean of the pawn.
        Overrides parent method.
        """
        self._coordinates = coordinates
        self._first_move = False

    def possible_moves(self, board: list[list[[Union[str, ChessPiece]]]]) -> list[str]:
        """Retrieves possible moves that the instance of Pawn can make from its current position.

        Args:
            board: A list that represents the current state of the game board.

        Returns:
            A list of the instance's possible moves. Each move is represented by its algebraic coordinates.
        """
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)

        # forward steps
        # pawn can move forward 1 square
        forward_step = 1 if self._color == "white" else -1
        forward_square = [current_position[0] + forward_step, current_position[1]]
        square_coordinates = convert_board_index_to_coordinates(forward_square)
        if self.square_is_empty(board, forward_square):
            possible_moves.append(square_coordinates)
        # if the pawn's first move, pawn can move forward 2 squares
        if self._first_move:
            forward_step *= 2
            forward_square = [current_position[0] + forward_step, current_position[1]]
            square_coordinates = convert_board_index_to_coordinates(forward_square)
            if self.square_is_empty(board, forward_square):
                possible_moves.append(square_coordinates)

        # capturing a chess piece steps
        if self._color == "white":
            # check diagonal up left square
            diagonal_up_left_square = [current_position[0] + 1, current_position[1] - 1]
            if diagonal_up_left_square[0] < 8 and diagonal_up_left_square[1] >= 0:
                if not self.square_is_empty(board, diagonal_up_left_square):
                    square_coordinates = convert_board_index_to_coordinates(diagonal_up_left_square)
                    possible_moves.append(square_coordinates)
            # check diagonal up right square
            diagonal_up_right_square = [current_position[0] + 1, current_position[1] + 1]
            if diagonal_up_right_square[0] < 8 and diagonal_up_right_square[1] < 8:
                if not self.square_is_empty(board, diagonal_up_right_square):
                    square_coordinates = convert_board_index_to_coordinates(diagonal_up_right_square)
                    possible_moves.append(square_coordinates)
        if self._color == "black":
            # check diagonal down left square
            diagonal_left_down_square = [current_position[0] - 1, current_position[1] - 1]
            if diagonal_left_down_square[0] >= 0 and diagonal_left_down_square[1] >= 0:
                if not self.square_is_empty(board, diagonal_left_down_square):
                    square_coordinates = convert_board_index_to_coordinates(diagonal_left_down_square)
                    possible_moves.append(square_coordinates)
            # check diagonal down right square
            diagonal_down_right_square = [current_position[0] - 1, current_position[1] + 1]
            if diagonal_down_right_square[0] >= 0 and diagonal_down_right_square[1] < 8:
                if not self.square_is_empty(board, diagonal_down_right_square):
                    square_coordinates = convert_board_index_to_coordinates(diagonal_down_right_square)
                    possible_moves.append(square_coordinates)

        return possible_moves


class Bishop(ChessPiece):
    """A class to represent a bishop chess piece.
    Inherits from ChessPiece.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, and unicode of the chess piece."""
        super().__init__(name, color, coordinates)
        self._unicode = "\u2657" if self._color == "white" else "\u265D"

    def possible_moves(self, board: list[list[[Union[str, ChessPiece]]]]) -> list[str]:
        """Retrieves possible moves that the instance of Bishop can make from its current position.

        Args:
            board: A list that represents the current state of the game board.

        Returns:
            A list of the instance's possible moves. Each move is represented by its algebraic coordinates.
        """
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)

        # check continuous diagonal up left squares
        diagonal_up_left_moves = []
        end = max(8 - current_position[0], current_position[1] + 1)
        for step in range(1, end):
            square = [current_position[0] + step, current_position[1] - step]
            if square[0] < 8 and square[1] >= 0:
                if self.square_is_empty(board, square):
                    diagonal_up_left_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        diagonal_up_left_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += diagonal_up_left_moves

        # check continuous diagonal up right squares
        diagonal_up_right_moves = []
        end = max(8 - current_position[0], 8 - current_position[1])
        for step in range(1, end):
            square = [current_position[0] + step, current_position[1] + step]
            if square[0] < 8 and square[1] < 8:
                if self.square_is_empty(board, square):
                    diagonal_up_right_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        diagonal_up_right_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += diagonal_up_right_moves

        # check continuous diagonal down left squares
        diagonal_down_left_moves = []
        end = max(current_position[0] + 1, current_position[1] + 1)
        for step in range(1, end):
            square = [current_position[0] - step, current_position[1] - step]
            if square[0] >= 0 and square[1] >= 0:
                if self.square_is_empty(board, square):
                    diagonal_down_left_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        diagonal_down_left_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += diagonal_down_left_moves

        # check continuous diagonal down right squares
        diagonal_down_right_moves = []
        end = max(current_position[0] + 1, 8 - current_position[1])
        for step in range(1, end):
            square = [current_position[0] - step, current_position[1] + step]
            if square[0] >= 0 and square[1] < 8:
                if self.square_is_empty(board, square):
                    diagonal_down_right_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        diagonal_down_right_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += diagonal_down_right_moves

        return possible_moves


class Knight(ChessPiece):
    """A class to represent a knight chess piece.
    Inherits from ChessPiece.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, and unicode of the chess piece."""
        super().__init__(name, color, coordinates)
        self._unicode = "\u2658" if self._color == "white" else "\u265E"

    def possible_moves(self, board: list[list[[Union[str, ChessPiece]]]]) -> list[str]:
        """Retrieves possible moves that the instance of Knight can make from its current position.

        Args:
            board: A list that represents the current state of the game board.

        Returns:
            A list of the instance's possible moves. Each move is represented by its algebraic coordinates.
        """
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)
        possible_steps = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for step in possible_steps:
            square = [current_position[0] + step[0], current_position[1] + step[1]]
            if 0 <= square[0] < 8 and 0 <= square[1] < 8:
                if not self.square_is_empty(board, square):
                    if board[square[0]][square[1]].get_color() != self._color:
                        possible_moves.append(convert_board_index_to_coordinates(square))
                else:
                    possible_moves.append(convert_board_index_to_coordinates(square))
        return possible_moves


class Rook(ChessPiece):
    """A class to represent a rook chess piece.
    Inherits from ChessPiece.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, and unicode of the chess piece."""
        super().__init__(name, color, coordinates)
        self._unicode = "\u2656" if self._color == "white" else "\u265C"

    def possible_moves(self, board: list[list[[Union[str, ChessPiece]]]]) -> list[str]:
        """Retrieves possible moves that the instance of Rook can make from its current position.

        Args:
            board: A list that represents the current state of the game board.

        Returns:
            A list of the instance's possible moves. Each move is represented by its algebraic coordinates.
        """
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)

        # check continuous left moves
        left_moves = []
        for step in range(1, current_position[1] + 1):
            square = [current_position[0], current_position[1] - step]
            if square[1] >= 0:
                if self.square_is_empty(board, square):
                    left_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        left_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += left_moves

        # check continuous right moves
        right_moves = []
        for step in range(1, 8 - current_position[1]):
            square = [current_position[0], current_position[1] + step]
            if square[1] < 8:
                if self.square_is_empty(board, square):
                    right_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        right_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += right_moves

        # check continuous up moves
        up_moves = []
        for step in range(1, 8 - current_position[0]):
            square = [current_position[0] + step, current_position[1]]
            if square[0] < 8:
                if self.square_is_empty(board, square):
                    up_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        up_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += up_moves

        # check continuous down moves
        down_moves = []
        for step in range(1, current_position[0] + 1):
            square = [current_position[0] - step, current_position[1]]
            if square[0] >= 0:
                if self.square_is_empty(board, square):
                    down_moves.append(convert_board_index_to_coordinates(square))
                else:
                    if board[square[0]][square[1]].get_color() != self._color:
                        down_moves.append(convert_board_index_to_coordinates(square))
                    break
        possible_moves += down_moves

        return possible_moves


class Queen(ChessPiece):
    """A class to represent a queen chess piece.
    Inherits from ChessPiece.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, and unicode of the chess piece."""
        super().__init__(name, color, coordinates)
        self._unicode = "\u2655" if self._color == "white" else "\u265B"

    def possible_moves(self, board: list[list[[Union[str, ChessPiece]]]]) -> list[str]:
        """Retrieves possible moves that the instance of Queen can make from its current position.

        Args:
            board: A list that represents the current state of the game board.

        Returns:
            A list of the instance's possible moves. Each move is represented by its algebraic coordinates.
        """
        possible_moves = []
        rook_temp = Rook("rook", self._color, self._coordinates)
        bishop_temp = Bishop("bishop", self._color, self._coordinates)
        possible_moves += rook_temp.possible_moves(board)
        possible_moves += bishop_temp.possible_moves(board)
        return possible_moves


class King(ChessPiece):
    """A class to represent a king chess piece.
    Inherits from ChessPiece.
    """

    def __init__(self, name: str, color: str, coordinates: str) -> None:
        """Initializes the instance based on name, color, coordinates, and unicode of the chess piece."""
        super().__init__(name, color, coordinates)
        self._unicode = "\u2654" if self._color == "white" else "\u265A"

    def possible_moves(self, board: list[list[[Union[str, ChessPiece]]]]) -> list[str]:
        """Retrieves possible moves that the instance of King can make from its current position.

        Args:
            board: A list that represents the current state of the game board.

        Returns:
            A list of the instance's possible moves. Each move is represented by its algebraic coordinates.
        """
        possible_moves = []
        current_position = convert_coordinates_to_board_index(self._coordinates)
        possible_steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for step in possible_steps:
            square = [current_position[0] + step[0], current_position[1] + step[1]]
            if 0 <= square[0] < 8 and 0 <= square[1] < 8:
                square_is_empty = board[square[0]][square[1]] == " "
                if square_is_empty:
                    possible_moves.append(convert_board_index_to_coordinates(square))
        return possible_moves
