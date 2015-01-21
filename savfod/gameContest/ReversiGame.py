from AbstractGame import Game
from AbstractGame import Position

DEFAULT_FIELD_SIZE = 8
EMPTY_PLAYER_INDEX = -1
PLAYER_COUNT = 2

#moves = (i,j) pairs
def argmax(ar):
    if len(ar) == 0:
        return -1
    return sorted(enumerate(ar), key=lambda pair:pair[1], reverse=True)[0][0]

class ReversiGame(Game):
    def __calculate_possible_moves(self):
        possible_moves = set()
        for i in range(self.field_size):
            for j in range(self.field_size):
                move = (i,j)
                if self.position.get_cell(move) == EMPTY_PLAYER_INDEX:
                    possible_moves.add(move)
        return possible_moves

    def __init__(self, field_size = DEFAULT_FIELD_SIZE):
        self.field_size = field_size
        self.position = ReversiPosition(self.field_size)
        self.possible_moves = self.__calculate_possible_moves()
        self.cur_player = 1

    def get_possible_moves(self):
        return list(self.possible_moves)

    def make_move(self, move):
        assert(self.position.get_cell(move) == EMPTY_PLAYER_INDEX)
        self.position.set_cell(move, self.cur_player)

        self.possible_moves -= {move}
        self.cur_player = (self.cur_player + 1) % 2

    def revert_move(self, move):
        assert(self.position.get_cell(move) != EMPTY_PLAYER_INDEX)
        self.position.set_cell(move, EMPTY_PLAYER_INDEX)

        self.possible_moves.add(move)
        self.cur_player = (self.cur_player - 1) % 2

    def finished(self):
        return len(self.get_possible_moves()) == 0

    def not_finished(self):
        return not self.finished()

    def get_winner(self):
        assert(self.finished)

        players_points = [0] * PLAYER_COUNT
        for i in range(self.field_size):
            for j in range(self.field_size):
                player = self.position.get_cell( (i,j) )
                if player != EMPTY_PLAYER_INDEX:
                    players_points[player] += 1

        return argmax(players_points)

    def make_copy(self):
        copy = ReversiGame(field_size = self.field_size)
        copy.position = self.position
        copy.possible_moves = self.possible_moves
        copy.cur_player = self.cur_player
        return copy


class ReversiPosition(Position):
    def __init__(self, field_size):
        self.field = [[EMPTY_PLAYER_INDEX] * field_size for i in range(field_size)]

    def get_cell(self, index):
        i,j = index
        return self.field[i][j]

    def set_cell(self, index, value):
        i,j = index
        self.field[i][j] = value


if __name__ == "__main__":
    #for testing only. This file is not expected to be called
    game = ReversiGame()
    import random

    moves = game.get_possible_moves()
    move = random.choice(moves)
    game.make_move(move)
    game.revert_move(move)

    for i in range(1000):
        if game.finished():
            print ("Game successfully finished in %d moves" % i)
            break;

        moves = game.get_possible_moves()
        move = random.choice(moves)
        game.make_move(move)

