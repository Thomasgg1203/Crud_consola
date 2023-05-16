#Parte donde ira la conexion de la base de datos
#librerias
import mysql.connector
from mysql.connector import Error

#Clase que permitira enviar datos
class DAO():
    #Conector
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='consola_crud')
        except Error as e:
            print("Error de conexcion {0}".format(e))

    #metodo para traer los datos de persona
    def listar_personas(self) -> list:
        if(self.connection.is_connected()): #Verificar que este el conector bien
            try:
                cursor = self.connection.cursor()
                sql = "SELECT * FROM personas ORDER BY documento ASC;"
                cursor.execute(sql)
                personas = cursor.fetchall()
                cursor.close() 
                return personas
            except Error as e:
                print("Error en listar persona, {0}".format(e))
    
    #metodo para insertar datos a la tabla persona
    def insertar_personas(self, datos_insert) -> None:
        if(self.connection.is_connected()):
            try:
                cursor =  self.connection.cursor()
                sql = "INSERT INTO `personas`(`documento`, `nombre`, `apellido`, `edad`) VALUES('{0}','{1}','{2}','{3}');"
                cursor.execute(sql.format(datos_insert[0], datos_insert[1], 
                                          datos_insert[2], datos_insert[3]))
                self.connection.commit()
                cursor.close()
                return True
            except Error as e:
                print("Error al insertar persona, {0}".format(e))

