import random

import time

from wizard_battle.actors import Wizard, Creature


def main():
    print_header("Wizard Game App")
    game_loop()


def print_header(banner_name):
    print()
    print()
    print("----------------------------------------------------")
    print("                {0}".format(banner_name))
    print("-----------------------------------------------------")
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Monster', 200),
        Creature('Rat', 1),
        Creature('Cat', 2)
    ]

    hero = Wizard('Gandolf', 75)

    while True:
        active_creature = random.choice(creatures)
        #print(active_creature.name)
        print(active_creature.name + " of level " + str(active_creature.level) + " has appeared")
        cmd = input("Do you [a]ttack, [r]unaway or [l]ook around")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard taking rest")
                time.sleep(5)
                print("Wizard returns")
        elif cmd == 'r':
            print("Wizard has fleed")
        elif cmd == 'l':
            print("The wizard {} takes in the surroundings and sees".format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name,c.level))
        else:
            print("Bye")
            break

if __name__ == '__main__':
    main()