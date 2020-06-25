def mostrarmat(matriz,n):
    for i in range(n):
        for j in range(n):
            print("\t",matriz[i][j],end="")
        print()

fila=4
b=1
valor=1
cont=1
aux=1
g=1
matriz = [[0 for i in range(fila)] for j in range(fila)]
for j in range(0,len(matriz)):
    aux=1
    g=1
    for i in range(0,cont):
        matriz[aux-1][b-g]=valor
        valor = valor + 1
        g=g+1
        aux=aux+1
    cont=cont+1
    b=b+1
mostrarmat(matriz,fila)