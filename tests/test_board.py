import unittest
from src.environment.board import Board
from src.utils.constants import *

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        
    def test_initial_position(self):
        """Test de la position initiale du plateau"""
        # Test des pions
        for col in range(8):
            piece_type, color = self.board.get_piece(1, col)
            self.assertEqual(piece_type, PAWN)
            self.assertEqual(color, WHITE)
            
            piece_type, color = self.board.get_piece(6, col)
            self.assertEqual(piece_type, PAWN)
            self.assertEqual(color, BLACK)
            
        # Test des pièces blanches
        expected_pieces = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        for col, piece in enumerate(expected_pieces):
            piece_type, color = self.board.get_piece(0, col)
            self.assertEqual(piece_type, piece)
            self.assertEqual(color, WHITE)
            
    def test_empty_squares(self):
        """Test des cases vides"""
        for row in range(2, 6):
            for col in range(8):
                piece_type, color = self.board.get_piece(row, col)
                self.assertIsNone(piece_type)
                self.assertIsNone(color) 