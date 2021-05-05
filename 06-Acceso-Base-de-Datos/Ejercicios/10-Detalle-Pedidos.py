from itertools import product
from pymongo import MongoClient

#Cliente
client = MongoClient('mongodb://localhost:27017/')

#Base de Datos
db = client.Northwind

#Colecciones
orders = db.orders
details = db.order_details
products = db.products


idPedido = input("Identificador del Pedido: ")

pedido = orders.find_one({ 'OrderID' : idPedido })
if(pedido != None):
    print(f"===============================================================")
    print(f" DATOS DEL PEDIDO {idPedido}")
    print(f"===============================================================")
    print(f" Entregar : {pedido['ShipName']}")
    print(f"            {pedido['ShipAddress']}")
    print(f"            {pedido['ShipCity']} ({pedido['ShipCountry']})")
    print("")
    # Buscamos el detalle del pedido
    detalle = details.find({ 'OrderID' :  idPedido })
    # Recorremos con While el curso del detalle del pedido
    while(detalle.alive):
        linea = detalle.next()
        # Buscasmos y mostramos la descripción del producto, utilizando ProductID
        producto = products.find_one({ 'ProductID' : linea['ProductID']})
        # Mostramos cada linea de pedido
        # Descripción  -  cantidad  - precio  -  precio * cantidad
        total = int(linea['Quantity']) * float(linea['UnitPrice'])
        print(f"  {producto['ProductName']:<35} {linea['Quantity']:>6} {linea['UnitPrice']:>8} {total:>8}")

    #Mostar el importe total del pedido
else:
    print(f"El pedido {idPedido} no existe.")
