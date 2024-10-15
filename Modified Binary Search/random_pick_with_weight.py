import random

class RandomPickWithWeight:

    def __init__(self, weights):
        self.weights = weights
        self.cum_weights = []
        self.total = 0

        for i in weights:
            self.total += i 
            self.cum_weights.append(self.total)

    def pick_index(self):
        r_num = random.randint(1, self.total)
        s, e = 0, len(self.cum_weights) - 1

        while s < e:
            mid = (s + e) //2

            if self.cum_weights[mid] <= r_num:
                s = mid + 1
            else:
                e = mid

        return s
