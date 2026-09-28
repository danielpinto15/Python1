class Client:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age >= 0: 
            self.__age = age

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email


carlos = Client("Carlos", 35, "carlos@carlos.com")


print(carlos.age)

carlos.age = -10

print(carlos.age)


class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price

cookies = Product(2.99)

print(cookies.price)

print("DESCONTOS LOUCOS!!")

cookies.price = cookies.price * 0.9

print(cookies.price)