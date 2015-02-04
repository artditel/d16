import random
import baseline
import elizshuvaeva
import tictac
import artemka
import azhuravlev1

GAMES_COUNT = 100

def get_players_functions():
    players = [
        baseline.Angry,
        baseline.Kind,
        baseline.Random,
        baseline.Unforgiving,
        elizshuvaeva.Confused,
        tictac.tictac,
        azhuravlev1.king,
        artemka.copying,
    ]
    return players

def get_func_name(function):
    return str(function).split()[1]

class Player:
    def __init__(self, function):
        self.function = function
        self.name = get_func_name(function)
        self.score = 0

    def cooperate(self, my_moves, enemy_moves):
        return self.function(my_moves, enemy_moves)

    def get_name(self):
        return self.name

    def add_score(self, diff_score):
        self.score += diff_score

    def get_score(self):
        return self.score

WINS = [
    [( 0, 0), (4, -1), ],
    [(-1, 4), (3,  3), ],
]

def play(player1, player2, win_table=WINS):
    print("Starting games between {} and {}".format(player1.get_name(), player2.get_name()))

    history_first = []
    history_second = []

    players_wins = [0, 0]
    for i in range(GAMES_COUNT):
        move1 = bool(player1.cooperate(history_first[:], history_second[:]))
        move2 = bool(player2.cooperate(history_second[:], history_first[:]))
        history_first.append(move1)
        history_second.append(move2)

        win1, win2 = win_table[int(move1)][int(move2)]
        players_wins[0] += win1
        players_wins[1] += win2

    print("Game finished. {}:{}. Log:".format(players_wins[0], players_wins[1]) + str(list(zip(history_first, history_second))))
    print()
    return players_wins

def main():
    random.seed(57005538399847203271)
    players = [Player(p) for p in get_players_functions()]

    for i, p1 in enumerate(players):
        for p2 in players[i+1:]:
            win1, win2 = play(p1, p2)
            p1.add_score(win1)
            p2.add_score(win2)

    print()
    sorted_players = sorted(players, key=lambda p: p.get_score(), reverse=True)
    for ind, player in enumerate(sorted_players):
        print("{}. {} with result {}".format(ind + 1, player.get_name(), player.get_score()))



main()

