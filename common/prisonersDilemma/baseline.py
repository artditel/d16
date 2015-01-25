import random

def Angry(my_moves, enemy_moves):
    return False

def Kind(my_moves, enemy_moves):
    return True

def Random(my_moves, enemy_moves):
    return random.random() > 0.5

def Unforgiving(my_moves, enemy_moves):
    return False not in enemy_moves

def Confused(self, my_moves, enemy_moves):
        history = list(zip(my_moves, enemy_moves))
        other_player_moves = (history[:-1])
        if other_player_moves == True:
            return True
        else:
            return False

