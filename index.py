from DataBase.con import DAO
import controller as cont
#Esta sera la principal interfaz del usuario
def clase_principal():
    #menu
    menu = '''
    ######__MENU__######
    1. Listar personas
    2. Insertar personas
    3. Actualizar personas
    4. Eliminar personas
    5. Salir
    ####################
    '''
    opc = 0
    while(opc != 5):
        print(menu, "\n")
        opc = input("Por favor ingrese una opcion: ")
        opc = int(opc)
        if(opc > 5 or opc < 1):
            print("\nPor favor ingrese los valores bien")
        else:
            if(opc == 1):
                persona = DAO()
                datos = persona.listar_personas()
                cont.imprimir_datos(datos)
            elif(opc == 2):
                print("Insertar datos")
                persona = DAO()
                datos = persona.listar_personas()
                datos_insertar = cont.recibir_datos(datos)
                #Envio de datos para insertar en la base de datos
                bien = persona.insertar_personas(datos_insertar)
                if(bien):
                    print("Datos insertados correctamente")
                else:
                    print("Datos incorrectos al insertar\n")
            elif(opc == 3):
                print("Actualizar datos")
            elif(opc == 4):
                print("Eliminar datos")
            elif(opc == 5):
                print("Muchas Gracias Por Usar El Sistema :D")
            else:
                print("Error, vuelva ingrasar un dato igual al menu")


#Codigo para ejecutar el menu
clase_principal()
