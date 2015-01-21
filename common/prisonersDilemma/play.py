import random
import baseline

GAMES_COUNT = 100

def get_players():
    players = [
        baseline.Angry,
        baseline.Kind,
        baseline.Random,
        baseline.Xor
    ]

    return players

WINS = [
[(0, 0), (4, -1), ],
[(-1, 4), (3, 3), ],
]

def play(player1, player2):

    print("Starting games between {} and {}".format(player1.get_name(), player2.get_name()))

    history = []
    history_reverted = []
    players_wins = [0, 0]

    for i in range(GAMES_COUNT):
        move1 = int(bool(player1.cooperate(history)))
        move2 = int(bool(player2.cooperate(history_reverted)))
        history.append( (move1, move2) )
        history_reverted.append( (move2, move1) )

        win1, win2 = WINS[move1][move2]
        players_wins[0] += win1
        players_wins[1] += win2

    print("Game finished. Log:" + str(history))
    print()
    return players_wins


def main():
    random.seed(1)
    players = get_players()
    results = [0] * len(players)
    for ind1, p1 in enumerate(players):
        for ind2, p2 in enumerate(players):
            win1, win2 = play(p1(), p2())
            results[ind1] += win1
            results[ind2] += win2

    print()

    sorted_players = sorted(zip(results, players), reverse=True)
    for ind, (res, player) in list(enumerate(sorted_players))[::-1]:
        print("{}. {} with result {}".format(ind + 1, player().get_name(), res))

main()
