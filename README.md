# Atomic Chess

This Python project provides a framework for playing Atomic Chess, allowing users to simulate this exciting chess variant programmatically. The provided methods enable game state management, move validation, and board visualization, making it a comprehensive tool for both casual play and testing.

## Getting Started

To utilize this project, ensure you have Python installed on your system. Clone this repository and run the provided Python scripts.

## Prerequisites

This project requires Python 3.8+ installed on your system.

## Rules of Atomic Chess
Atomic Chess retains the basic movement rules of standard chess but includes the following special rules:
1. **Explosions**: When a piece is captured, all pieces (except pawns) on the 8 surrounding squares are also removed from the board.
2. **Suicidal Captures**: The capturing piece is also removed in the explosion.
3. **King Captures**: The king cannot capture pieces. Capturing a king ends the game. A move that would result in both kings being captured simultaneously is not allowed.
4. **Pawn Capture Exception**: Pawns can only be removed if directly involved in a capture.
5. **No Check or Checkmate**: The game is won by capturing the opponent's king.

## Classes and Descriptions

### `ChessVar`
Represents a game of Atomic Chess played between two players. It initializes the game board, manages players, validates moves, updates game state, and handles piece explosions upon captures.

### `Player`
Represents a player in the atomic chess game. Stores the player's name ("Player 1" or "Player 2") and color ("white" or "black").

### `ChessPiece`
Base class for all chess pieces. Provides common attributes and methods for chess pieces, including coordinates on the board and movement validations.

### `Pawn`
Subclass of `ChessPiece` representing a pawn on the chessboard. Implements specific pawn movement rules, including two-square first moves and capture mechanics.

### `Rook`
Subclass of `ChessPiece` representing a rook on the chessboard. Implements specific rook movement rules along rows and columns.

### `Bishop`
Subclass of `ChessPiece` representing a bishop on the chessboard. Implements specific bishop movement rules along diagonals.

### `Knight`
Subclass of `ChessPiece` representing a knight on the chessboard. Implements specific knight movement rules in an L-shape pattern.

### `Queen`
Subclass of `ChessPiece` representing a queen on the chessboard. Combines movement rules of rooks and bishops, allowing movement along rows, columns, and diagonals.

### `King`
Subclass of `ChessPiece` representing a king on the chessboard. Implements specific king movement rules, including castling, and is pivotal in determining game state.

## Implementation Details
- **Private Data Members**: All data members of the `ChessVar` class are private to ensure encapsulation and proper state management.
- **Class Interactions**: The `ChessVar` class interacts with instances of `Player` and various subclasses of `ChessPiece` to manage gameplay mechanics, validate moves, and handle game state changes.