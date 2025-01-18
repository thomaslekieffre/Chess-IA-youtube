from typing import List, Tuple
from src.utils.constants import *
from src.utils.move import Move

class MoveGenerator:
    def __init__(self, board):
        self.board = board
        
    def get_legal_moves(self, row: int, col: int) -> List[Move]:
        """Retourne tous les coups légaux pour une pièce donnée"""
        piece_type, color = self.board.get_piece(row, col)
        if piece_type is None:
            return []
            
        if piece_type == PAWN:
            return self._get_pawn_moves(row, col, color)
        elif piece_type == KNIGHT:
            return self._get_knight_moves(row, col, color)
        elif piece_type == BISHOP:
            return self._get_bishop_moves(row, col, color)
        elif piece_type == ROOK:
            return self._get_rook_moves(row, col, color)
        elif piece_type == QUEEN:
            return self._get_queen_moves(row, col, color)
        elif piece_type == KING:
            return self._get_king_moves(row, col, color)
            
        return []
        
    def _get_pawn_moves(self, row: int, col: int, color: int) -> List[Move]:
        moves = []
        direction = 1 if color == WHITE else -1
        start_row = 1 if color == WHITE else 6
        
        # Avancée simple
        new_row = row + direction
        if self.board.is_valid_position(new_row, col) and \
           self.board.get_piece(new_row, col)[0] is None:
            moves.append(Move((row, col), (new_row, col), PAWN))
            
            # Avancée double depuis la position initiale
            if row == start_row:
                new_row = row + 2 * direction
                if self.board.get_piece(new_row, col)[0] is None:
                    moves.append(Move((row, col), (new_row, col), PAWN))
        
        # Captures en diagonale
        new_row = row + direction
        for col_offset in [-1, 1]:
            new_col = col + col_offset
            if self.board.is_valid_position(new_row, new_col):
                target_piece, target_color = self.board.get_piece(new_row, new_col)
                if target_piece is not None and target_color != color:
                    moves.append(Move((row, col), (new_row, new_col), PAWN))
                    
        return moves

    def _get_knight_moves(self, row: int, col: int, color: int) -> List[Move]:
        moves = []
        # Les 8 mouvements possibles du cavalier
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        for row_offset, col_offset in knight_moves:
            new_row = row + row_offset
            new_col = col + col_offset
            
            if self.board.is_valid_position(new_row, new_col):
                target_piece, target_color = self.board.get_piece(new_row, new_col)
                if target_piece is None or target_color != color:
                    moves.append(Move((row, col), (new_row, new_col), KNIGHT))
                    
        return moves

    def _get_bishop_moves(self, row: int, col: int, color: int) -> List[Move]:
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales du fou

        for row_dir, col_dir in directions:
            new_row = row + row_dir
            new_col = col + col_dir

            while self.board.is_valid_position(new_row, new_col):
                target_piece, target_color = self.board.get_piece(new_row, new_col)

                if target_piece is None:
                    moves.append(Move((row, col), (new_row, new_col), BISHOP))
                elif target_color != color:
                    moves.append(Move((row, col), (new_row, new_col), BISHOP))
                    break
                else:
                    break  # On sort si on rencontre une pièce de notre couleur

                new_row += row_dir
                new_col += col_dir

        return moves

    def _get_rook_moves(self, row: int, col: int, color: int) -> List[Move]:
        moves = []
        # Les 4 directions orthogonales
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for row_dir, col_dir in directions:
            new_row = row + row_dir
            new_col = col + col_dir
            
            while self.board.is_valid_position(new_row, new_col):
                target_piece, target_color = self.board.get_piece(new_row, new_col)
                
                if target_piece is None:
                    moves.append(Move((row, col), (new_row, new_col), ROOK))
                    new_row += row_dir
                    new_col += col_dir
                else:
                    if target_color != color:
                        moves.append(Move((row, col), (new_row, new_col), ROOK))
                    break  # On sort immédiatement après avoir rencontré une pièce
                
        return moves

    def _get_queen_moves(self, row: int, col: int, color: int) -> List[Move]:
        # La dame combine les mouvements de la tour et du fou
        moves = self._get_rook_moves(row, col, color)
        bishop_moves = self._get_bishop_moves(row, col, color)
        
        # Convertir les mouvements de fou et de tour en mouvements de dame
        for move in moves + bishop_moves:
            move.piece_type = QUEEN
            
        return moves + bishop_moves

    def _get_king_moves(self, row: int, col: int, color: int) -> List[Move]:
        moves = []
        # Le roi peut se déplacer d'une case dans toutes les directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for row_dir, col_dir in directions:
            new_row = row + row_dir
            new_col = col + col_dir
            
            if self.board.is_valid_position(new_row, new_col):
                target_piece, target_color = self.board.get_piece(new_row, new_col)
                if target_piece is None or target_color != color:
                    moves.append(Move((row, col), (new_row, new_col), KING))
                
        # TODO: Ajouter le roque
        return moves 