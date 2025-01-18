import unittest
from src.environment.board import Board
from src.environment.move_generator import MoveGenerator
from src.utils.constants import *

class TestKnightMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_generator = MoveGenerator(self.board)
        
    def test_initial_knight_moves(self):
        """Test des mouvements initiaux des cavaliers"""
        moves = self.move_generator.get_legal_moves(0, 1)
        self.assertEqual(len(moves), 2)
        expected_positions = {(2, 0), (2, 2)}
        actual_positions = {move.end_pos for move in moves}
        self.assertEqual(expected_positions, actual_positions)
        
    def test_knight_captures(self):
        """Test des captures par les cavaliers"""
        self.board.set_piece(2, 2, PAWN, BLACK)
        moves = self.move_generator.get_legal_moves(0, 1)
        captures = [move for move in moves if move.end_pos == (2, 2)]
        self.assertEqual(len(captures), 1) 