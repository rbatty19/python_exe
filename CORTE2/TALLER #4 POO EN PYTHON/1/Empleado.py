class Empleado:
    id=""
    tId=""
    cargo=""
    sueldo= 0.0
    email=""
    telefono = 0
    empresa = " "

    def __init__ (self, id, tId, cargo, sueldo, email, telefono, empresa):
        self.id = id
        self.tId = tId
        self.cargo = cargo
        self.sueldo = sueldo
        self.email = email
        self.telefono = telefono
        self.empresa = empresa
     

    def getId(self):
        return self.id
    
    def getTid(self):
        return self.tId
         
    def getCargo(self):
        return self.cargo

    def getSueldo(self):
        return self.sueldo

    def getEmail(self):
        return self.email
    
    def getTelefono(self):
        return self.telefono

    def getEmpresa(self):
        return self.empresa

    


    def setId(self ,newId):
         self.id =newId

    def setTid(self ,newTid):
         self.tId =newTid

    def setCargo(self ,newCargo):
         self.cargo =newCargo

    def setSueldo(self, newSueldo):
         self.sueldo = newSueldo

    def setEmail(self ,newEmail):
         self.email =newEmail

    def setTelefono(self ,newTelefono):
         self.telefono =newTelefono

    def setEmpresa(self ,newEmpresa):
         self.empresa = newEmpresa
