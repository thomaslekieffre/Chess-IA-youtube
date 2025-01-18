import unittest
from src.environment.board import Board
from src.environment.move_generator import MoveGenerator
from src.utils.constants import *

class TestKingMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_generator = MoveGenerator(self.board)
        
    def test_initial_king_moves(self):
        """Test des mouvements initiaux du roi"""
        # Le roi ne devrait pas avoir de mouvements au début
        moves = self.move_generator.get_legal_moves(0, 4)  # Position e1
        self.assertEqual(len(moves), 0)
        
    def test_king_center_moves(self):
        """Test des mouvements du roi au centre"""
        self.board.clear_board()
        self.board.set_piece(3, 3, KING, WHITE)  # Roi en d4
        moves = self.move_generator.get_legal_moves(3, 3)
        self.assertEqual(len(moves), 8)  # Le roi devrait avoir 8 mouvements possibles
        
    def test_king_capture(self):
        """Test des captures par le roi"""
        self.board.clear_board()
        self.board.set_piece(3, 3, KING, WHITE)  # Roi blanc en d4
        self.board.set_piece(3, 4, PAWN, BLACK)  # Pion noir en e4
        self.board.set_piece(3, 2, PAWN, WHITE)  # Pion blanc en c4
        
        moves = self.move_generator.get_legal_moves(3, 3)
        captures = [move for move in moves if move.end_pos == (3, 4)]
        blocked = [move for move in moves if move.end_pos == (3, 2)]
        
        self.assertEqual(len(captures), 1)  # Devrait pouvoir capturer le pion noir
        self.assertEqual(len(blocked), 0)   # Ne devrait pas pouvoir capturer le pion blanc

if __name__ == '__main__':
    unittest.main() 