class Worker:
    def __init__(self):
        pass

    def work(self):
        print("Estou a trabalhar")

class Programmer(Worker):
    def work(self):
        print("Estou a programar")

class Designer(Worker):
    def work(self):
        print("Preciso de tempo")

joaquim = Programmer()
alberto = Designer()

joaquim.work()
alberto.work()