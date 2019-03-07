from ClaseForma import Forma
from math import pi


class ClaseCirculo(Forma):
        
    def __init__(self,radio):
        Forma.__init__(self, "Circulo")
        #se inicializan los atributos de la figura Circulo
        self.r=radio

    #se calcula el area de la figura Circulo
    def calcular_area(self):
        print("El area del Circulo es: ", pi * self.r*self.r)  

#a=ClaseCirculo(5)