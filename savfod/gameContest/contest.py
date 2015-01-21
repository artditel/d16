import AbstractGame
from ReversiGame import ReversiGame
from Player import ScorePlayer


def play_game(game, players):
    player_index = 0
    while game.not_finished():
#        game_copy = game.make_copy()
        game_copy = game

        player_index = (player_index + 1) % len(players)
        move = players[player_index].generate_move(game_copy)

        game.make_move(move)

    return game.get_winner()


def parse_args():
    pass

def random_function(game_copy):
    import random
    return random.random()



def main():
    args = parse_args()

    player1 = ScorePlayer(random_function)
    player2 = ScorePlayer(random_function)

    count = [0,0]
    for i in range(100):
        game = ReversiGame()
        res = play_game(game, [player1, player2])
        count[res] += 1
        print("{}-th game played".format(i))

    print("Count p1 p2 {}:{}".format(count[0], count[1]))




if __name__ == "__main__":
    main()


