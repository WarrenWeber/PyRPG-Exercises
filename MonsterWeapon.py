from Weapon import Weapon
import random as rand


class MonsterWeapon(Weapon):

    def __init__(self):
        self.critical_failure = 5
        self.normal_attack = rand.randint(5,10)
        self.critical_success = 10