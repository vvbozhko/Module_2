import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {int(self._cords[2])}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are {eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

# Example usage
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
