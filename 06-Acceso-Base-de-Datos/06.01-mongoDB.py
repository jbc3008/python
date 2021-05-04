from pymongo import MongoClient, collation
from pprint import pprint

## Establecer conexión con MongoDB (motor de base datos)
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

## Mostar el estado del servidor (motor de base de datos)
# Asignamos a la variable db el objeto que representa la base de datos admin
db = client.admin

# Ejecutamos comandos en la base de datos utilizando la función command
# El comando serverStatus nos retorna el estado del servidor en JSON
status = db.command("serverStatus")
#pprint(status)

## Trabajando con Datos
# Seleccionar la base de datos con la que vamos a trabajo
#northwindDB = client['Northwind']
northwindDB = client.Northwind

# Listar las colecciones de la base de datos
print(northwindDB.list_collection_names())

# Seleccionar una colección de la base de datos
#collection = client.Northwind.customers
#collection = client['Northwind']['customers']
#collection = northwindDB['customers']
collection = northwindDB.customers

# Utilizamos estimated_document_count() para saber el número de documentos en la colección
result = collection.estimated_document_count()

# Buscar documentos dentro de una colección
result = collection.find({'Country': 'USA'})
result = collection.find({'Country': 'USA'}).limit(3)
result = collection.find({'Country': 'USA'}).skip(5)
result = collection.find({'Country': 'USA'}).sort('City')
result = collection.find({'Country': 'USA'}).sort('City').limit(10).skip(5)
result = collection.find({'Country': 'USA', 'City': 'Portland'}).sort('City')
result = collection.find({'Country': { '$in' : ['USA', 'Mexico']}})
result = collection.find({'Country': { '$in' : ['USA', 'Mexico']}}).sort('City')

print("Número de documentos: ", result.count())
print("Número de documentos: ", collection.count_documents({'Country': 'USA'}))

print("Datos por leer: ", result.alive)

while (result.alive):
    cliente = result.next()
    pprint(cliente)

result.close()
print("Datos por leer: ", result.alive)


# Buscar documentos dentro de una colección y retornamos el primer documento encontrado
result = collection.find_one({'Country': 'USA'})
pprint(result)


customer = {
    "CustomerID": "DEMO2",
    "CompanyName": "Uno Comidad y Bebidas, SL",
    "ContactName": "Borja Cabeza",
    "ContactTitle": "Propietario",
    "Address": "Calle Gran Vía, 41",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28044",
    "Country": "Spain",
    "Phone": "(91) 200 20 20",
    "Fax": "(91) 200 20 21"
}

#idNewDocument = collection.insert_one(customer).inserted_id
#print('ID Nuevo Documento: ', idNewDocument)

query = {'CustomerID': 'DEMO2'}
newValues = { 
    "$set" : { 
        "CompanyName": "Restaurantes Dos, SL", 
        "Address": "Calle Serrano, 81", 
        "Phone": "(91) 400 80 80"
        } 
    }
result = collection.update_one(query, newValues)
print(result.matched_count, ' elementos encontrados.')
print(result.modified_count, ' elementos modificados.')
pprint(result)
pprint(collection.find_one(query))