from Cliente import cl
from Administrador import ad
from Base_datos_gestion_combustible import ingresar_datos , visualizar_datos, buscar_cliente , buscar_cliente_loguearse
from Validar_datos import validar
from Venta_combustible import vent
from Despacho import despa
from Compra_combustible import compra
from Reporte import repor

def menu_prinipal():

    print("\n                            ----------------Sistema de Gestión de Combustible-------------")
    print("1. Administrador\n"+
        "2. Cliente\n"
        + "3. Salir\n"
        
    )

def controlador(opcion):

    while (opcion > 3 or opcion < 1):
        print("Solo opciones: 1 al 3")
        break

def menu_administrador():
    print("------------ Menu Administrador ------------- ")
    print("1. Compra Combustible\n"
        + "2. Ver Despacho de Combustible\n"
        + "3. Reporte de ventas\n"
        + "4. Reporte de Combustible\n"
        + "5. Salir\n" )

def menu_cliente():
    print("\n---------------- Menu Cliente --------------")
    print("1. Ingresar\n"+
    "2. Registrarse\n"
    )



class Gestor_Combustible :

    def __init__(self):
        self.nombre_cliente = ""
        self.apellido_cliente = ""

    def set_nombre_cliente(self,nombre):
        self.nombre_cliente = nombre

    def get_nombre_cliente(self):
        return self.nombre_cliente

    def set_apellido_cliente(self,apellido):
        self.apellido_cliente = apellido

    def get_apellido_cliente(self):
        return self.apellido_cliente

    def gestor_combustible(self):
        while True:
            
            try :
            
                
                menu_prinipal()
                opcion = int(input("Ingresar Opcion: "))
                controlador(opcion)


                if(opcion == 1):
                    print("\n--------- Iniciar Sesion -------")

                    ad.crear_cliente()
                    if (ad.administradores(ad.nombre,ad.apellido,ad.password) == True):
                        

                        while True :
                            menu_administrador()
                            opcion = int(input("Ingresar Opcion: "))
                            if opcion == 1 :
                                print("\t ------------- COMPRA COMBUSTIBLE ------------")
                                compra.compra_gasolina(ad.nombre,ad.apellido)



                            elif opcion == 2 :
                                print("\t ------------- DESPACHO DE COMBUSTIBLE ------------\n")
                                despa.despacho_super()
                                print("\n")
                                despa.despacho_extra()
                                print("\n")
                                despa.despacho_diesel()
                                print("\n")

                            elif opcion == 3 :
                                print("\t ------------- REPORTE DE VENTAS ------------")
                                print("\n------------- REPORTE DE SUPER ------------")
                                repor.reportes_ventas_super(self.get_nombre_cliente(),self.get_apellido_cliente())
                                print("\n------------- REPORTE DE EXTRA ------------")
                                repor.reportes_ventas_extra(self.get_nombre_cliente(),self.get_apellido_cliente())
                                print("\n------------- REPORTE DE DIESEL ------------")
                                repor.reportes_ventas_diesel(self.get_nombre_cliente(),self.get_apellido_cliente())
                                


                            elif opcion == 4 :
                                print("\t ------------- REPORTE DE COMBUSTIBLE ------------")
                                print("\n------------- REPORTE DE SUPER ------------")
                                repor.reporte_compras_super(ad.nombre,ad.apellido)
                                print("\n------------- REPORTE DE EXTRA ------------")
                                repor.reporte_compras_extra(ad.nombre,ad.apellido)
                                print("\n------------- REPORTE DE DIESEL ------------")
                                repor.reporte_compras_diesel(ad.nombre,ad.apellido)
                                
                            elif opcion == 5 :
                                break
                            

                    else :
                        print("------ Gracias por utilizar nuestro sistema ----------")



                elif (opcion == 2):
                    menu_cliente()
                    opcion = int(input("Ingresar Opcion: "))
                    if opcion ==1 :
                        
                        
                        print("----------- Loguearse ---------")
                        cl.crear_cliente()
                        if buscar_cliente_loguearse(cl.nombre,cl.apellido,cl.password) == True:
                            vent.venta(cl.nombre,cl.apellido)
                            self.set_nombre_cliente(cl.nombre)
                            self.set_apellido_cliente(cl.apellido)
                            
                        else:
                            print("No existe este cliente en su base de Datos")
                            


                        

                    elif opcion == 2:
                        print("------------ Registrarse ---------")

                        cl.crear_cliente()
                        
                        if buscar_cliente(cl.nombre,cl.apellido) == True:


                            pass
                        else:
                                
                            if  validar.validor(cl.nombre,cl.apellido,cl.password) :
                                ingresar_datos(cl.nombre,cl.apellido,cl.password)
                                print("---- Registro Exitoso -----")
                                #visualizar_datos()
                            else:
                                print("Registro Fallido")

                elif opcion == 3:
                    print("--- Fin de ejecucion -----")
                    break
            except :
                print ("Acaba de Ingresar un dato no valido")

gestor = Gestor_Combustible()
gestor.gestor_combustible()



