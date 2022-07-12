import random as rand


class Dice:
    """
    Class to define the dice
    number_face : int
    """
    def __init__(self, number_face):
        self.number_face = number_face

    def rollDice(self):
        """
        We generate a random number
        :return: Tuple (int,str)
        """
        roll = rand.randint(1, self.number_face)
        if roll <= 8:
            state = "Critical Failure"
        elif roll >= self.number_face-6:
            state = "Critical success"
        else:
            state = "Normal"
        print("Dice rolling: "+str(roll))
        print(state)
        return (roll, state)
