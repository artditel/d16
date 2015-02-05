import random
import chess

# ===================================================
# scorers
# ===================================================

def random_scorer(p):
    return random.uniform(-1, 1)

PIECE_2_SCORE = {
    'p': 1,
    'n': 3,
    'b': 3,
    'r': 5,
    'q': 9,
    'k': 0,
}

def material_scorer(p):
    s = 0
    for square in chess.SQUARES:
        piece = p.piece_at(square)
        if piece == None:
            continue
        s += PIECE_2_SCORE[piece.symbol().lower()] * (1 if piece.color == chess.WHITE else -1)
    return s

