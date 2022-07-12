from Character import Character


class Thieft(Character):
    def __init__(self, Dice, name):
        Character.__init__(self, Dice, name)
        self.life += 2

    def getClassName(self):
        return "Thieft"

    def attack(self, character):
        roll = self.dice.rollDice()
        if roll[1] != "Critical Failure":
            damage = self.weapon.attack(roll)
            character.receiveDamage(damage)
            print(self.name + " hits " + character.getName() + " for " + str(damage))
            if not character.alive():
                print("You killed " + character.getName() + "\n")
            else:
                print(character.getName() + " HP: " + str(character.getLife()) + "\n")
        return roll