numbers = [1, 2 , 3, 4, 5, 6, 7, 8, 9]

#duble = [pudim * 2 for pudim in numbers]

dobro = []

for number in numbers:
    dobro.append(number * 2)

print(dobro)

#variavel = [valor, loop, condição]
pairs = [batata for batata in numbers if batata % 2 == 0]

print("pairs", pairs)

names = ["filipe", "tiago"]

upper_case_names = [name.upper() for name in names]

print(upper_case_names)

