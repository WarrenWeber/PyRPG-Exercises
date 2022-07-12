import random as rand


class Character:
    """
    Class to define the different classes: Sorcerer, Warrior, Thieft and also monster
    because they share the same specifications.
    Life : int
    Dice : Object of type Dice
    Name : str
    Weapon : Object of type Weapon (Weapon is added during the initialisation)
    Gold : int
    cpt_strike : int (used to count the number of strike for light saber)
    """
    def __init__(self, dice, name):
        self.life = 0
        self.dice = dice
        self.name = name
        self.weapon = None
        self.gold = 0
        self.cpt_strike = 0
        self.defineLife()

    def defineLife(self, monster=False):
        """
        :param monster: Boolean (To define if we build a monster or a player)
        :return: None
        This method is used to set life at the construction of the object
        """
        if monster:
            # We roll the dice to define the life of the monster
            roll_life = self.dice.rollDice()
            if roll_life[1] == "Critical Failure":
                self.setLife(15)
            elif roll_life[1] == "Critical success":
                self.setLife(20)
            else:
                self.setLife(rand.randint(15, 20))
            print("Monster HP: " + str(self.getLife()) + "\n")
        else:
            # We roll the dice to define the life of the player
            roll_life = self.dice.rollDice()
            if roll_life[1] == "Critical Failure":
                self.setLife(80)
            elif roll_life[1] == "Critical success":
                self.setLife(100)
            else:
                self.setLife(rand.randint(80, 100))
            print("Your HP will be " + str(self.getLife()) + "\n")

    def attack(self, character):
        """
        :param character: Object of type Character
        :return: Tuple
                Tuple[0]: Int (number that we get at the roll of the dice)
                Tuple[1]: str (Critical Success, Critical Failure or Normal. We return it for the Thieft to know
                          if we have to run away or not)
        """
        # We want to know if the player use a light saber or not in order to apply the effect of it
        if self.weapon.getName() == "Light Saber":
            if self.cpt_strike == 3:
                print("Light Saber hits you because it's your third strike with it. You loose 2 HP.")
                self.receiveDamage(2)
                self.cpt_strike = 0
            else:
                self.cpt_strike += 1

        # We roll dice to know if we do a critical success, a critical failure or a normal
        roll = self.dice.rollDice()
        damage = self.weapon.attack(roll)
        character.receiveDamage(damage)
        print(self.name + " hits " + character.getName() + " for " + str(damage))
        if not character.alive():
            print("You killed " + character.getName() + "\n")
        else:
            print(character.getName() + " HP: " + str(character.getLife()) + "\n")
        return roll

    def getClassName(self):
        return None

    def getLife(self):
        return self.life

    def getGold(self):
        return self.gold


    def getName(self):
        return self.name

    def receiveDamage(self, damage):
        """
        :param damage: int
        :return: None
        Method to set life with the damage received.
        """
        self.setLife(self.getLife() - damage)

    def receiveAward(self, gold):
        """
        :param damage: int
        :return: None
        Method to set award with the gold that the monster had.
        """
        self.gold = self.getGold() + gold

    def setWeapon(self, weapon):
        self.weapon = weapon

    def setLife(self, life):
        self.life = life

    def alive(self):
        """
        :return: Boolean
        Method to know if the object is alive.
        """
        if self.getLife() > 0:
            return True
        else:
            return False
