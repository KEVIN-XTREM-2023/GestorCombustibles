import mysql.connector
import base64
try:
    database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "gestion_combustible"
    )
    print("------------------ Conexion Exitosa ------------------------")
except :
    print("-------------- Conexion Fallida ---------------------")


def ingresar_datos(nombre,apellido,password):


    cursor = database.cursor(buffered= True)

    clientes = [
        (nombre,apellido,password)
        ]
            
    cursor.executemany("INSERT INTO clientes VALUES(null,%s,%s,%s)", clientes)
    database.commit()




def visualizar_datos():
    cursor = database.cursor(buffered= True)
    print("----- Cliente ------")
    """
    cursor.execute("SELECT *FROM clientes  ")
    result = cursor.fetchall()
    for cliente in result :
        print(cliente[0],cliente[1],cliente[2] )
    """

    cursor.execute("SELECT *FROM clientes  ")
    cli = cursor.fetchone()
    #print(cli)


def buscar_cliente(nombre, apellido):

    cursor = database.cursor(buffered= True)
    cursor.execute("SELECT *FROM clientes  ")
    result = cursor.fetchall()
    for cliente in result :
        
        if cliente[1] == nombre and cliente[2] == apellido:
            print ("-------------------- Se enocontro el dato Y no se puede volver ha registrarse ------------------\nFin de ejecucion")
            return True
        
def buscar_cliente_loguearse(nombre, apellido,password):

    cursor = database.cursor(buffered= True)
    cursor.execute("SELECT *FROM clientes  ")
    result = cursor.fetchall()
    for cliente in result :
        
        if cliente[1] == nombre and cliente[2] == apellido and cliente[3] == password :
            print ("-------------------- Se enocontro el dato  en la base ------------------\n")
            print(f"\n\tBienvenido cliente {cliente[1]} {cliente[2]}\n")
            return True
