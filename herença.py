class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} está a comer")
    
    def talk(self):
        print("animal sound")

class Dog(Animal):
    def barck(self):
        print("AU AU AU")
    
    def talk(self):
        print("au au au")


class Dalmata(Dog):
    pass

class Rafeiro(Dog):
    pass

class Caramelo(Dog):
    pass

class Cat(Animal):
    pass

bob = Dog("Bob")

bob.eat()
bob.barck()
bob.talk()

bolinhas = Rafeiro("bolinhas")
bolinhas.talk()

tareco = Cat("Tareco")

tareco.eat()


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Olá, o meu nome é {self.name}")

class Student(Person, Dog):
    pass

pedro = Student("Pedro")
pedro.say_hello()
pedro.barck()
pedro.eat()