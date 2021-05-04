from datetime import datetime

#Creamos una clase utilizando class
class Alumno:
    #Variables o Propiedades de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    #Función constructor se ejecuta al crear el objeto
    #self represente al mismo objeto
    def __init__(self, nombre, apell1, apell2) -> None:
        self.Nombre = nombre
        self.Apellido1 = apell1
        self.Apellido2 = apell2

    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if(len(fecha) == 8):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()

            return True           
        except:
            return False

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None): 
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento.year


