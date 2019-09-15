class Forma(object):
    def __init__(self, figura):
        #Se inicializan los atributos de la clase
        self.figura=figura
        print('Creando un Objeto de tipo ',self.figura)

    def calcular_area(self):
        #calculo del area
        print('Area de ',self.figura, "calculada.u")    