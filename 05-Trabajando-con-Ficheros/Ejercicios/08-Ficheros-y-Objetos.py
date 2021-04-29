def BuscarClienteID(item):
    if(item.Identificador == "1562"):
        return True
    else:
        return False

class Cliente:
    Identificador   = None
    Nombre          = None
    Apellidos       = None
    Genero          = None
    Pais            = None
    FechaNacimiento = None

    def __init__(self, id, nombre, apellidos) -> None:
        self.Identificador = id
        self.Nombre = nombre
        self.Apellidos = apellidos

################################################################################

clientes = []
path = ".\\Ficheros\\fichero.txt"
file = open(path)

for linea in (file.readlines()):
    data = linea.split(",")
    if(data[0].isdigit() == True):    
        #clientes.append(Cliente(data[7], data[1], data[2]))  
        cliente = Cliente(data[7].strip(), data[1].strip(), data[2].strip())
        clientes.append(cliente)

file.close()
print(f"{len(clientes)} clientes importados.")

print(clientes[0].Identificador)

resultado = list(filter(BuscarClienteID, clientes))
print(len(resultado))

