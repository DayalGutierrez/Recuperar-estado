import os, time
from agenda import Agenda

agend = Agenda()

agend.cargar()

while(True):
    os.system("cls")
    print('Menu de opciones')
    print('\t1. Aniadir nueva entrada a Agenda')
    print('\t2. Borrar de agenda')
    print('\t3. Mostrar agenda completa')
    print('\t4. Eliminar agenda completa')
    print('\t0. Salir')
    opc = int(input('Dame el valor de la opcion a realizar: '))

    
    if (opc == 1):
        nombre = input('Dame el nombre de la nueva entrada: ')
        apellido = input('Dame el(los) apellido(s): ')
        codigo = int(input('Dame el codigo: '))
        telefono = int(input('Dame el telefono: '))
        carrera = input('Dame la carrera: ')
        agend.aniadir_nuevo(nombre, apellido, codigo, telefono, carrera)

        print('\nEntrada agregada con exito!')
        time.sleep(1)

    elif (opc == 2):
        codigo = int(input('Dame el codigo de la entrada a buscar: '))

        if (agend.borrar_elem(codigo)):
            print('Contacto eliminado con exito')
        else:
            print(f'Entrada con codigo {codigo} no encontrado')

        input('Presione enter para volver al menu ')
    elif (opc == 3):
        agend.mostrar()
        input('Presione enter para regresar al menu')
    elif (opc == 4):
        agend.limpiar()
        print('Agenda eliminada completamente')
        input('Presione enter para regresar al menu ')
    elif (opc == 0):
        break
    else:
        print('Valor de opcion no valido')
        time.sleep(1)

