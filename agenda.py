import os
from entrada import Entrada

class Agenda:
    def __init__(self):
        self.__contactos = []


    def aniadir_nuevo(self, nombre, apellido, codigo, telefono, carrera):
        nuevo = Entrada(nombre, apellido, codigo, telefono, carrera)
        self.__contactos.append(nuevo)
        self.guardar()

    def mostrar(self):
        for contacto in self.__contactos:
            print(contacto)
    
    def limpiar(self):
        self.__contactos.clear()

    def borrar_elem(self, elem):
        for i in range(len(self.__contactos) ):
            if self.__contactos[i].codigo == str(elem):
                del self.__contactos[i]
                self.guardar()
                return True
        return False


    def guardar(self):
        file = open('agenda.txt', 'w')
        for contacto in self.__contactos:
            file.write(contacto.nombre + '*')
            file.write(contacto.apellido + '*')
            file.write(str(contacto.codigo) + '*')
            file.write(str(contacto.telefono) + '*')
            file.write(str(contacto.carrera) + '\n')
        file.close()
        if (os.path.exists('agenda.txt')):
            return True
        else:
            return False
    
    def cargar(self):
        if (os.path.exists('agenda.txt')):
            self.__contactos.clear()
            file = open('agenda.txt', 'r')
            for line in file:
                contacto = line[:-1].split('*',4)
                nuevo = Entrada(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4])

                self.__contactos.append(nuevo)
            return True
        else:
            return False
