import random

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
}

def calc_by_bitboard(p):
    s = 0
    for square in chess.SQUARES:
        piece = p.piece_at(square)
        if piece == None:
            continue
        s += PIECE_2_SCORE[piece.symbol().lower()] * (1 if piece.color == chess.WHITE else -1)
    return s

def calc_by_fen(p):
    s = 0.
    for c in p.fen().split()[0]:
        if c.lower() not in 'pnbrq':
            continue
        is_white = c.isupper()
        s += PIECE_2_SCORE[c.lower()] * (1 if is_white else -1)
    return s

def material_scorer(p):
    use_fen = True

    return calc_by_fen(p) if use_fen else calc_by_bitboard(p)

