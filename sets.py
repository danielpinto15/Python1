numbers = { 1, 1, 3, 3, 2, 4}

print(numbers)

numbers.add(5)

print(numbers)

numbers.remove(2)

print(numbers)

if 3 in numbers:
    print("Existe")

names = ["Ana", "João", "Ana", "Miguel"]

names_set = set(names)

print(names_set)


set_a = { 1, 2, 3}
set_b = { 3, 4, 5}

uniao = set_a | set_b

print(uniao)

interseçao = set_a & set_b

print(interseçao)

diferença = set_a - set_b

print(diferença)

diferença2 = set_b - set_a

print(diferença2)