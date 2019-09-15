from ClaseForma import Forma


class ClaseRectangulo(Forma):

    def __init__(self,base, altura):
        Forma.__init__(self, "Rectangulo")
        #se inicializan los atributos de la figura rectangulo
        self.base=base
        self.altura=altura

    #se calcula el area de la figura rectangulo
    def calcular_area(self):
        super().calcular_area()
        print("El area del Rectangulo es = ",self.base * self.altura)    

