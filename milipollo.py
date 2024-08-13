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

print("\n1.Creación de pedidos\n2.Registrar los pagos\n3.Cambiar estado de los pedidos.\n4.cancelar pedido.")
opc=int(input("Elige una opción: "))
miInfo=[]