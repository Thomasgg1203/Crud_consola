from DataBase.con import DAO
import controller as cont
#Esta sera la principal interfaz del usuario
def clase_principal():
    #menu
    menu = '''
    ######__MENU__####
    1. Listar personas
    2. Insertar personas
    3. Actualizar personas
    4. Eliminar personas
    5. Salir
    ##################
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

#Codigo para ejecutar el menu
clase_principal()
