import random

def Angry(my_moves, enemy_moves):
    return False

def Kind(my_moves, enemy_moves):
    return True

def Random(my_moves, enemy_moves):
    return random.random() > 0.5

def Unforgiving(my_moves, enemy_moves):
    return False not in enemy_moves
def king(my_moves, enemy_moves):
	return False
