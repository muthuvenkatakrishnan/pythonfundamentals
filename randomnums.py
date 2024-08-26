import random
class Weapon:

    def useWeapon(self):
        pass

class Knife(Weapon):

    def useWeapon(self):
        print("Slit the throat")

class Grenade(Weapon):

    def useWeapon(self):
        print("Pull the pin and throw")

class Gun(Weapon):

    def useWeapon(self):
        print("Aim the Target and Shoot")

class Shield(Weapon):

    def useWeapon(self):
        print("Protect")


r = random.randrange(1,5)
obj = None
if r == 1:
    obj = Knife()
elif r == 2:
    obj = Grenade()
elif r == 3:
    obj = Gun()
else:
    obj = Shield()

obj.useWeapon()