#Se importa del Paquete Point la Clase Point
from ClaseTiempo import Time

def main():
    #Se crea un objeto de la Clase Tiempo con paso de los parametros
    t=Time(4,30,50)
    #Se imprime los valores del Objeto Tiempo
    t.print_time()
    #Se imprime los valores actuales del Objeto Punto
    #Se crea un objeto de la Clase Tiempo sin parametros y con los valores por defecto
    t=Time()
    #Se imprime los valores del Objeto Tiempo
    t.print_time()
    #Se crea un Objeto de la Clase Tiempo pasando un parametro
    t=Time(9)
    #Se imprime los valores del Objeto Tiempo
    t.print_time()


#Se ejecuta la funcion principal
main()