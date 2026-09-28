import csv

columns = ["name", "age", "phone"]
people = [
    {"name": "Ana", "age": 102, "phone": "Porto"},
    {"name": "Bruno", "age": 110, "phone": "Porto"},
    {"name": "Daniel", "age": 15, "phone": "Porto"},
]
teste = [
    {"name": "Ana", "email": 102, "phone": "Porto"},
    {"name": "Bruno", "email": 110, "phone": "Porto"},
    {"name": "Daniel", "email": 15, "phone": "Porto"},
]

with open("oldPeople.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, columns)
    w.writeheader()
    w.writerows(people)

with open("oldPeople.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print(list(reader))
    for line in teste:
        print(line["email"])
    for line in reader:
        print(line["email"])


def obter_nota(lista_notas):
    return lista_notas["nota"]