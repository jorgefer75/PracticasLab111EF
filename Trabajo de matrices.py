def mostrarmat(matriz, n):
    for i in range(n):
        for j in range(n):
            print("\t", matriz[i][j], end="")
        print()
def MatrizU(n):
    a = 0
    b = n - 1
    valor = 1
    matriz = [[0 for i in range(n)] for j in range(n)]
    if n % 2 == 0:
        le = len(matriz) // 2
    else:
        le = (len(matriz) // 2) + 1
    l = len(matriz)
    v = 0
    vam = le - 2
    for j in range(le):
        for i in range(0, l):
            matriz[a][i] = valor
            valor = valor + 1
        for i in range(a + 1, l):
            matriz[i][b] = valor
            valor = valor + 1
        for i in range(b - 1, v - 1, -1):
            matriz[b][i] = valor
            valor = valor + 1
        if n % 2 != 0:
            if j == vam:
                v = v + 10
        l = l - 1
        a = a + 1
        b = b - 1
    return(mostrarmat(matriz, n))


def MatrizSubeBaja(n):
    a=-1
    b=n-1
    valor=1
    matriz = [[0 for i in range(n)] for j in range(n)]
    l=len(matriz)
    if n % 2==0:
        le=len(matriz)//2
    else:
        le = (len(matriz) // 2)+1
    for j in range(le):
        a=a+1
        if matriz [n-1][n-1]!=n*n:
            for i in range(0, l):
                matriz[i][a] = valor
                valor = valor + 1
            a=a+1
        if matriz [n-1][n-1]!=n*n:
            for i in range(l-1, -1,-1):
                matriz[i][a] = valor
                valor = valor + 1
                b=b-1
    return (mostrarmat(matriz, n))
def MatrizCaracol(n):
    a=0
    b= n - 1
    valor=1
    matriz = [[0 for i in range(n)] for j in range(n)]
    for j in range(0,len(matriz)):
        for i in range(a,b+1):
            matriz[a][i]=valor
            valor = valor + 1
        for i in range(a+1,b+1):
            matriz[i][b]=valor
            valor = valor + 1
        for i in range(b-1,a-1,-1):
            matriz[b][i] = valor
            valor = valor + 1
        for i in range(b - 1, a, -1):
            matriz[i][a] = valor
            valor = valor + 1
        a=a+1
        b=b-1
    return (mostrarmat(matriz, n))
def Matriz_L(n):
    lim= n * n
    b=0
    matriz = [[0 for i in range(n)] for j in range(n)]
    c=0
    a=len(matriz)-1
    for j in range(0,len(matriz)):
        for i in range(len(matriz)-1,c-1, -1):
            matriz[i][c] = lim
            lim = lim - 1
        for i in range(b+1,len(matriz)):
            matriz[b][i] = lim
            lim = lim - 1
        b=b+1
        a=a-1
        c = c + 1
    return (mostrarmat(matriz, n))

def MatrizTriangular(n):
    a = 0
    b = n - 1
    valor = 1
    matriz = [["" for i in range(n)] for j in range(n)]
    le = len(matriz)
    for j in range(le):
        for i in range(a, len(matriz)):
            matriz[b][i] = valor
            valor = valor + 1
            b = b - 1
        a = a + 1
        b = len(matriz) - 1
    return (mostrarmat(matriz, n))

def Matriz_Diagonal(n):
    matriz = [[0 for i in range(n)] for j in range(n)]

    b = 1; valor = 1; cont = 1; aux = 1; g = 1; n1 = 0

    b2=len(matriz)-1; cont2=len(matriz)-1; a2=1; g2=1; d=0

    for j in range(0,len(matriz)*2):
        if n1==len(matriz):
            aux2 = len(matriz)-1
            g2 = 1
            for i in range(0, cont2):
                matriz[d+g2][aux2] = valor
                valor = valor + 1
                aux2 = aux2 - 1
                g2 = g2 + 1
            b2 = b2 - 1
            cont2 = cont2 - 1
            d = d + 1
        else:
            aux = 0
            g = 1
            for i in range(0, cont):
                matriz[aux][b-g] = valor
                valor = valor + 1
                g = g + 1
                aux = aux + 1
            cont=cont+1
            b = b + 1
            n1 = n1 + 1
    return (mostrarmat(matriz, n))


def menu():
    print ("Selecciona una opción")
    print ("\t1.- Matriz en U")
    print ("\t2.- Matriz Sube Baja")
    print ("\t3.- Matriz Caracol")
    print("\t4.- Matriz en L")
    print ("\t5.- Matriz Triangular")
    print ("\t6.- Matriz en Diagonal")
    print ("\t7.- Salir")
while True:
    menu()
    opcionMenu=input("Elige una opcion: ")
    if opcionMenu == "1":
        n=int(input("Ingresa el tamano de la matriz: "))
        MatrizU(n)
    elif opcionMenu == "2":
        n = int(input("Ingresa el tamano de la matriz: "))
        MatrizSubeBaja(n)
    elif opcionMenu == "3":
        n = int(input("Ingresa el tamano de la matriz: "))
        MatrizCaracol(n)
    elif opcionMenu == "4":
        n = int(input("Ingresa el tamano de la matriz: "))
        Matriz_L(n)
    elif opcionMenu == "5":
        n = int(input("Ingresa el tamano de la matriz: "))
        MatrizTriangular(n)
    elif opcionMenu == "6":
        n = int(input("Ingresa el tamano de la matriz: "))
        Matriz_Diagonal(n)
    elif opcionMenu == "7":
        print("Finalizado")
        break
    else:
        print("Escoja una opcion que exista...")