class Point:
    #Constructor de la Clase
    def __init__(self, x, y):
        #se inicializan las variables de instancia de la clase
        print("Inicializando los valores del Objeto Punto")
        self.x = x
        self.y = y

    #Metodo de la Clase Punto
    def distance_from_origin(self):
        print("Calculando distancia del origen")
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    #Metodo de clase para imprimir el objeto punto
    def print_point(self):
        print('({0}, {1})'.format(self.x, self.y))  