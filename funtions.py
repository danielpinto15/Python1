
def sayHello(name):
    print(f"Olá {name}")


def somar(a, b):
    resultado = a + b
    print(resultado)

def area(l, a):
    result = l * a
    return result

number1 = 3
number2 = 5
print(area(number1, number2))


def profundidade(l, a, p):
    result = l * a * p
    return result

def calculoTotal(l, a, p):
    prof = 60 #profundidade(l, a, p)
    ar = 20 #area(l, a)
    resultado_final = prof + ar
    print(resultado_final)
    


len("ola") # tamanho
max(1, 5, 3) # o maior numero
min(1, 5, 3) # menor numero
sum([1, 2, 3]) # soma todos os numeros da lista. 



numberList = [15, 17, 16, 19, 20, 2, 12]

def media(numeros):
    result = sum(numeros) / len(numeros)
    return result

media(numberList)