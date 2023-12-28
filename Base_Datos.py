import mysql.connector

#Conexion

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "sistema_gestor_combustibles"
)


#print(database)
# CREAR TABLA DE DATOS

cursor = database.cursor(buffered= True)
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_gestor_combustibles")


#cursor.execute("SHOW DATABASEs")
"""

# Cear Tablas
#nombre = kevinsaq;
#cursor.execute("INSERT INTO clientes VALUES(null,'Kevin','Saquinga','123')")


clien = [
    ('xxxx','xxxx','xxxx'),
]
"""
cursor.executemany("INSERT INTO clientes VALUES(null,%s,%s,%s)", clien)
database.commit()
"""

#--------------------------------------------------------------------------------------------------------------------------------

# buscar
print("------------------------- DESDE AQUI EMPIEZA EL BUSCAR -----------------")
nombre = "Kevin"
apellido = "Saquinga"
print("---Todos mi clientes---")
cursor.execute("SELECT *FROM clientes  ")
result = cursor.fetchall()
for cliente in result :
    print(cliente[0],cliente[1],cliente[2],cliente[3] )
    if cliente[1] == nombre and cliente[2] == apellido:
        print ("-------------------- Se enocontro el dato ------------------")
        
    else :
        #print("---------------------No existe en la base de datos ------------")
        pass
        



print("------------------------- AQUI TERMINA -----------------")

#--------------------------------------------------------------------------------------------------------------------------------

cursor.execute("SELECT *FROM clientes  ")
cli = cursor.fetchone()
print(cli)

#Borrar
"""
cursor.execute("DELETE FROM clientes WHERE Apellidos = 'Teran' ")
database.commit()
"""

#Acgtualizar 
cursor.execute("UPDATE  clientes SET Nombres = 'Rene' WHERE Nombres = 'Bryan' ")
database.commit()
