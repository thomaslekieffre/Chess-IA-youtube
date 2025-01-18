import unittest
from src.environment.board import Board
from src.environment.move_generator import MoveGenerator
from src.utils.constants import *

class TestPawnMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_generator = MoveGenerator(self.board)
        
    def test_initial_pawn_moves(self):
        """Test des mouvements initiaux des pions"""
        # Pion blanc e2
        moves = self.move_generator.get_legal_moves(1, 4)
        self.assertEqual(len(moves), 2)
        expected_positions = {(2, 4), (3, 4)}
        actual_positions = {move.end_pos for move in moves}
        self.assertEqual(expected_positions, actual_positions)
        
    def test_pawn_capture(self):
        """Test des captures par les pions"""
        # Placer un pion noir en e3
        self.board.set_piece(2, 4, PAWN, BLACK)
        moves = self.move_generator.get_legal_moves(1, 3)  # Pion d2
        captures = [move for move in moves if move.end_pos == (2, 4)]
        self.assertEqual(len(captures), 1) 