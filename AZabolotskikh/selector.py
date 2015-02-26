from operator import lt, gt
class DecisionStump:
    def __call__(self, score):
        return self.relation(score,self.treshold)
    def __init__(self, rel, treshold):
        self.relation = rel
        self.treshold = treshold
    @classmethod
    def makeFromDataset(clazz,ds,objtype, rel):
        xmax = 1<<32
        ymax = None
        for i in [x[1] for x in ds]:
            errors = len([x for x in ds if not rel(x[1],i) and x[2] in objtype]) + len([x for x in ds if rel(x[1],i) and not x[2] in objtype])
            if errors < xmax:
                xmax = errors
                ymax = i
        return clazz(rel, ymax)
    def __str__(self):
        return str(self.relation) + " " + str(self.treshold)

def convertLabel(data, labelMapping):
    return [(x,labelMapping[y]) for x,y in data]

kPiecesToScores = {'q':9,'r':5,'b':3,'n':3,'p':1,'k':3}
def fenToScore(fen):
    pos = fen.split(" ")[0]
    whiteScore = 0
    blackScore = 0
    for piece, score in kPiecesToScores:
        whiteScore += pos.count(piece) * score
        blackScore += pos.count(piece.upper()) * score
    return (whiteScore, blackScore)



def check(your_function):
    correct = 0
    incorrect = 0
    for line in open("position_scores.txt"):
        smth, num, res = line.strip().split('\t')
        if your_function(int(num)) == res:
            correct += 1
        else:
            incorrect += 1
    print("correct share: %.2f%%" % (100 * correct / float(correct + incorrect)))

def main():
    dataset = [x.rstrip().split("\t") for x in open("position_scores.txt").readlines()]
    dataset = [[x,int(y), z] for x,y,z in dataset]
    zero_one_ds = DecisionStump.makeFromDataset(dataset, ["0-1"], lt)
    one_zero_ds = DecisionStump.makeFromDataset(dataset, ["1-0"], gt)
    def ds_wrapper(score):
        if zero_one_ds(score):
            return "0-1"
        if one_zero_ds(score):
            return "1-0"
    print (check(ds_wrapper))
    wtds = DecisionStump.makeFromDataset(dataset, ["0-1", "1/2-1/2"], lt)
    ods = DecisionStump(gt, wtds.treshold)
    dataset1 = [pos for pos in dataset if wtds(pos[1])]
    tds = DecisionStump.makeFromDataset(dataset, ["1/2-1/2"], gt)
    lds = DecisionStump(lt, tds.treshold)
    def ds_wrapper2(score):
        if ods(score):
            return "1-0"
        if tds(score):
            return "1/2-1/2"
        return "0-1"
    print (check(ds_wrapper2))
    
    

main()
