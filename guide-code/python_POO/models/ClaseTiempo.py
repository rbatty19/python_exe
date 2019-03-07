class Time:
    #Constructor de la Clase Tiempo
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    #Se define el metodo imprimir para el Objeto Time
    def print_time(self):
        s = "{0}:{1:02d}:{2:02d}"
        print(s.format(self.hours, self.minutes, self.seconds))