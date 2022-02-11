'''Procure criar um arquivo chamado DesafioDecisao.py e elaborar o código para resolver a seguinte situação: 
o seu módulo solicitará o nível de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e o gênero dessa pessoa, 
caso o nível seja ADM, ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres.
Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres. Se o nível for 
GUEST, a mensagem deverá ser “Olá visitante”. E se o nível digitado for diferente de ADM, USR ou GUEST deverá exibir 
a mensagem “Olá desconhecido(a)”. Considere apenas os gêneros masculino e feminino e não olhe o código abaixo, até 
resolver o seu desafio.'''

nivel_acess = input("Digite nivel de acesso: ").upper()
genero = input("Digite a letra correspondente ao seu genero:\nM= Masculino \nF=Feminino \nLetra: ").upper()

if (nivel_acess == "ADM") and (genero == "M"):
    print("Olá Administrador")

elif (nivel_acess == "ADM") and (genero == "F"):
    print("Olá Administradora")

elif (nivel_acess == "USR") and (genero == "M"):
    print("Olá Usuario")

elif (nivel_acess == "USR") and (genero == "F"):
    print("Olá Usuaria")

elif (nivel_acess == "GUEST"):
    print("Olá visitante")

else:
    print("Olá desconhecido(a)")


#Resolução:

nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero1=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero1=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero1=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
