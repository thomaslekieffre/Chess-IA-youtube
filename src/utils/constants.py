# Constantes pour les pièces
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

# Couleurs
WHITE = 0
BLACK = 1

# Valeurs des pièces
PIECE_VALUES = {
    PAWN: 100,
    KNIGHT: 300,
    BISHOP: 300,
    ROOK: 500,
    QUEEN: 900,
    KING: 10000
}

# Représentation des pièces en caractères
PIECE_CHARS = {
    (WHITE, PAWN): '♙',
    (WHITE, KNIGHT): '♘',
    (WHITE, BISHOP): '♗',
    (WHITE, ROOK): '♖',
    (WHITE, QUEEN): '♕',
    (WHITE, KING): '♔',
    (BLACK, PAWN): '♟',
    (BLACK, KNIGHT): '♞',
    (BLACK, BISHOP): '♝',
    (BLACK, ROOK): '♜',
    (BLACK, QUEEN): '♛',
    (BLACK, KING): '♚',
    (EMPTY, 0): '·'
} 