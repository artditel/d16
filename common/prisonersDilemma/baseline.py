import random
random.random()

class Angry:
    def cooperate(self,history):
        return False
    def get_name(self):
        return "Angry"

class Kind:
    def cooperate(self,history):
        return True
    def get_name(self):
        return "Kind"

class Random:
    def cooperate(self,history):
        return random.random() > 0.5
    def get_name(self):
        return "Random"

class Unforgiving:
    def cooperate(self,history):
        other_player_moves = (j for (i,j) in history)
        if False in other_player_moves:
            return False
        else:
            return True
    def get_name(self):
        return "Unforgiving"

