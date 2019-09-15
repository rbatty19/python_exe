class Estudiantes:
    id = ""
    identificacion = ""
    tIdentificacion = ""
    nombre = ""
    programaAcademico = ""
    semestre =  0
    institucion = ""

    def __init__ (self, id, identificacion, tIdentificacion,nombre,programaAcademico, semestre, institucion):
        self.id = id
        self.identificacion = identificacion
        self.tIdentificacion = tIdentificacion
        self.nombre = nombre
        self.programaAcademico = programaAcademico 
        self.semestre = semestre
        self.institucion = institucion

    def getId(self):
        return self.id

    def getIdentificacion(self):
       return self.identificacion

    def getTidentificacion(self):
       return self.tIdentificacion

    def getNombre (self):
       return self.nombre

    def  getProgramaAcademico(self):
       return self.programaAcademico

    def getSemestre(self):
       return self.semestre

    def  getIntituciion (self):
      return self.institucion

    
    def setId(self, newId):
       self.id= newId

    def setIdentificacion(self, newIdentificacion):
       self.identificacion= newIdentificacion

    def setTidentificacion(self, newTidentificacion):
       self.tIdentificacion= newTidentificacion

    def setNombre(self, newNombre):
       self.nombre= newNombre
     
    def setProgramaAcademico(self, newProgramaAcademico):
       self.programaAcademico= newProgramaAcademico

    def setSemestre (self, newSemestre):
        self.semestre= newSemestre

    def setIntitucion (self, newIntitucion):
        self.institucion = newIntitucion


    
    

