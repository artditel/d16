class Player:
    pass

class ScorePlayer(Player):
    def __init__(self, score_function):
        self.score_function = score_function

    def calc_best_move_score(self, game_copy, recursion_depth = 4):
        possible_moves = game_copy.get_possible_moves()
        if recursion_depth == 0 or len(possible_moves) == 0:
            return None, self.score_function(game_copy)


        move_scores = []
        for move in possible_moves:
            game_copy.make_move(move)
            score = self.calc_best_move_score(game_copy, recursion_depth - 1)[1]
            move_scores.append((move, score))
            game_copy.revert_move(move)

        move_scores.sort(key=lambda move_score: move_score[1], reverse=True)
        return move_scores[0]


    def generate_move(self, game_copy, recursion_depth = 2):
        move, score = self.calc_best_move_score(game_copy, recursion_depth)
        return move

