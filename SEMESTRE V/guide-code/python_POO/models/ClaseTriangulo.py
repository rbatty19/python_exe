from ClaseForma import Forma


class ClaseTriangulo(Forma):

    def __init__(self,base, altura):
        Forma.__init__(self, "Triangulo")
        #Se inicializan los atributos de la figura Triangulo
        self.base=base
        self.altura=altura

    #Se calcula el area de la figura Triangulo
    def calcular_area(self):
        print("El area del Triangulo es ",(self.base * self.altura)/2) 