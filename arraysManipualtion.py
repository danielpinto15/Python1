names = ["Ana", "João", "Ana"]

names.append("Daniel") #[Ana, Joao, 5]

print(names)

names.insert(1, "Maria") #[Ana, Maria, João, 5]

print(names)

names.remove("Ana") #[Maria, Joaão, 5] remove o elemento descrito no argumento da função
#names.pop() #[Ana, Maria, João] Remove o ultimo elemento da array
#names.pop(1) #[Ana, Maria, João] Remove o indice passado no argumento da função

print(names)

names.sort()

print(names)

names.reverse()

print(names)

tasks = ["Estudar python", "Entregar o trabalho da semana passada", "arrays"]

tasks.append("Treinar")
tasks.append("fazer um pudim")

print("tasks =", tasks)

tasks.pop()

print("tasks =", tasks)

print("pudins =", len(tasks))
print(len(tasks))

tasks.sort()

print(tasks)