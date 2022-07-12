from Character import Character


class Sorcerer(Character):
    def __init__(self, Dice, name):
        Character.__init__(self, Dice, name)
        self.life -= 1

    def getClassName(self):
        return "Sorcerer"

    def attack(self, character):
        roll = self.dice.rollDice()
        # For the sorcerer we kill the monster if we get a Critical success
        if roll[1] == "Critical success":
            character.receiveDamage(character.getLife())
            print("You killed the monster in one shot ! \n")
        else:
            damage = self.weapon.attack(roll)
            character.receiveDamage(damage)
            print(self.name + " hits " + character.getName() + " for " + str(damage))
            if not character.alive():
                print("You killed " + character.getName() + "\n")
            else:
                print(character.getName() + " HP: " + str(character.getLife()) + "\n")
        return roll
