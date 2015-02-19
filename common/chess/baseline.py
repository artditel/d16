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
        self.p = p
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

class titanic(EasyScorer):
    def get_pawn_score(self, i, j):
        if len(self.p.move_stack) >= 50:
            return i**(1/2)
        else:
            return 1
    def get_knight_score(self, i, j):
        if len(self.p.move_stack) >= 50:
            return 2
        else:
            return 3
    def get_bishop_score(self, i, j):
        if len(self.p.move_stack) >= 50:
            return 4
        else:
            return 3
    def get_rook_score(self, i, j):
        if len(self.p.move_stack) >= 50:
            return 6
        else:
            return 5
class Timur_scorer(EasyScorer):
    #pieces=p.get_pieces()
    def get_king_score(self, i, j):
        return 0.1/((5-i)**2+1)
    def get_pawn_score(self, i, j):
        return 1+0.5/((5-i)**2+1)

    def get_knight_score(self, i, j):
        return 3+1.5/((5-i)**2+1)

    def get_bishop_score(self, i, j):
        return 3+1.5/((5-i)**2+1)

    def get_rook_score(self, i, j):
        return 5+2/((5-i)**2+1)

    def get_queen_score(self, i, j):
        return 9+4.5/((5-i)**2+1)

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

def daylight_grande(p):
    s = 0
    for square in chess.SQUARES:
        piece = p.piece_at(square)
        if piece == None:
            s += -0.1
            continue
        s += PIECE_2_SCORE[piece.symbol().lower()] * (1.1 if piece.color == chess.WHITE else -1)
    for pc, n, e in p.get_pieces():
        if pc == 'p' or pc == 'P':
            s += n*0.2
        if pc == 'r' or pc == 'R':
            s += n*0.15
        if pc == 'n' or pc == 'N':
            s += n*0.1
    return s

class varya_scorer_class(EasyScorer):
    def get_king_score(self, i, j):
        return -i/10.

class liz_scorer(EasyScorer):
    def get_pawn_score(self, i, j):
        if len(self.p.move_stack) >= 50:
            return 1 + i/10
        else:
            if i<4:
                return 1 + i/10
            else:
                return 1

class artemka_scorer_class(EasyScorer):
    def get_queen_score(self, i , j):
        return 9 + i/4
    def get_rook_score(self, i, j):
        return 5 + i/6
    def get_knight_score(self, i, j):
        return 3 + i/9
    def get_bishop_score(self, i, j):
        return 3 + i/9
    def get_pawn_score(self, i, j):
        return 1 + i/12

class az(EasyScorer):
    def get_pawn_score(self, i, j):
        if len(self.p.move_stack) <30:
            return 1-i/10
        else:
            return 1+i/10
    def get_king_score(self, i, j):
        if len(self.p.move_stack) <27:
            return -i/10
        else:
            return 0
    def get_knight_score(self, i, j):
        return 3+i/20
    def get_bishop_score(self, i, j):
        return 3+i/20
    def get_rook_score(self, i, j):
        return 5+i/20
    def get_queen_score(self, i, j):
        return 9+i/20


def deep_red(p):
    s = 0
    for square in chess.SQUARES:
        piece = p.piece_at(square)
        if piece == None:
            s += -0.01
            continue
        s += PIECE_2_SCORE[piece.symbol().lower()] * (2.1 if piece.color == chess.WHITE else -2)
    for pc, n, e in p.get_pieces():
        if pc == 'p' or pc == 'P':
            s += n*0.01
        if pc == 'r' or pc == 'R':
            s += n*0.01
        if pc == 'n' or pc == 'N':
            s += n*0.012
        if pc == 'k' or pc == 'K':
            s += (-n)*0.01
            for dn, kn, ke in p.get_pieces():
                if not piece == None and kn-n > 0:
                    s+=0.02/(kn-n)
    return s

