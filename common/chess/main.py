import sys
import argparse
import random
import game
import baseline

# ===================================================
# scorers list
# ===================================================

def get_scorers():
    scorers = {
        "random": baseline.random_scorer,
        "material": baseline.material_scorer,
    }
    scorers_wrapped = {name: game.ScorerWrapper(scorer) for name, scorer in scorers.items()}

    return scorers_wrapped


# ===================================
# run!
# ===================================

def run_compare(first, second, rounds=10, verbose=True):
    score_first, score_second = 0, 0
    for i in range(rounds):
        f, s = (first, second) if i < rounds / 2 else (second, first)
        w, b = game.Game(f, s, verbose, step_by_step=False).run()
        score_first  += w if i < rounds / 2 else b
        score_second += b if i < rounds / 2 else w
        print('Game', i, ':', score_first, score_second)
    print('Final score :', score_first, score_second)
    return score_first, score_second


def parse_args():
    parser = argparse.ArgumentParser(description='Chess contest leaderboard program. Use python main.py player1 player2 for their fight')
    parser.add_argument('--rounds', type=int, default=2, help='how many rounds each pair plays')
    parser.add_argument('--quiet', action='store_true', help='print no debug info')
    parser.add_argument('--random', action='store_true', help='use true random (not for leaderboard)')
    parser.add_argument('--lister', default="0,5,5", help='set recursion depths to use. For e.g. 0,5,5')
    parser.add_argument(
        'scorers',
        nargs='*',
        help='scorers that should play with eash other (all if no scorers)'
    )

    return parser.parse_args()

def make_default_player(scorer, lister="0,5,5"):
    val_list = list(map(int, lister.split(',')))
    return game.DepthWidthMoveFinder(scorer, game.PositionScoreLister(scorer, val_list))

if __name__ == '__main__':
    parser = parse_args()
    if not parser.random:
        random.seed(1)

    players = []
    scorers = get_scorers()
    names = list(parser.scorers if len(parser.scorers) > 0 else get_scorers().keys())
    for name in names:
        if name == 'manual':
            players.append(game.ManualFinder(make_default_player(game.ScorerWrapper(baseline.material_scorer), parser.lister)))
        elif name in scorers.keys():
            players.append(make_default_player(scorers[name], parser.lister))
        else:
            print("unexpected player {}".format(name))
            print("expected: manual or %s" % " ".join(scorers.keys()))
            sys.exit()

    results = [0] * len(players)
    for i, p1 in enumerate(players):
        for j, p2 in enumerate(players[:i]):
            print("playing {} Vs {}".format(names[i], names[j]))
            res1, res2 = run_compare(p1, p2, parser.rounds, not parser.quiet)
            results[i] += res1
            results[j] += res2

    print("")
    print("Leaderboard:")
    place = 1
    for res, name in sorted(zip(results, names), reverse=True):
        print("{}. {} with result {}".format(place, name, res))
        place += 1
