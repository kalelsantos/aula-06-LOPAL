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
    {"titulo":"estudar", "concluida":"sim", "prioridade":"media"},
    {"titulo":"trabalhar", "concluida":"nao", "prioridade":"alta"},
    {"titulo":"ler", "concluida":"nao", "prioridade":"baixa"}
]

def mostrar_todas():
    for tarefa in tarefas:
        print(tarefa)

def mostrar_concluidas():
    for tarefa in tarefas:
        if tarefa["concluida"] == "sim":
            print(tarefa)

def mostrar_pendentes():
    for tarefa in tarefas:
        if tarefa["concluida"] == "nao":
            print(tarefa)

def mostrar_prioridade():
    escolha = input("Você quer ver as tarefas com prioridade:\naltissima, alta, media ou baixa?\n")
    for tarefa in tarefas:
        if tarefa["prioridade"] == escolha:
            print(tarefa)

def finalizar_tarefa():
    finalizar = input("Digite a tarefa que você dseja finalizar\n")
    for tarefa in tarefas:
        if tarefa["titulo"] == finalizar:
            tarefa["concluida"] = "sim"

def remover_tarefa():
        remover = input("Digite o nome da tarefa que deseja remover\n")
        for tarefa in tarefas:
            if tarefa["titulo"] == remover:
                tarefas.remove (tarefa)
            break

def cadastrar_tarefa():
    titulo_tarefa_nova = input("Digite o título da nova tarefa\n")
    situacao_tarefa_nova = input("Digite a se a nova tarefa está ou não concluída (sim ou nao)\n")
    prioridade_tarefa_nova = input("Digite a prioridade da nova tarefa (altissima, alta, media ou baixa)\n")

    tarefas.append({"titulo":titulo_tarefa_nova, "concluida":situacao_tarefa_nova, "prioridade":prioridade_tarefa_nova})
    print(tarefas)

while True:
    print("------------------\n LISTA DE TAREFAS\n------------------\n1. Mostrar todas as tarefas\n2. Mostrar tarefas concluídas\n3. Mostrar tarefas pendentes\n4. Mostrar tarefas por prioridade\n5. Cadastrar nova tarefa\n6. Finalizar tarefa\n7. Remover tarefa\n0. Sair")
    print( )
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_todas()
    elif opcao == "2":
        mostrar_concluidas()
    elif opcao == "3":
        mostrar_pendentes()
    elif opcao == "4":
        mostrar_prioridade()
    elif opcao == "5":
        cadastrar_tarefa()
    elif opcao == "6":
        finalizar_tarefa()
    elif opcao == "7":
        remover_tarefa()
    elif opcao == "0":
        print("Saindo. . .")
        break
    else:
        print("Opção Inválida. Tente Novamente.")
