class Terrestre(Vehiculo):
    carretera =""
    id=""
    conductor=""
    placa=""
    def __init__ (self, carretera, id, conductor, placa):
        Vehiculo.__init__(self, id, conductor, placa)

x = Terrestre ("campeche", "00", "lucho","rbv456")
 
print(x)

