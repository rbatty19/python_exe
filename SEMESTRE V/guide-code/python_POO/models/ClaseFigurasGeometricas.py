from ClaseForma import Forma
from ClaseRectangulo import ClaseRectangulo
from ClaseTriangulo import ClaseTriangulo
from ClaseCirculo import ClaseCirculo

def main() :
    #Se crea una objeto tipo Figura Circulo
    circ=ClaseCirculo(7)
    #Se crea un objetio tipo Figura Rectangulo
    rect= ClaseRectangulo(4,5)
    #se crea un objeto tipo Figura Triangulo
    tria= ClaseTriangulo(3,4)
    #Se calculas las areas de cada figura
    circ.calcular_area()
    rect.calcular_area()
    tria.calcular_area()

main()   


   
    
    
    
