import unittest
from src.environment.board import Board
from src.environment.move_generator import MoveGenerator
from src.utils.constants import *

class TestRookQueenMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_generator = MoveGenerator(self.board)
        
    def test_initial_rook_moves(self):
        """Test des mouvements initiaux de la tour"""
        moves = self.move_generator.get_legal_moves(0, 0)
        self.assertEqual(len(moves), 0)
        
    def test_rook_open_file(self):
        """Test des mouvements de la tour sur une colonne ouverte"""
        self.board.clear_board()  # Vider d'abord le plateau
        self.board.set_piece(0, 0, ROOK, WHITE)  # Tour en a1
        moves = self.move_generator.get_legal_moves(0, 0)
        vertical_moves = [move for move in moves if move.end_pos[1] == 0]
        self.assertEqual(len(vertical_moves), 7)
        
    def test_queen_moves(self):
        """Test des mouvements de la dame"""
        self.board.clear_board()  # Vider d'abord le plateau
        self.board.set_piece(3, 3, QUEEN, WHITE)  # Dame au centre
        moves = self.move_generator.get_legal_moves(3, 3)
        self.assertEqual(len(moves), 27)  # 8+8+7+4 mouvements possibles

if __name__ == '__main__':
    unittest.main() 