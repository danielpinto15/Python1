

tarefas = []

while True:
    # menu
    print("\n--- Lista de Tarefas ---")
    print("1 - Adicionar Tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

    user_selection = input("Escolha uma opção: ")

    #função para adicionar tarefas
    if user_selection == "1":
        tarefa = input("Adicione uma tarefa: ")

        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")      

    #ver se o input tem algum texto . a tarefa não pode estar vazia

    #função para ver as tarefas
    elif user_selection == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa")
        else:
            print("Esta é a tua lista: ")

            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1} . {tarefa}")
    #função para remover uma tarefa
        #o user vai ter de escolher uma tarefa para remover. input a receber um numero, ir a nossa lista e apagar a tarefa correspondente a esse numero.

    #função para sair do programa, usar o break
    elif user_selection == "4":
        print("Programa terminado")
        break

    #controlo de erros
    else:
        print("Opção Invalida. Tente outra vez!")
    