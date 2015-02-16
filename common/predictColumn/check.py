FILENAME = "position_scores.txt"

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
