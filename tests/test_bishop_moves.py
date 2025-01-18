import unittest
from src.environment.board import Board
from src.environment.move_generator import MoveGenerator
from src.utils.constants import *

class TestBishopMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_generator = MoveGenerator(self.board)
        
    def test_initial_bishop_moves(self):
        """Test des mouvements initiaux du fou"""
        # Le fou ne devrait pas avoir de mouvements au début
        moves = self.move_generator.get_legal_moves(0, 2)  # Position c1
        self.assertEqual(len(moves), 0)
        
    def test_bishop_center_moves(self):
        """Test des mouvements du fou au centre"""
        self.board.clear_board()
        self.board.set_piece(3, 3, BISHOP, WHITE)  # Fou en d4
        moves = self.move_generator.get_legal_moves(3, 3)
        self.assertEqual(len(moves), 13)  # Le fou devrait avoir 13 mouvements possibles
        
    def test_bishop_captures(self):
        """Test des captures par le fou"""
        self.board.clear_board()
        self.board.set_piece(3, 3, BISHOP, WHITE)  # Fou blanc en d4
        self.board.set_piece(5, 5, PAWN, BLACK)    # Pion noir en f6
        self.board.set_piece(1, 1, PAWN, WHITE)    # Pion blanc en b2
        
        moves = self.move_generator.get_legal_moves(3, 3)
        captures = [move for move in moves if move.end_pos == (5, 5)]
        blocked = [move for move in moves if move.end_pos[0] < 1 or move.end_pos[1] < 1]
        
        self.assertEqual(len(captures), 1)  # Devrait pouvoir capturer le pion noir
        self.assertEqual(len(blocked), 0)   # Ne devrait pas pouvoir aller au-delà du pion blanc

if __name__ == '__main__':
    unittest.main() 