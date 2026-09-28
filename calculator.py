while True:
    # Pedir dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Pedir operação
    operacao = input("Escolha a operação (+, -, *, /): ")

    # Fazer cálculo
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação inválida!")
        continue  # volta ao início do loop

    # Mostrar resultado
    print("Resultado:", resultado)

    # Perguntar se quer continuar
    continuar = input("Quer fazer outra conta? (y/n): ")

    if continuar.lower() != "s":
        print("Programa terminado.")
        break