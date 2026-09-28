from random import choice

class_name = {
    "1": {
        "name": "Richard",
        "has_not_presented": True
    },
    "2": {
        "name": "Idalecio",
        "has_not_presented": False
    },
    "3": {
        "name": "João",
        "has_not_presented": False
    },
    "4": {
        "name": "Tiago",
        "has_not_presented": True
    },
    "5": {
        "name": "Filipe",
        "has_not_presented": True
    },
    "6": {
        "name": "Miguel",
        "has_not_presented": False
    },
    "7": {
        "name": "Ellen",
        "has_not_presented": True
    }
}

available_students = []

for student in class_name.values():
    if student["has_not_presented"]:
        available_students.append(student)

chosen_student = choice(available_students)

print(chosen_student["name"])