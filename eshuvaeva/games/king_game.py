length = int(input())
width = int(input())
winning_positions = []

for i in range(width):
	winning_positions.append([])
	for t in range(length):
		winning_positions[i].append(2)

for i in range(width):
	for g in range(length):
		if (g>2 and winning_positions[i][g-3] == 2) or \
		(g > 2 and i>0 and winning_positions[i-1][g-3] == 2) or \
		(g > 1 and i>1 and winning_positions[i-2][g-2] == 2) or \
		(g > 0 and i>0 and winning_positions[i-1][g-1] == 2) or \
		(i>0 and winning_positions[i-1][g] == 2):
			winning_positions[i][g] = 1

for i in reversed(winning_positions):
	print(i)
