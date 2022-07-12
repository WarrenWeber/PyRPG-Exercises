from Weapon import Weapon


class ShortSword(Weapon):

    def __init__(self, name):
        Weapon.__init__(self, name)
        self.normal_attack = 3
        self.critical_success = 6