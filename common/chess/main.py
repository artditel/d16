#!/usr/bin/env python3
# encoding: utf-8
import sys
import argparse
import random
import baseline
import game
import check

def get_scorers():
    scorers = {
        "random":   baseline.random_scorer,
        "material": baseline.material_scorer,
        "titanic": baseline.titanic(),
        "varya": baseline.varya,
        "varya_scorer_class": baseline.varya_scorer_class(),
        "Timur": baseline.Timur_scorer(),
        "liz":baseline.liz_scorer(),
        "Deep Red": baseline.deep_red,
        "az": baseline.az(),
        "az": baseline.az(),
        "baseline_knn": baseline.KNNChecker([baseline.EasyScorer()]),
    }

    return {name: game.ScorerWrapper(scorer) for name, scorer in scorers.items()}

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
    parser.add_argument('--predict', action='store_true', help='use prediction file instead of playing game')
    parser.add_argument('--rounds', type=int, default=2, help='how many rounds each pair plays')
    parser.add_argument('--quiet',  action='store_true', help='no debug info')
    parser.add_argument('--no_random', action='store_true', help='do not use random (for leaderboard)')
    parser.add_argument('--lister', default="0,5,5",     help='set recursion depths to use. E.g. 0,5,5')
    parser.add_argument(
        'scorers',
        nargs='*',
        help='scorers that should play with eaсh other (default: all)'
    )
    return parser.parse_args()

def make_default_player(scorer, lister="0,5,5"):
    val_list = list(map(int, lister.split(',')))
    if len(val_list) == 1 and val_list[0] >= 2:
        return game.AlphaBetaFinder(scorer, val_list[0])
    else:
        return game.DepthWidthMoveFinder(scorer, game.PositionScoreLister(scorer, val_list))


def make_players(parser):
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
    return names, players

def calc_results(names, players, parser):
    results = [0] * len(players)
    if parser.predict:
        scorers = get_scorers()
        for i, name in enumerate(names):
            results[i] = check.check_get_score(scorers[name])
    else:
        print("Starting tournament!")
        for i, p1 in enumerate(players):
            for j, p2 in enumerate(players[:i]):
                print("playing {} Vs {}".format(names[i], names[j]))
                res1, res2 = run_compare(p1, p2, parser.rounds, not parser.quiet)
                results[i] += res1
                results[j] += res2

    return results

if __name__ == '__main__':
    parser = parse_args()
    if parser.no_random:
        random.seed(1)

    names, players = make_players(parser)
    results = calc_results(names, players, parser)

    print("")
    print("Leaderboard:")
    place = 1
    for res, name in sorted(zip(results, names), reverse=True):
        print("{}. {} with result {}".format(place, name, res))
        place += 1

