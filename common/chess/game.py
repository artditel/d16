#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import sys
import chess
import baseline

class ScorerWrapper:
    WHITE_WINS_SCORE = 1000
    BLACK_WINS_SCORE = -1000
    DRAW_SCORE = 0

    def __init__(self, scorer, use_cache=True):
        self.scorer = scorer
        self.total_calls = 0
        self.cached_calls = 0
        self.cache = {}
        self.use_cache = use_cache

    def calc(self, p):
        if self.use_cache:
            zobrist_hash = p.zobrist_hash()
            pos_hash = (zobrist_hash, p.transpositions[zobrist_hash])
            if pos_hash in self.cache:
                self.cached_calls += 1
                return self.cache[pos_hash]

        self.total_calls += 1
        if p.is_game_over():
            if p.is_draw():
                score = self.DRAW_SCORE
            elif p.is_white_move():
                score = self.BLACK_WINS_SCORE
            else:
                score = self.WHITE_WINS_SCORE
        else:
            score = self.scorer(p)

        if self.use_cache:
            self.cache[pos_hash] = score
        return score

class Position(chess.Bitboard):
    GREEN = ''
    RED   = ''
    ENDC  = '\033[0m'

    def get_pieces(self):
        pieces = []
        for i in range(8):
            for j in range(8):
                if self.piece_at(8*i + j) is not None:
                    pieces.append((self.piece_at(8*i + j).symbol(), i, j))
        return pieces

    def get_white_pieces(self):
        return [x for x in self.get_pieces() if x[0].upper() == x[0]]

    def get_black_pieces(self):
        return [x for x in self.get_pieces() if x[0].lower() == x[0]]

    def get_pieces(self):
        pieces = []
        for i in range(8):
            for j in range(8):
                if self.piece_at(8*i + j) is not None:
                    pieces.append((self.piece_at(8*i + j).symbol(), i, j))
        return pieces

    def get_piece_by_coordinate(self, i, j):
        return self.piece_at(8*i + j).symbol()


    def is_white_move(self):
        return self.turn == chess.WHITE

    def is_draw(self):
        return self.is_stalemate()          or \
            self.is_insufficient_material() or \
            self.is_fivefold_repitition()   or \
            self.is_seventyfive_moves()

    def print_console(self):
        move_num = self.fullmove_number
        if self.is_white_move():
            move_num -= 1
        print( '%d.%s' % (move_num, ' ...' if self.is_white_move() else ''), self.peek() if len(self.move_stack) else "")
        print()
        s = self.fen().split()[0]
        try:
            print( s \
                .replace('/', '\n')   \
                .replace('1', ' '*1*2)  \
                .replace('2', ' '*2*2)  \
                .replace('3', ' '*3*2)  \
                .replace('4', ' '*4*2)  \
                .replace('5', ' '*5*2)  \
                .replace('6', ' '*6*2)  \
                .replace('7', ' '*7*2)  \
                .replace('8', ' '*8*2)  \
                .replace('p', '♟ ') \
                .replace('n', '♞ ') \
                .replace('b', '♝ ') \
                .replace('r', '♜ ') \
                .replace('q', '♛ ') \
                .replace('k', '♚ ') \
                .replace('P', '♙ ') \
                .replace('N', '♘ ') \
                .replace('B', '♗ ') \
                .replace('R', '♖ ') \
                .replace('Q', '♕ ') \
                .replace('K', '♔ '))
        except:
            print( s \
                .replace('/', '\n')   \
                .replace('1', ' '*1*2)  \
                .replace('2', ' '*2*2)  \
                .replace('3', ' '*3*2)  \
                .replace('4', ' '*4*2)  \
                .replace('5', ' '*5*2)  \
                .replace('6', ' '*6*2)  \
                .replace('7', ' '*7*2)  \
                .replace('8', ' '*8*2)  \
                .replace('p', 'p ') \
                .replace('n', 'n ') \
                .replace('b', 'b ') \
                .replace('r', 'r ') \
                .replace('q', 'q ') \
                .replace('k', 'k ') \
                .replace('P', 'P ') \
                .replace('N', 'N ') \
                .replace('B', 'B ') \
                .replace('R', 'R ') \
                .replace('Q', 'Q ') \
                .replace('K', 'K '))


        # print('\n==================================\n')

class MoveLister(object):
    def get(self, p, depth):
        '''
        @param  p     -- Position
        @param  depth -- current depth
        @return list of (move, move_score) tuples sorted accordingly
        '''
        raise NotImplemented('Must be implemented!')

class TrivialLister(MoveLister):
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def get(self, p, depth):
        if depth >= self.max_depth:
            return []
        ans = [(move, 0.) for move in p.legal_moves]
        random.shuffle(ans)
        return ans

class PositionScoreLister(MoveLister):
    def __init__(self, scorer, depth_widths):
        '''
        @param score        -- descendant of PositionScorer
        @param depth_widths -- list of total best moves left at each depth, 0 means all moves should be taken
        '''
        self.scorer       = scorer
        self.depth_widths = depth_widths

    def get(self, p, depth):
        if depth >= len(self.depth_widths):
            return []

        scored_moves = []
        for move in p.legal_moves:
            p.push(move)
            scored_moves.append((move, self.scorer.calc(p)))
            p.pop()
        random.shuffle(scored_moves)
        scored_moves.sort(key=lambda t: t[1], reverse=p.is_white_move())

        width = self.depth_widths[depth]
        return scored_moves if width == 0 else scored_moves[:width]

class MoveFinder(object):
    def __init__(self, scorer):
        self.scorer = scorer

    def _find(self, p):
        raise NotImplemented('Must be implemented!')

    def find(self, p):
        self.scorer.total_calls = 0
        self.scorer.cached_calls = 0
        return self._find(p)

class DepthWidthMoveFinder(MoveFinder):
    def __init__(self, scorer, lister):
        super(DepthWidthMoveFinder, self).__init__(scorer)
        self.lister = lister

    def _find(self, p, depth=0):
        considered_moves = self.lister.get(p, depth)
        if len(considered_moves) == 0:
            return None, self.scorer.calc(p)

        scored_variations = []
        for move, move_score in considered_moves:
            p.push(move)
            scored_variations.append((move, self._find(p, depth + 1)[1]))
            p.pop()

        random.shuffle(scored_variations)
        scored_variations.sort(key=lambda t: t[1], reverse=p.is_white_move())
        return (max if p.is_white_move() else min)(scored_variations, key=lambda t: t[1])

class BruteForceFinder(MoveFinder):
    def __init__(self, scorer, depth):
        super(BruteForceFinder, self).__init__(scorer)
        self.depth = depth

    def _calc_best_move_score(self, position, recursion_depth = 2):
        possible_moves = position.legal_moves
        if recursion_depth == 0 or position.is_game_over():
            return None, self.scorer.calc(position)

        move_scores = []
        for move in possible_moves:
            position.push(move)
            score = self._calc_best_move_score(position, recursion_depth - 1)[1]
            move_scores.append((move, score))
            position.pop()

        random.shuffle(move_scores)
        move_scores.sort(key=lambda move_score: move_score[1], reverse=position.is_white_move())

        if recursion_depth == self.depth:
            print(move_scores[:3])

        return move_scores[0]

    def _find(self, position):
        move, score = self._calc_best_move_score(position, self.depth)
        return move, score

class AlphaBetaFinder(MoveFinder):
    def __init__(self, scorer, depth):
        super(AlphaBetaFinder, self).__init__(scorer)
        self.depth = depth
        self.INFTY = ScorerWrapper.WHITE_WINS_SCORE + 1
        self.MINUS_INFTY = ScorerWrapper.BLACK_WINS_SCORE - 1

    def calc_move_score(self, position, move):
        position.push(move)

        if position.is_game_over():
            score = self.scorer.calc(position)
        else:
            scores = []
            for move in list(position.legal_moves):
                position.push(move)
                scores.append(self.scorer.calc(position))
                position.pop()

            if position.is_white_move():
                score = max(scores)
            else:
                score = min(scores)

        position.pop()


        return score

    def alpha_beta_find(self, position, depth, alpha, beta):
        if depth == 0 or position.is_game_over():
            return None, self.scorer.calc(position)

        possible_moves = list(position.legal_moves)
        random.shuffle(possible_moves)
        if depth == self.depth:
            reverse = position.is_white_move()
            possible_moves.sort(key = lambda move: self.calc_move_score(position, move), reverse=reverse)
            # print (depth, reverse)
            # for move in possible_moves:
            #     print (move, self.calc_move_score(position, move))

        best_move = possible_moves[0]
        if position.is_white_move():
            score = self.MINUS_INFTY
            for move in possible_moves:
                position.push(move)
                m, new_score = self.alpha_beta_find(position, depth - 1, alpha, beta)
                position.pop()
                if new_score > score:
                    score = new_score
                    best_move = move

                alpha = max(alpha, score)
                if beta <= alpha:
                    break #beta cut-off

        else:
            score = self.INFTY
            for move in possible_moves:
                position.push(move)
                m, new_score = self.alpha_beta_find(position, depth - 1, alpha, beta)
                position.pop()
                if new_score < score:
                    score = new_score
                    best_move = move

                beta = min(beta, score)
                if beta <= alpha:
                    break #alpha cut-off
        return best_move, score


    def _find(self, position):
        move, score = self.alpha_beta_find(position, self.depth, self.MINUS_INFTY, self.INFTY)

        if False:
            #compare with brute-force
            calls = self.scorer.total_calls + self.scorer.cached_calls
            check = BruteForceFinder(self.scorer, self.depth)
            print (check.find(position))
            calls_after = self.scorer.total_calls + self.scorer.cached_calls
            print("alpha-beta calls: {}, brute-force calls: {}, diff: {}".format(calls, calls_after, calls_after - calls))

            # print (move, score)
            # assert(check._find(position)[1] == score)

        return move, score

class ManualFinder(MoveFinder):
    def __init__(self, default_finder):
        self.default_finder = default_finder
        super(ManualFinder, self).__init__(lambda x: 0) #mock score

    def _find(self, position):
        position.print_console()
        print("possible_moves:")

        possible_moves = sorted(list(position.legal_moves), key=str)
        move_by_str = {str(move):move for move in possible_moves}
        def format_func(ind_move):
            return "%d: %s" % ind_move
        print(list(map(format_func, enumerate(possible_moves, start=1))))

        success = False
        while not success:
            if sys.version.startswith('2'):
                #python 2 compatibility
                universal_input = raw_input
            else:
                universal_input = input

            inp = universal_input("Print move or it's index. Or q to quit. Or just nothing (and enter) for auto-move: ").strip()
            if inp.startswith('q'):
                print("exiting")
                sys.exit(0)
            elif inp == "":
                return self.default_finder._find(position)
            elif inp in move_by_str.keys():
                return move_by_str[inp], 0 #mock score
            else:
                try:
                    num = int(inp)
                    move = possible_moves[num - 1]
                    success = True
                except:
                    print("Bad input. Move or index ({}-{}) or q expected".format(1, len(position.legal_moves)))
        return move, 0 #mock score

class Game(object):
    def __init__(self, white_finder, black_finder, verbose=True, step_by_step=False, step_by_advantage=False):
        self.position = Position()
        self.white_finder = white_finder
        self.black_finder = black_finder
        self.verbose      = verbose
        self.step_by_step = step_by_step
        self.step_by_advantage = step_by_advantage

    def run(self):
        position_scores = []

        while not self.position.is_game_over():
            start  = time.time()
            finder = self.white_finder if self.position.is_white_move() else self.black_finder
            move, score = finder.find(self.position)
            self.position.push(move)
            if self.verbose:
                self.position.print_console()
                total_calls = finder.scorer.total_calls
                cached_calls = finder.scorer.cached_calls
                total_time  = time.time() - start
                position_scores.append(score)
                print('calls :', total_calls)
                print('in cache :', cached_calls    )
                print('time  :', total_time)
                print('speed :', total_calls / total_time if total_time > 0 else 0)
                print('score :', position_scores[-1])
                print('\n=========== *** ===========\n')

            if self.step_by_step:
                input("Press Enter to continue...")
            if score != 0 and self.step_by_advantage:
                input("Advantage! Press Enter to continue...")
        return self.get_result()

    def get_result(self):
        if not self.position.is_game_over():
            raise ValueError('Game not over yet!')
        if self.position.is_draw():
            return 0.5, 0.5
        if self.position.is_white_move():
            return 0, 1
        return 1, 0

def run_once(first, second):
    w, b = Game(first, second, verbose=True, step_by_step=False, step_by_advantage=False).run()
    print('Result', w, ':', b)

if __name__ == '__main__':
    first_scorer  = SCORERS_WRAPPED['material']
    second_scorer = SCORERS_WRAPPED['material']
    run_once(
        DepthWidthMoveFinder(first_scorer, PositionScoreLister(first_scorer, [0, 10])),
        BruteForceFinder(second_scorer, 2),
    )

