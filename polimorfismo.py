class Animal:
    def talk(self):
        print("Som")

    def run(self):
        print("barulho a correr")

class Dog(Animal):
    def talk(self):
        print("au au au")


class Cat(Animal):
    def talk(self):
        print("Miau miau")


class Cow(Animal):
    def talk(self):
        print("MUUUUUUUUUUU")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.talk()
    animal.run()