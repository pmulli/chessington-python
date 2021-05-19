"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def is_piece_in_front(self, board):
        current_square = board.find_piece(self)
        piece_in_front = None
        if self.player == Player.WHITE:
            square_in_front = Square.at(current_square.row+1,current_square.col)
            piece_in_front = board.get_piece(square_in_front)
        elif self.player == Player.BLACK:
            square_in_front = Square.at(current_square.row-1,current_square.col)
            piece_in_front = board.get_piece(square_in_front)
        return piece_in_front != None

    def is_piece_at_end_of_board(self, board):
        current_square = board.find_piece(self)
        return (self.player == Player.WHITE and current_square.row == 7) or (self.player == Player.BLACK and current_square.row == 0)

    def can_capture_diagonally_left(self, board):
        current_square = board.find_piece(self)
        if self.player == Player.WHITE:
            square_diagonally_left = Square.at(current_square.row+1,current_square.col-1)
            piece_diagonally_left = board.get_piece(square_diagonally_left)
            if piece_diagonally_left != None and piece_diagonally_left.player == Player.BLACK:
                return True
        elif self.player == Player.BLACK:
            square_diagonally_left = Square.at(current_square.row-1,current_square.col+1)
            piece_diagonally_left = board.get_piece(square_diagonally_left)
            if piece_diagonally_left != None and piece_diagonally_left.player == Player.WHITE:
                return True

        return False
    
    def can_capture_diagonally_right(self, board):
        current_square = board.find_piece(self)
        if self.player == Player.WHITE:
            square_diagonally_right = Square.at(current_square.row+1,current_square.col+1)
            piece_diagonally_right = board.get_piece(square_diagonally_right)
            if piece_diagonally_right != None and piece_diagonally_right.player == Player.BLACK:
                return True
        elif self.player == Player.BLACK:
            square_diagonally_right = Square.at(current_square.row-1,current_square.col-1)
            piece_diagonally_right = board.get_piece(square_diagonally_right)
            if piece_diagonally_right != None and piece_diagonally_right.player == Player.WHITE:
                return True

        return False
    
    def get_available_moves(self, board):
        moves = []

        if not self.is_piece_at_end_of_board(board):
            current_square = board.find_piece(self)

            if not self.is_piece_in_front(board):
                if self.player == Player.WHITE:
                    moves.append(Square.at(current_square.row+1,current_square.col))
                    if current_square.row == 1:
                        moves.append(Square.at(current_square.row+2,current_square.col))
                elif self.player == Player.BLACK:
                    moves.append(Square.at(current_square.row-1,current_square.col))
                    if current_square.row == 6:
                        moves.append(Square.at(current_square.row-2,current_square.col))
            
            if self.can_capture_diagonally_left(board):
                if self.player == Player.WHITE:
                    moves.append(Square.at(current_square.row+1,current_square.col-1))
                elif self.player == Player.BLACK:
                    moves.append(Square.at(current_square.row-1,current_square.col+1))

            if self.can_capture_diagonally_right(board):
                if self.player == Player.WHITE:
                    moves.append(Square.at(current_square.row+1,current_square.col+1))
                elif self.player == Player.BLACK:
                    moves.append(Square.at(current_square.row-1,current_square.col-1))

        return moves



class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []