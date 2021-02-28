import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kw):
        self.contents = list()
        for k, v in kw.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, balls):
        temp = []
        if len(self.contents) <= balls:
            temp = self.contents
            self.contents = []
            return temp
        else:
            while balls > 0:
                x = self.contents.pop(random.randrange(len(self.contents)))
                temp.append(x)
                balls -= 1
            return temp


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    not_fails = 0
    fails = 0
    looking_for = list()
    for k, v in expected_balls.items():
        for i in range(v):
            looking_for.append(k)

    counter = num_experiments
    while counter > 0:
        look_temp = copy.deepcopy(looking_for)
        counter -= 1
        h = copy.deepcopy(hat)
        temp = h.draw(num_balls_drawn)

        try:
            for item in look_temp:
                temp.remove(item)
            not_fails += 1
        except ValueError:
            fails += 1

    if not_fails == 0:
        return 0
    else:
        return float(not_fails) / num_experiments
