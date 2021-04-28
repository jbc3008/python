#####################################################################
# Clases                                                            #
#####################################################################
#                                                                   #
#   Sintaxis: class [nombre de la clase]):                          #
#                                                                   #
#   Ejemplos:                                                       #
#       class Alumno:                                               #    
#                                                                   #
#####################################################################

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

    def getNombreCompleto(self) -> None:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

    def setFechaNacimiento(self, fecha) -> None:
        try:
            if(len(fecha) == 8):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()            
        except:
            pass

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None): 
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento.year

#Instanciamos el Objeto, se ejecuta la función constructor
alumno = Alumno("Borja", "Cabeza", "Rozas")

#Invocamos a las funciones del objeto
alumno.setFechaNacimiento("11-09-95")
print(f"Edad: {alumno.getEdad()}")
