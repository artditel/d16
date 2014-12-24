list = open("a.txt", "r")
end = []
for line in list:
	line = line.strip()
	line = int(line)
	end.append(line)

b = len(end)
end = sorted(end)
print(end[b - 1], end[b - 2],  end[b - 3], end[b - 4], end[b - 5], end[b - 6], end[b - 7], end[b - 8], end[b - 9], end[b - 10],)
