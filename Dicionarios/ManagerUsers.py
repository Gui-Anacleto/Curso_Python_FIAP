from Dicionarios.Funcoes import *
users = {}
opcao = perguntar()
while opcao == "I" or opcao == "A" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(users)
    opcao = perguntar()