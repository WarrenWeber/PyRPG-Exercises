class Weapon:
    """
        Class to define the different weapons: Light Saber, Short Sword and Staff
        Name : str
        critical_failure : int
        normal_attack : int
        critical_success : int
    """
    def __init__(self, name):
        self.name = name
        self.critical_failure = 0
        self.normal_attack = 0
        self.critical_success = 0

    def attack(self, dice):
        """
        :param dice : Tuple (int, str)
        :return: int (number of damage)
        """
        if dice[1] == "Critical Failure":
            return self.critical_failure
        elif dice[1] == "Critical Success":
            return self.critical_success
        else:
            return self.normal_attack

    def getName(self):
        return self.name
