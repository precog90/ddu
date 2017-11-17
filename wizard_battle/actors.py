import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        print(random.randint(1, 12) + self.level)
        return random.randint(1, 12) + self.level

class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}".format(
            self.name, creature.name
        ))
        my_roll = random.randint(1, 12) + self.level
        creature_roll = creature.get_defensive_roll()
        print("My roll {} Creature Roll {}".format(my_roll, creature_roll))
        if my_roll >= creature_roll:
            print("The wizard has handsomely triumphed over {}".format(creature.name))
            return 1
        else:
            print("The wizard has been defeated")
            return 0


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = None
        #if self.breaths_fire:
        #    fire_modifier = 5
        #else:
        #    fire_modifier = 1
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        #print(base_roll)
        #print(scale_modifier)
        #print(fire_modifier)
        return base_roll*fire_modifier*scale_modifier




