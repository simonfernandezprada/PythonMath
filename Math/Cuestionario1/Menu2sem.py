from os import system

lista_nombres = []
lista_edades = []

validador = True

while validador:
    system('cls')
    print('BIENVENID@ AL SISTEMA')
    print('[1] - ALMACENAR NUEVA PERSONA')
    print('[2] - BUSCAR PERSONA POR NOMBRE')
    print('[3] - LISTAR TODAS LAS PERSONAS')
    print('[X] - SALIR')
    respuesta = input('SELECCIONE UNA OPCIÓN: ')

    if respuesta == "1":
        system('cls')

        nombre = input("INGRESE NOMBRE: ")
        edad = -1

        while edad < 0:
            try:
                edad = int(input("INGRESE EDAD: "))
            except:
                edad = -1

        lista_nombres.append(nombre)
        lista_edades.append(edad)

        print("PERSONA ALMACENADA CORRECTAMENTE")
        input("PARA CONTINUAR PRESIONE ENTER...")
    elif respuesta == "2":
        system('cls')

        nombreBuscar = input("INGRESE NOMBRE A BUSCAR: ")
        validadorPersona = False

        for i in range(len(lista_nombres)):
            if nombreBuscar == lista_nombres[i]:
                validadorPersona = True
                print(
                    f'NOMBRE: {lista_nombres[i]} - EDAD: {lista_edades[i]} AÑOS')

        if validadorPersona == False:
            print('PERSONA NO ENCONTRADA')

        input("PARA CONTINUAR PRESIONE ENTER...")
    elif respuesta == "3":
        system('cls')

        for i in range(len(lista_nombres)):
            print(
                f'NOMBRE: {lista_nombres[i]} - EDAD: {lista_edades[i]} AÑOS')

        input('PRESIONE ENTER PARA CONTINUAR')
    elif respuesta == 'X' or respuesta == 'x':
        validador = False

print("GRACIAS POR UTILIZAR NUESTRO SISTEMA")
