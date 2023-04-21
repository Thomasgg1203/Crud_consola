#Archivo que manejara la infor
from tabulate import *

def imprimir_datos(datos) -> None:
    print("Listado de personas")
    print(tabulate(datos, 
                   headers = ['ID', 'Documentos', 'Nombres', 'Apellidos', 'Edades'],
                   tablefmt= 'fancy_grid'))
    print(" ")