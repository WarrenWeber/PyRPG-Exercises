from Weapon import Weapon


class LightSaber(Weapon):

    def __init__(self, name):
        Weapon.__init__(self, name)
        self.normal_attack = 4
        self.critical_success = 8


