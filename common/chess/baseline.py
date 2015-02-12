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

class EasyScorer:
    def __call__(self, p):
        return self.calc_score(p)

    def calc_score(self, p):
        white_pieces = p.get_white_pieces()
        black_pieces = p.get_black_pieces()

        white = self.get_score_one_sided(white_pieces, black_pieces)
        black = self.get_score_one_sided(black_pieces, white_pieces)

        return white - black

    def get_score_one_sided(self, pieces, enemy_pieces):
        score = 0

        functions = {
            'p': self.get_pawn_score,
            'n': self.get_knight_score,
            'b': self.get_bishop_score,
            'r': self.get_rook_score,
            'q': self.get_queen_score,
            'k': self.get_king_score,
        }

        for p, i, j in pieces:
            if p == p.lower():
                i = 7 - i
            score += functions[p.lower()](i, j)
        return score

    def get_pawn_score(self, i, j):
        return 1

    def get_knight_score(self, i, j):
        return 3

    def get_bishop_score(self, i, j):
        return 3

    def get_rook_score(self, i, j):
        return 5

    def get_queen_score(self, i, j):
        return 9

    def get_king_score(self, i, j):
        return 0

def titanic(p):
    return random.uniform(-1, 1)
def Timur(p):
    s=0
    bish=0
    pawn=0    
    pieces = p.get_pieces()
    for square in chess.SQUARES:
            piece = p.piece_at(square)
            if piece == None:
                continue
            if (piece.symbol()=='B' and piece.color == chess.WHITE) or (piece.symbol()=='b' and piece.color == chess.BLACK):
                bish+=1
            s += PIECE_2_SCORE[piece.symbol().lower()] * (1 if piece.color == chess.WHITE else -1) 
    if bish==2:
        s+=(1/3)* (1 if piece.color == chess.WHITE else -1)
    return s

def material_scorer(p):
    s = 0
    for square in chess.SQUARES:
        piece = p.piece_at(square)
        if piece == None:
            continue
        s += PIECE_2_SCORE[piece.symbol().lower()] * (1 if piece.color == chess.WHITE else -1)
    return s

def varya(p):
    s = 0
    for square in chess.SQUARES:
        piece = p.piece_at(square)
        if piece == None:
            continue
        s += PIECE_2_SCORE[piece.symbol().lower()] * (1 if piece.color == chess.WHITE else -1)
    for t, n, e in p.get_pieces():
        if t == 'k':
            s += (-n)*3/100.
        if t == 'K':
            s += (-n)*3/100.
    return s

class varya_scorer_class(EasyScorer):
    def get_king_score(self, i, j):
        return -i/10.

class liz_scorer(EasyScorer):
    def get_pawn_score(self, i, j):
        if i > 1:
            return 1 + i/10
        else:
            return 1
