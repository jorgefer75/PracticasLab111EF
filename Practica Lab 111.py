estudiantesNombres = ['Juan', 'Carlos', 'Miguel']
estudiantesApellidos = ['Sanchez', 'Rivera', 'Tejada']
estudiantesCI = ['8463443', '6156166','5579264']
estudiantesFechaNacimiento = ["01 \ 11 \ 1994", "08 \ 03 \ 2000", "25 \ 08 \ 1997"]
estudiantesTelefono = ['71201944', '72002015', '77568945']
def mostrarMenu():
    print('')
    print('Ingrese la opcion requerida: ')
    print('1. Mostrar la lista')
    print('2. Adicionar un estudiante')
    print('3. Editar información de un estudiante')
    print('4. Eliminar un estudiante')
    print('5. Consulta Salida cuarentena')
    print('6. Ver el Mayor de todos')
    print('0. Salir')
    print('')

def mostrarEstudiantes():
    print("-----------------------------------------------------------------")
    print("Nombres","|","Apellidos","|  ","CI","\t","\t|","Celular","\t|","Fecha de Nacimiento")
    print("-----------------------------------------------------------------")
    for i in range(len(estudiantesNombres)):
        print(estudiantesNombres[i],"\t|", estudiantesApellidos[i],"\t|", estudiantesCI[i],"\t|", estudiantesTelefono[i],"\t|",estudiantesFechaNacimiento[i])

def adicionarEstudiante():
    # nombres
    nuevoNombre = input('Ingrese los nombres del estudiante: ')
    estudiantesNombres.append(nuevoNombre)
    # apellidos
    estudiantesApellidos.append(input('Ingrese los apellidos del estudiante: '))
    # CI
    estudiantesCI.append(input('Ingrese el CI del estudiante: '))
    # Fecha de nacimiento
    dia=int(input("Ingrese el dia de nacimiento: "))
    mes = int(input("Ingrese el mes de nacimiento: "))
    year = int(input("Ingrese el año de nacimiento: "))
    estudiantesFechaNacimiento.append(f"{dia} \ {mes} \ {year}")
    # Telefono
    estudiantesTelefono.append(input('Ingrese el telefono del estudiante: '))
    print('Se han guardado los datos del nuevo estudiante')
    mostrarEstudiantes()
def eliminarEstudiante():
    posicion = estudiantesCI.index(input('Ingrese el Carnet de Identidad del estudiante a borrar: '))
    estudiantesNombres.pop(posicion)
    estudiantesApellidos.pop(posicion)
    estudiantesCI.pop(posicion)
    estudiantesFechaNacimiento.pop(posicion)
    estudiantesTelefono.pop(posicion)
    print('Se ha eliminado al estudiante.')
def consultaSalidaCuarentena():
    # Lun Mie Vie   impares
    # Mar Jue Sab   pares
    dia = input('Ingrese el dia que se desea validar (lun mie vie mar jue sab): ').lower()
    comparador = -1
    # LUN lun Lun LuN
    if dia in ['lun', 'mie', 'vie']:
        comparador = 1
        print('Los estudiantes que pueden salir son: ')
    elif dia in ['mar', 'jue', 'sab']:
        comparador = 0
        print('Los estudiantes que pueden salir son: ')
    else:
        print('Dia no registrado')                
    for i in range(len(estudiantesNombres)):
        if int(estudiantesCI[i]) % 2 == comparador:
            print(estudiantesNombres[i], "\t|", estudiantesApellidos[i], "\t|", estudiantesCI[i], "\t|",estudiantesTelefono[i], "\t|", estudiantesFechaNacimiento[i])
def editarEstudiante():
    cont=0
    x = input("Introduca el nombre del estudiante a editar: ")
    while cont < len(estudiantesNombres):
        if x==estudiantesNombres[cont].lower():
            ind = cont
            cont = cont + len(estudiantesNombres)
            estudiantesNombres.pop(ind)
            estudiantesNombres.insert(ind,input("Ingrese el Nombre: "))
            estudiantesApellidos.pop(ind)
            estudiantesApellidos.insert(ind, input("Ingrese el Apellido: "))
            estudiantesCI.pop(ind)
            estudiantesCI.insert(ind, input("Ingrese el CI: "))
            estudiantesTelefono.pop(ind)
            estudiantesTelefono.insert(ind, input("Ingrese el celular: "))
            estudiantesFechaNacimiento.pop(ind)
            dia = int(input("Ingrese el dia de nacimiento: "))
            mes = int(input("Ingrese el mes de nacimiento: "))
            year = int(input("Ingrese el año de nacimiento: "))
            estudiantesFechaNacimiento.insert(ind, f"{dia} \ {mes} \ {year}")
        cont = cont + 1
def mayoEdad():
    d = estudiantesFechaNacimiento
    vector = []
    for i in range(len(estudiantesNombres)):
        cad = d[i]
        a1 = cad[0:2]
        a2 = cad[5:7]
        a3 = cad[10:14]
        at = int(a1) + int(a2) + int(a3)
        vector.insert(i,at)
    ind = vector.index(min(vector))
    res = estudiantesNombres[ind]
    print("El mayor de todos es", res)
mostrarMenu()
while True:
    opcion = input()
    if opcion == '1':
        print("")
        mostrarEstudiantes()
        print()
        input("Presione ENTER para ir al MENU")
        mostrarMenu()
    elif opcion == '2':
        print('Ingrese los datos del nuevo estudiante')
        adicionarEstudiante()
        input("Presione ENTER para ir al MENU")
        mostrarMenu()
    elif opcion == '3':
        editarEstudiante()
        mostrarEstudiantes()
        input("Presione ENTER para ir al MENU")
        mostrarMenu()
    elif opcion == '4':
        eliminarEstudiante()
        mostrarEstudiantes()
        input("Presione ENTER para ir al MENU")
        mostrarMenu()
    elif opcion == '5':
        consultaSalidaCuarentena()
        input("Presione ENTER para ir al MENU")
        mostrarMenu()
    elif opcion == '6':
        mayoEdad()
        input("Presione ENTER para ir al MENU")
        mostrarMenu()
    else:
        break