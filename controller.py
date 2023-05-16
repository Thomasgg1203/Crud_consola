#Archivo que manejara la infor
from tabulate import *

def imprimir_datos(datos) -> None:
    print("Listado de personas")
    print(tabulate(datos, 
                   headers = ['ID', 'Documentos', 'Nombres', 'Apellidos', 'Edades'],
                   tablefmt= 'fancy_grid'))
    print(" ")

def recibir_datos(datos) -> list:
    docBol, nomBol, apeBol, edadBol = True, True, True, True
    print("Ingrese los siguientes datos:\n")
    while(True):
        #validar que ya exista doc
        if(docBol):
            doc = input("Ingrese documento: ")
            if(doc.isdigit()):#validar que son digitos
                doc = int(doc)
                #validar que no este la base de datos
                bien = False
                for i in range(0, len(datos), 5):
                    if(doc == datos[i+2]):
                        bien = True
                        break

                if(bien):
                    print("Datos repetidos, por favor vuelva a ingresar los datos")
                else:
                    docBol = False

            else: 
                print("Por favor ingrese datos numericos")
                continue
        
        #validar que el nombre ya exista
        if(nomBol):
            nom = input("Ingrese el nombre: ")
            nomBol = False
        
        #validar que el apellido ya exista
        if(apeBol):
            ape = input("Ingrese el apellido: ")
            apeBol = False
        
        #validad que la edad ya exista
        if(edadBol):
            eda = input("Ingrese la edad: ")
            if(eda.isdigit()):
                edadBol = False
            else:
                print("Por favor ingrese la edad bien")

        #validar que todos esten bien :D
        if(docBol != True and nomBol != True and apeBol != True and edadBol != True):
            print("Datos registrados correctamente")
            break
    datos_a_inser = (doc, nom, ape, eda)

    return datos_a_inser    
