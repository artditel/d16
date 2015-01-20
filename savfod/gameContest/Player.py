class Player:

class ScorePlayer(Player):
    def __init__(self, score_function):
        self.score_function = score_function

    def make_move(self, game):
        possible_moves = game.get_possible_moves()

        move_scores = []
        for move in possible_moves:
            new_pos = game.get_pos_after_move(pos, move):
            score = self.score_function(new_pos)
            move_scores.append((move, score))



