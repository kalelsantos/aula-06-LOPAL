# Lista de tarefas
# 1. Mostrar todas as tarefas
# 2. Mostrar tarefas concluídas
# 3. Mostrar tarefas pendentes
# 4. Mostrar tarefas por prioridade
# 5. Cadastrar nova tarefa
# 6. Finalizar tarefa
# 7. Remover tarefa
# 0. Sair

tarefas = [
    {"titulo":"estudar", "concluida":"[X]", "prioridade":"media"},
    {"titulo":"trabalhar", "concluida":"[ ]", "prioridade":"alta"},
    {"titulo":"ler", "concluida":"[ ]", "prioridade":"baixa"}
]

def mostrar():
    for tarefa in tarefas:
        print()
        print(f"{tarefa["concluida"]} {tarefa["titulo"]} | {tarefa["prioridade"]}")
        print()

# def mostrar_todas():
#     for tarefa in tarefas:
#         print(tarefa)

def mostrar_concluidas():
    for tarefa in tarefas:
        if tarefa["concluida"] == "[X]":
            print()
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} | {tarefa["prioridade"]}")
            print()

def mostrar_pendentes():
    for tarefa in tarefas:
        if tarefa["concluida"] == "[ ]":
            print()
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} | {tarefa["prioridade"]}")
            print()

def mostrar_prioridade():
    escolha = input("Você quer ver as tarefas com prioridade:\naltissima, alta, media ou baixa?\n")
    for tarefa in tarefas:
        if tarefa["prioridade"] == escolha:
            print()
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} | {tarefa["prioridade"]}")
            print()
           
def finalizar_tarefa():
    finalizar = input("Digite a tarefa que você dseja finalizar\n")
    for tarefa in tarefas:
        if tarefa["titulo"] == finalizar:
            tarefa["concluida"] = "[X]"

def remover_tarefa():
        remover = input("Digite o nome da tarefa que deseja remover\n")
        for tarefa in tarefas:
            if tarefa["titulo"] == remover:
                tarefas.remove (tarefa)
            break

def cadastrar_tarefa():
    titulo_tarefa_nova = input("Digite o título da nova tarefa\n")
    situacao_tarefa_nova = input("Digite a se a nova tarefa está ou não concluída ( [X] ou [ ] )\n")
    prioridade_tarefa_nova = input("Digite a prioridade da nova tarefa (altissima, alta, media ou baixa)\n")

    tarefas.append({"titulo":titulo_tarefa_nova, "concluida":situacao_tarefa_nova, "prioridade":prioridade_tarefa_nova})
    print(tarefas)

while True:
    print("------------------\n LISTA DE TAREFAS\n------------------\n1. Mostrar todas as tarefas\n2. Mostrar tarefas concluídas\n3. Mostrar tarefas pendentes\n4. Mostrar tarefas por prioridade\n5. Cadastrar nova tarefa\n6. Finalizar tarefa\n7. Remover tarefa\n0. Sair")
    print( )
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Mostrando todas as tarefas. . .")
        mostrar()
    elif opcao == "2":
        print("Mostrando apenas tarefas concluídas. . .")
        mostrar_concluidas()
    elif opcao == "3":
        print("Mostrando apenas tarefas pendentes. . .")
        mostrar_pendentes()
    elif opcao == "4":
        print("Mostrando tarefas pro prioridade. . . ")
        mostrar_prioridade()
    elif opcao == "5":
        print("Cadastrando nova tarefa. . .")
        cadastrar_tarefa()
    elif opcao == "6":
        print("Finalizando tarefa. . .")
        finalizar_tarefa()
    elif opcao == "7":
        print("Removendo tarefa. . .")
        remover_tarefa()
    elif opcao == "0":
        print("Saindo. . .")
        break
    else:
        print("Opção Inválida. Tente Novamente.")