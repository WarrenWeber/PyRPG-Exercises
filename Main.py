from Dice import Dice
from LightSaber import LightSaber
from Monster import Monster
from ShortSword import ShortSword
from Sorcerer import Sorcerer
from Staff import Staff
from Thieft import Thieft
from Warrior import Warrior


class main:
    """
    Class used to initialise and launch the game
    dice : Object of type dice
    name : str
    player : Object of type Character
    weapon : Object of type Weapon
    """
    def __init__(self):
        self.dice = None
        self.name = None
        self.player = None
        self.weapon = None

    def launchGame(self):
        """
        Method used to launch the game
        :return: None
        """
        self.dice = Dice(20)
        print("Hi there !")
        self.name = input("Choose a name: \n")
        self.selectClass()
        self.selectWeapon()
        self.main_Loop()
        input("Press enter to exit ;)")

    def selectClass(self):
        """
        Method used to select the class
        :return: None
        """

        listClasses = ["Warrior", "Sorcerer", "Thieft"]
        # Display of the classes
        print("List of Classes:")
        for i in range(len(listClasses)):
            print(str(i) + ". " + listClasses[i])
        # Selection of the class
        while True:
            try:
                classChoice = int(input("Choose your class in the list ! (Write the number ahead the class) \n"))
                assert 0 <= classChoice <= len(listClasses) - 1
            except ValueError:
                print("Sorry, I didn't understand that.")
            except AssertionError:
                print("Please Enter a number between 0 and " + str(len(listClasses) - 1))
            else:
                break
        # Registration of the selected class
        if classChoice == 0:
            self.player = Warrior(self.dice, self.name)
        elif classChoice == 1:
            self.player = Sorcerer(self.dice, self.name)
        else:
            self.player = Thieft(self.dice, self.name)

    def selectWeapon(self):
        """
            Method used to select the weapon
            :return: None
        """

        dictWeapon = {"Warrior": ["Light Saber", "Short Sword", "Staff"],
                      "Sorcerer": ["Staff"],
                      "Thieft": ["Short Sword", "Staff"]}
        listWeapon = dictWeapon.get(self.player.getClassName())
        # Display of the weapon
        print("List of weapon:")
        for i in range(len(listWeapon)):
            print(str(i) + ". " + listWeapon[i])
        # Selection of the weapon
        while True:
            try:
                weaponChoice = int(input("Choose your weapon in the list ! (Write the number ahead the weapon) \n"))
                assert 0 <= weaponChoice <= len(listWeapon) - 1
            except ValueError:
                print("Sorry, I didn't understand that.")
            except AssertionError:
                print("Please Enter a number between 0 and" + str(len(listWeapon) - 1))
            else:
                break
        # Registration of the selected weapon
        if listWeapon[weaponChoice] == "Light Saber":
            playerWeapon = LightSaber(listWeapon[weaponChoice])
        elif listWeapon[weaponChoice] == "Short Sword":
            playerWeapon = ShortSword(listWeapon[weaponChoice])
        else:
            playerWeapon = Staff(listWeapon[weaponChoice])

        self.player.setWeapon(playerWeapon)


    def main_Loop(self):
        """
        The game engine
        :return: None
        """
        # Did the game finish ?
        while self.player.alive() and self.player.getGold() < 50:
            monster = Monster(self.dice)
            award = monster.getLife()
            # Do we have a dead ?
            while monster.alive() and self.player.alive():
                roll = self.player.attack(monster)
                if roll[1] == "Critical Failure" and self.player.getClassName() == "Thieft":
                    award = 0
                    print("You ran away ! \n")
                    break
                monster.attack(self.player)
            # We reward the player for killing the monster
            if not monster.alive():
                self.player.receiveAward(award)
        # Did the player die ?
        if not self.player.alive():
            print("You died !")
        # Did the player has enough money to win
        if self.player.getGold() >= 50:
            print("You win ! Well play")


if __name__ == '__main__':
    main = main()
    main.launchGame()
