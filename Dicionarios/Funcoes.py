def perguntar():
    return input("O que deseja realizar ? \n"+
                 "I - Inserir\n"+
                 "A - Alterar\n"+
                 "E - Excluir\n"+
                 "L - Listar ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                  input("Digite a última data de acesso: ").upper(),
                                                  input("Qual a última estação acessada: ").upper()]