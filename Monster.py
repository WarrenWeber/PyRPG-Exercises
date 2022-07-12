from Character import Character
from MonsterWeapon import MonsterWeapon


class Monster(Character):

    def __init__(self, Dice, name="Wolf"):
        Character.__init__(self, Dice, name)
        # We redefine life of the monster
        self.defineLife(True)
        # We set the weapon for the monster
        self.setWeapon(MonsterWeapon())

    def attack(self, character):
        roll = self.dice.rollDice()
        damage = self.weapon.attack(roll)
        character.receiveDamage(damage)
        print(self.name + " hits " + character.getName() + " for " + str(damage))
        print(character.getName() + " HP: " + str(character.getLife()) + "\n")