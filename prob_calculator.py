import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))+1) for _ in range(n)] # The previous code can't reach to the last element because random.randrange does not include the upperbound(the last value of that range), hence I just added 1 in the random.randrange(len(self.contents)+1) so that it can now reach the last element and pop out every element. Hope this will help,if I am wrong here then please tell me .


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments
