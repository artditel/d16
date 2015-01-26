def tictac(my_moves, enemy_moves):
        history = list(my_moves, enemy_moves)
        other_player_moves = [history[:-3]]
        if other_player_moves[0] == True and other_player_moves[1] == True and other_player_moves[2] == True:
            return True
        else:
            return False
