import game
from baseline import EasyScorer

FILENAME = "test.txt"

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def check(your_function):
    correct = 0
    incorrect = 0
    for line in open(FILENAME):
        smth, num, res = line.strip().split('\t')
        if your_function(int(num)) == res:
            correct += 1
        else:
            incorrect += 1
    print("correct share: %.2f%%" % (100 * correct / float(correct + incorrect)))


def check_get_score(your_function):
    pairs = []
    for line in open(FILENAME):
        fen, score = line.strip().split('\t')[:2]
        pos = game.Position()
        pos.set_fen(fen)

        predicted_score = your_function(pos)
        pairs.append( (int(score), predicted_score) )

    correct = 0
    incorrect = 0
    for i, (s1, p1) in enumerate(pairs):
        for s2, p2 in pairs[:i]:

            if sign(s1 - s2) == sign(p1 - p2):
                correct += 1
            else:
                incorrect += 1

    print("correct share: %.2f%%" % (100. * correct / float(correct + incorrect)))
    return(100. * correct / float(correct + incorrect))

if __name__ == "__main__":
    #this line is called in "python check.py" but not in importing check.py
    check_get_score(EasyScorer())
