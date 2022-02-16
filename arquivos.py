bd = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        bd.append(registro.split(","))

print(bd)

print(float(bd[0] [0]) + float(bd[0] [1]))