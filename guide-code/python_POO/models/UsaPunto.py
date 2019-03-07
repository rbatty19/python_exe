#Se importa del Paquete Point la Clase Point
from ClasePunto import Point

def principal():
    #Se crea un objeto de la Clase Punto
    p=Point(10,20)
    #Se invoca al metodo de calculo de la distancia
    p.distance_from_origin()
    #Se imprime los valores actuales del Objeto Punto
    p.print_point()


#Se ejecuta la funcion principal
principal()


  