import json


def abrirArchivo():
    miJSON=[]
    with open('menu.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def abrirArchivo():
    miJSON=[]
    with open('pagos.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("pagos.json","w") as outfile:
        json.dump(miData,outfile)               

def abrirArchivo():
    miJSON=[]
    with open('pedidos.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("pedidos.json","w") as outfile:
        json.dump(miData,outfile)   



print("   __________________________")
print("  | BIENVENIDO A MOLIPOLLITO |")
print("  |__________________________|")

print("\n1.Creación de pedidos\n2.Registrar los pagos\n3.Cambiar estado de los pedidos.\n4.cancelar pedido.\n5.Consultar pedidos.")
opc=int(input("Elige una opción: "))
print("")
miInfo=[]

if(opc==1):
     print("----------------------------------------------------")
     nuevaVenta = {}
     nuevaVenta["cliente"] = input("Nombre del cliente: ")
     nuevaVenta["categoria"] = input("Categoria del pedido: ")
     nuevaVenta["nombre"] = input("Nombre del pedido: ")
     nuevaVenta["precio"] = int(input("Precio del pedido: "))
     nuevaVenta["estado"] = input("Estado del pedido: ")
  
     miInfo = abrirArchivo()
     miInfo[0]["items"].append(nuevaVenta)
     guardarArchivo(miInfo)
     print("venta registrada exitosamente.")

elif(opc==3):
     miInfo=abrirArchivo()
     for i in miInfo[0]["items"]:
        print("---------------------------------------")
        print("INFORMES DE PEDIDOS ")
        print("")
        
        print("Productos vendidos:",i["producto"])
        print("Precio del producto:",i["preProducto"])


     miInfo=abrirArchivo()
     for i in miInfo[0]["pagos"]:
        print("---------------------------------------")
        print("INFORMES DE VENTAS")
        print("")
        
        print("Productos vendidos:",i["productoComprado"])
        print("Cantidad de producto comprado:",i["cantProductoComprado"])
        print("Ingresos totales:",i["preProductoComprado"])  