import numpy as np
from typing import List, Tuple, Optional
from src.utils.constants import *
from src.utils.move import Move

class Board:
    def __init__(self):
        # Plateau 8x8x12 (8x8 cases, 6 types de pièces x 2 couleurs)
        self.board = np.zeros((8, 8, 12), dtype=np.int8)
        self.current_player = WHITE
        self.move_history = []
        self.initialize_board()
        
    def initialize_board(self):
        """Initialise le plateau dans sa position de départ"""
        # Placement des pions
        for col in range(8):
            self.set_piece(1, col, PAWN, WHITE)  # Pions blancs
            self.set_piece(6, col, PAWN, BLACK)  # Pions noirs
            
        # Placement des pièces
        piece_order = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        for col, piece in enumerate(piece_order):
            self.set_piece(0, col, piece, WHITE)  # Pièces blanches
            self.set_piece(7, col, piece, BLACK)  # Pièces noires
            
    def set_piece(self, row: int, col: int, piece_type: int, color: int):
        """Place une pièce sur le plateau"""
        layer = piece_type - 1 + (color * 6)
        self.board[row, col, :] = 0  # Efface toute pièce existante
        self.board[row, col, layer] = 1
        
    def get_piece(self, row: int, col: int) -> Tuple[Optional[int], Optional[int]]:
        """Retourne (type_piece, couleur) à la position donnée"""
        piece_layer = np.where(self.board[row, col] == 1)[0]
        if len(piece_layer) == 0:
            return None, None
            
        layer = piece_layer[0]
        color = WHITE if layer < 6 else BLACK
        piece_type = (layer % 6) + 1
        return piece_type, color
        
    def is_valid_position(self, row: int, col: int) -> bool:
        """Vérifie si une position est dans les limites du plateau"""
        return 0 <= row < 8 and 0 <= col < 8
        
    def make_move(self, move: Move) -> bool:
        """Effectue un mouvement sur le plateau"""
        start_piece, color = self.get_piece(*move.start_pos)
        
        # Vérifications de base
        if start_piece is None or color != self.current_player:
            return False
            
        # TODO: Vérifier si le mouvement est légal
        
        # Effectuer le mouvement
        self.set_piece(*move.end_pos, start_piece, color)
        self.board[move.start_pos[0], move.start_pos[1], :] = 0
        
        # Enregistrer le mouvement
        self.move_history.append(move)
        
        # Changer de joueur
        self.current_player = BLACK if self.current_player == WHITE else WHITE
        
        return True
        
    def __str__(self) -> str:
        """Affiche le plateau en ASCII"""
        board_str = "  a b c d e f g h\n"
        for row in range(7, -1, -1):
            board_str += f"{row+1} "
            for col in range(8):
                piece_type, color = self.get_piece(row, col)
                if piece_type is None:
                    char = PIECE_CHARS[(EMPTY, 0)]
                else:
                    char = PIECE_CHARS[(color, piece_type)]
                board_str += char + " "
            board_str += f"{row+1}\n"
        board_str += "  a b c d e f g h"
        return board_str 
        
    def clear_board(self):
        """Vide complètement le plateau"""
        self.board = np.zeros((8, 8, 12), dtype=np.int8) 