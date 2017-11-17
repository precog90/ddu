import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}".format(
            self.name, creature.name
        ))
        my_roll = random.randint(1,12) + self.level
        creature_roll = random.randint(1,12) +creature.level
        print("My roll {} Creature Roll {}".format(my_roll, creature_roll))
        if my_roll >= creature_roll:
            print("The wizard has handsomely triumphed over {}".format(creature.name))
            return 1
        else:
            print("The wizard has been defeated")
            return 0




class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
