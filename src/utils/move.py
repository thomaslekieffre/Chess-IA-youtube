from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class Move:
    start_pos: Tuple[int, int]
    end_pos: Tuple[int, int]
    piece_type: int
    captured_piece: Optional[int] = None
    is_promotion: bool = False
    promotion_piece: Optional[int] = None
    is_castling: bool = False
    is_en_passant: bool = False
    
    def to_uci(self) -> str:
        """Convertit le mouvement en notation UCI"""
        files = 'abcdefgh'
        ranks = '12345678'
        
        start_file = files[self.start_pos[1]]
        start_rank = ranks[self.start_pos[0]]
        end_file = files[self.end_pos[1]]
        end_rank = ranks[self.end_pos[0]]
        
        move_str = f"{start_file}{start_rank}{end_file}{end_rank}"
        
        if self.is_promotion and self.promotion_piece:
            piece_chars = {2: 'n', 3: 'b', 4: 'r', 5: 'q'}
            move_str += piece_chars[self.promotion_piece]
            
        return move_str
    
    @classmethod
    def from_uci(cls, uci: str) -> 'Move':
        """Crée un mouvement à partir d'une notation UCI"""
        files = 'abcdefgh'
        ranks = '12345678'
        
        start_file = files.index(uci[0])
        start_rank = ranks.index(uci[1])
        end_file = files.index(uci[2])
        end_rank = ranks.index(uci[3])
        
        is_promotion = len(uci) == 5
        promotion_piece = None
        
        if is_promotion:
            piece_chars = {'n': 2, 'b': 3, 'r': 4, 'q': 5}
            promotion_piece = piece_chars[uci[4]]
            
        return cls(
            start_pos=(start_rank, start_file),
            end_pos=(end_rank, end_file),
            piece_type=None,  # Sera défini par l'environnement
            is_promotion=is_promotion,
            promotion_piece=promotion_piece
        ) 