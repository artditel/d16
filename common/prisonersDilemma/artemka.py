def copying(my_moves, enemy_moves):
	if len(enemy_moves) > 0:
		if enemy_moves[len(enemy_moves) - 1] == True:
			return True
		else:
			return False
	else:
		return True
