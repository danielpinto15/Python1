class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        test = height * 2
        self.batata = test
    
    def say_hi(self):
        print("Ola, eu sou", self.name)

    def test(self, another_name):
        print(self.name, "diz ola a", another_name)
    

person1 = Person("Ana", 25, 165)
person2 = Person("Pedro", 25, 198)



class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def levantar(self, valor):
        self.saldo -= valor

conta1 = Conta(100)

conta1.depositar(150)

conta1.levantar(90)


class Aluno:
    def __init__(self, name, grade):
        self.name = name
        self.grade =  grade

    def approved(self):
        if self.grade >= 10:
            print("Approved!")
        else:
            print("Repproved!")

aluno1 = Aluno("Ana", 20)
aluno2 = Aluno("Pedro", 9.5)

aluno1.approved()
aluno2.approved()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print("o barulho que o animal fizer")

dog = Animal("Bob")
print(dog)
dog.talk()