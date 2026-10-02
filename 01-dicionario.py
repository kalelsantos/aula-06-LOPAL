aluna = {"nome":"Rebecca", "nota":10, "tel":"1192447934"}

clientes = [
    {"nome":"Link", "tel":"1192123", "empresa":"NINTENDO"},
    {"nome":"Charmander", "tel":"1195497", "empresa":"INTEL"},
    {"nome":"Pikachu", "tel":"1190053", "empresa":"XBOX"},
    {"nome":"Rebecca", "tel":"1190502", "empresa":"XBOX"}
]

for cliente in clientes:
    print(cliente) # Código para mostrar os clientes

# for cliente in clientes:
#     if cliente["empresa"] == "INTEL":
#         print(cliente) # Código para mostrar clientes apenas com algo em especifico, 
                       # como quem trabalha na empresa INTEL

# escolha = input("Você quer ver quem trabalha em qual empresa?\n").upper().strip()
# for cliente in clientes:

#     if cliente["empresa"] == escolha:
#         print(cliente["nome"])

# nome_ncliente = input("Digite o nome do novo cliente\n").capitalize()
# tel_ncliente = input('Digite o telefone do novo cliente como "11XXXXX"\n')
# empresa_ncliente = input("Digite a empresa do novo cliente\n").upper()

# clientes.append({"nome":nome_ncliente, "tel":tel_ncliente, "empresa":empresa_ncliente})
# print(clientes)

# Remover um cliente

# del_nome_cliente = input("Digite o nome do cliente que deeseja remover\n").capitalize
# del_tel_cliente = input("Digite o telefone do cliente que deseja remover\n")
# del_empresa_cliente = input("Digite a empresa do cliente que deseja remover\n").upper

# clientes.remove({"nome":del_nome_cliente, "tel":del_tel_cliente, "empresa":del_empresa_cliente})
# print(clientes)

# print("<------- Removendo um cliente pelo nome")

remover_nome = input("Digite o nome do cliente que deseja remover\n").capitalize()
for cliente in clientes:
    if cliente["nome"] == remover_nome:
        clientes.remove (cliente)
        break

# print(clientes)