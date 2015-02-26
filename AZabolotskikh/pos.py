
#def simplePredictor(score):
#	if 
positions = open("position_scores.txt")
data = list(map(lambda x: x.rstrip().split('\t'), positions.readlines()))
print("\n".join(" ".join(x[1:]) for x in data))
print("\033[31;1mwins: {} loses: {} ties: {}".format(len([x for x in data if x[2] == "1-0"]), len([x for x in data if x[2] == "0-1"]), len([x for x in data if x[2] == "1/2-1/2"])))
print("average: {}".format(sum(int(x[1]) for x in data) / len(data) ) )