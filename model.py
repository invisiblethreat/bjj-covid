import random


class Jiujiteiro(object):
    def __init__(self):
        self.infected = False
        self.partnered = False
        self.rester = False
        self.opponents = []

    def infect(self):
        self.infected = True


def simulate(students, rounds):
    fighters = {}
    for i in range(students):
        fighters[i] = Jiujiteiro()

    # infect one participant at random
    fighters[random.randrange(0, students-1)].infect()

    # for k, v in fighters.items():
    #    if v.infected:
    #print("fighter {} is infected".format(k))

    master = list(range(len(fighters)))
    #print("master opponent list: {}".format(master))
    for i in range(rounds):
        opps = master.copy()
        #print("Round: {}".format(i))
        while len(opps) != 0:
            first = random.choice(opps)
            opps.remove(first)
            second = random.choice(opps)
            opps.remove(second)
        # print("fighter {} faces fighter {}".format(first, second))

            fighters[first].opponents.append(second)
            fighters[second].opponents.append(first)

            if fighters[first].infected or fighters[second].infected:
                fighters[first].infect()
                fighters[second].infect()

    infected = 0
    for _, v in fighters.items():
        if v.infected:
            infected += 1
        #print("Fighter {} infected: {}".format(k, v.infected))
        #print("Fighter {} opponents: {}".format(k, v.opponents))
        # print("***")

    return infected


runs = 1000000
students = 20
rounds = 5
results = []
for _ in range(runs):
    results.append(simulate(students, rounds))


ave = sum(results)/len(results)
print("BJJ Class Contact Tracing: 1 infected participant")
print("Sparring rounds: {}".format(rounds))
print("Class size:      {}".format(students))
print("Simulation runs: {}".format(runs))
print("***")
print("Average infection rate: {}/{}".format(ave, students))
print("Average infection pct:  {}%".format((ave/students)*100))
