length = int(input())
width = int(input())
winning_positions = []

for i in range(width):
	winning_positions.append([])
	for t in range(length):
		winning_positions[i].append(0)
winning_positions[width-1][0] == 2

for i in range(width):
	for g in range(length):
		if (g>3 and winning_positions[i][g-3] == 2) or \
		(g > 3 and winning_positions[i-1][g-3] == 2) or \
		(g > 2 and winning_positions[i-2][g-2] == 2) or \
		(g > 2 and winning_positions[i-1][g-1] == 2) or \
		winning_positions[i-1][g] == 2:
			winning_positions[i][g] = 1
		else:
			winning_positions[i][g] = 2

for i in reversed(winning_positions):
	print(i) 
