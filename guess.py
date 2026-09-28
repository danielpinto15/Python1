guess = 0
number = 5


while guess != number:
    guess = int(input("digitar numero: " ))

    if (guess == number):
        print("Acertou")
    elif (guess >= number + 2):
        print("muito alto")
    elif (guess <= number - 2):
        print("muito baixo")
    else:
        print("quase lá")
        