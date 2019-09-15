from ClaseMoto import Moto

def main():
    #Acceso a la Variable de Clase, de manera directa, sin instancia
    print("Numero de Ruedas por defecto, Objeto Moto: ",Moto.n_ruedas)
    #Creacion de un Objeto de la clase Moto
    m=Moto("Yamaha",100,"Roja")
    print("Acceso a la variable de Clase por medio de la instancia del Objeto Moto:", m.n_ruedas)



main()