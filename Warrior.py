from Character import Character


class Warrior(Character):
    def __init__(self, Dice, name):
        Character.__init__(self, Dice, name)
        self.life += 5

    def getClassName(self):
        return "Warrior"

    def attack(self, character):
        # We want to know if the player use a light saber or not in order to apply th effect of it
        if self.weapon.getName() == "Light Saber":
            if self.cpt_strike == 3:
                print("Light Saber hits you because it's your third strike with it")
                self.receiveDamage(2)
                self.cpt_strike = 0
            else:
                self.cpt_strike += 1
        roll = self.dice.rollDice()
        damage = self.weapon.attack(roll)

        if roll[1] != "Critical Failure":
            damage += 2
        character.receiveDamage(damage)
        print( self.name + " hits " + character.getName() + " for " + str(damage))
        if not character.alive():
            print("You killed " + character.getName() + "\n")
        else:
            print(character.getName() + " HP: " + str(character.getLife()) + "\n")
        return roll