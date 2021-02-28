import random
import copy

class Hat:

#    collection = list()
    def __init__(self, **kw):
#        print(kw)
        self.collection = []
        for k, v in kw.items():
#            print(k, v)
            for i in range(v):
                self.collection.append(k)
#        print(self.collection)

    def draw(self, balls):
        temp = []
        if len(self.collection) <= balls:
            temp = self.collection
            self.collection = []
#            print(temp)
#            print('hope empy collection: ', self.collection)
            return temp
        else:
#            temp = list()
            while balls > 0:
                x = random.randrange(1, len(self.collection))
                temp.append(self.collection[x])
                self.collection.pop(x)
                balls -= 1
            return temp


#def experiment(H, expected_balls, num_balls_drawn, num_experiments):
#     not_fails = 0
#     fails = 0
#     looking_for = list()
#     for k, v in expected_balls.items():
#         for i in range(v):
#             looking_for.append(k)
#
# #    print('2: ', looking_for.__dict__, looking_for.collection)
#    print('search dict: ', expected_balls)
#    print('searching for: ', looking_for)
#    print('inside: ', H.collection)
    # counter = num_experiments
    # while counter > 0:
    #     look_temp = copy.deepcopy(looking_for)
    #     counter -= 1
    #     h = copy.deepcopy(H)
    #     temp = h.draw(num_balls_drawn)
    #     print(temp)
    #     print(look_temp)
    #     try:
    #         for item in look_temp:
    #             temp.remove(item)
    #         not_fails += 1
    #         print('win')
    #     except ValueError:
    #         fails += 1
    #         print('fail')
    # print(not_fails, fails)
    # if not_fails == 0:
    #     return 0
    # else:
    #     return float(not_fails) / num_experiments

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0.0
    expected = list()
    counter = 0
    for k, v in expected_balls.items():
        for i in range(v):
            expected.append(k)
    print(expected)
    # while counter < num_experiments:
    #     temp_hat = copy.deepcopy(hat)
    #     grabbed_balls = temp_hat.draw(num_balls_drawn)
    #     counter += 1
    #     test = all(item in expected for item in grabbed_balls)
    #     print(test, grabbed_balls, success)
    #     if test:
    #         success += 1
    #
    while counter <= num_experiments:
        temp_exp = copy.deepcopy(expected)
        counter += 1
        temp_hat = copy.deepcopy(hat)
        grab_balls = temp_hat.draw(num_balls_drawn)
#        print(grab_balls)
        found = False
        for ball in expected:
            if(ball in grab_balls):
                grab_balls.remove(ball)
                found = True
            else:
                found = False
                break
#            print('loop')
        if found:
            print(found, success)
            success += 1

#    success = float(success) / num_balls_drawn
    return float(success) / num_experiments


Hat(red=5, blue=4)
x = Hat(red=23, blue=20, green=3)
print(x.draw(8))
print('experiment')
#hat = Hat(black=6, red=4, green=3)
#probability = experiment(hat, {"red": 2, "green": 1}, 5, 2000)
#print('prob: ', probability)

#hat = Hat(blue=4, red=2, green=6)
#prob = experiment(hat, {"blue": 2, "red": 1}, 4, 30)
#print("Probability:", prob)
#hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
#p = experiment(hat, {"yellow":2,"blue":3,"test":1}, 18, 10)
#print('another test: ', p)
#        expected = 1.0
#        self.assertAlmostEqual(actual, expected, delta = 0.01, msg =
#       'Expected experiment method to return a different probability.')

hat = Hat(blue=3,red=2,green=6)
bility = experiment(hat, {"blue":2,"green":1}, 4, 100)
print('prob: ', bility)
#actual = probability
#expected = 0.272
