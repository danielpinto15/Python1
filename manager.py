tarefas = []


def mostrar_menu():
    print("\n--- GESTOR DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")


while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    # Adicionar tarefa
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")

        if tarefa.strip() == "":
            print("A tarefa não pode estar vazia.")
        else:
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")

    # Ver tarefas
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não existem tarefas.")
        else:
            print("\n--- LISTA DE TAREFAS ---")

            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1} - {tarefa}")

    # Remover tarefa
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não existem tarefas para remover.")

        else:
            print("\n--- REMOVER TAREFA ---")

            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1} - {tarefa}")

            indice = input("Escolha o número da tarefa: ")

            if indice.isdigit():
                indice = int(indice)

                if 1 <= indice <= len(tarefas):
                    removida = tarefas.pop(indice - 1)
                    print(f"Tarefa '{removida}' removida com sucesso!")
                else:
                    print("Número inválido.")
            else:
                print("Digite apenas números.")

    # Sair
    elif opcao == "4":
        print("Programa terminado.")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")