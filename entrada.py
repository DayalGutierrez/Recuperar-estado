class Entrada:
    def __init__(self, nombre = "", apellido = "", codigo = 0, telefono= 0, carrera = ""):
        self.__nombre =  nombre
        self.__apellido = apellido
        self.__codigo = codigo
        self.__telefono = telefono
        self.__carrera = carrera

    def __str__(self):
        entrada = "\t" + self.__nombre + " " + self.__apellido
        entrada += "\nCodigo: " + str(self.__codigo)
        entrada += "\nTelefono: " + str(self.__telefono)
        entrada += "\nCarrera: " + self.__carrera
        return entrada

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def codigo(self):
        return self.__codigo

    @property
    def telefono(self):
        return self.__telefono

    @property
    def carrera(self):
        return self.__carrera