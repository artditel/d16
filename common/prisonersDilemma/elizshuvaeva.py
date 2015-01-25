def Confused(my_moves, enemy_moves):
        history = list(zip(my_moves, enemy_moves))
        other_player_moves = (history[:-1])
        if other_player_moves == True:
            return True
        else:
            return False

