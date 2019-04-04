class Vehiculo:
    id = ""
    conductor = ""
    placa  = ""

    def __init__ (self, id, conductor, placa):
        self.id = id
        self.conductor = conductor
        self.placa= placa

    def getId(self):
      return self.id
    def getConductor(self):
      return self.conductor
    def getPlaca(self):
       return self.placa

    def setId(self, newId):
       self.id= newId
    def setConductor (self, newConductor):
        self.conductor = newConductor
    def setPlaca( self , newPlaca):
        self.placa = newPlaca
