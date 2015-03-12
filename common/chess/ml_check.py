from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
import sklearn
import game
import baseline

LEARN_FILE = "learn.txt"
TEST_FILE = "test.txt"

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def prepare_data(filename, position_functions):
    scores = []
    features_values = []
    for line in open(filename):
        fen, score = line.strip().split('\t')[:2]
        score = int(score)
        scores.append(score)

        pos = game.Position()
        pos.set_fen(fen)
        features = [f(pos) for f in position_functions]
        features_values.append(features)

    return features_values, scores

def calc_metric(predicted, expected):
    #share of right sorted pairs
    correct = 0
    incorrect = 0

    for i in range(len(expected)):
        for j in range(i):
            if sign(expected[i] - expected[j]) == sign(predicted[i] - predicted[j]):
                correct += 1
            else:
                incorrect += 1

    print("correct share: %.2f%%" % (100. * correct / float(correct + incorrect)))
    return(100. * correct / float(correct + incorrect))

def check_model(model, position_functions):
    learn_features, learn_scores = prepare_data(LEARN_FILE, position_functions)
    test_features, test_scores = prepare_data(TEST_FILE, position_functions)

    # learn_features = preprocessing.normalize(learn_features)
    # test_features = preprocessing.normalize(test_features)

    model.fit(learn_features, learn_scores)
    predicted = model.predict(test_features)

    calc_metric(predicted, test_scores)

check_model(DecisionTreeRegressor(), [baseline.EasyScorer(), baseline.lizz(), baseline.az(), baseline.artemka_scorer_class(), baseline.deep_red, baseline.elephants, ])


