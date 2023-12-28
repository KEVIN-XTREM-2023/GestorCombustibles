from Validar_venta import validador_venta
from Facturacion import factu
from random import randint, uniform,random

class Pagos:

    def __init__(self):
        self.precio_super = 2.28
        self.descuento_super = 0.1 
        self.precio_extra = 1.75
        self.descuento_extra = 0.05
        self.precio_diesel = 1.18
        self.descuento_diesel = 0.05
        self.tarjeta_fondo = randint(0,200)
        self.cantidad_super = 0
        self.cantidad_extra = 0
        self.cantidad_diesel = 0
        self.cont_super = 0
        self.cont_extra = 0
        self.cont_diesel = 0
        self.precio_sp = 0
        self.precio_ext = 0
        self.precio_ds = 0

    def menu_pago(self):
        print("---------- Forma de Pago ---------------\n1. Efectivo \n2. Tarjeta Credito")
        pago = int(input("Ingrese forma de pago: "))
        if pago ==1:
            return "efectivo"
        elif pago == 2:
            return "tarjeta"

    def verificar_fondos(self,fondos):
        
        if self.tarjeta_fondo >= fondos:
            print("Tiene Fondos")
            print(f"")
            return True
        else :
            print("No tiene fondos") 
            return False

    def set_cantidad_super(self,valor):
        self.cantidad_super = valor

    def get_cantidad_super(self):
        return self.cantidad_super 

    def set_cantidad_extra(self,valor):
        self.cantidad_extra = valor

    def get_cantidad_extra(self):
        return self.cantidad_extra

    def set_cantidad_diesel(self,valor):
        self.cantidad_diesel = valor

    def get_cantidad_diesel(self):
        return self.cantidad_diesel


    def set_super(self,valor):
        self.precio_sp = valor

    def get_precio_super(self):
        return self.precio_sp

    def set_extra(self,valor):
        self.precio_ext = valor

    def get_precio_extra(self):
        return self.precio_ext

    def set_diesel(self,valor):
        self.precio_ds = valor

    def get_precio_diesel(self):
        return self.precio_ds


    def pagos(self, nombre,apellido,tipo):
        opcion_menu = self.menu_pago()

        if opcion_menu == "efectivo" and tipo =="super" :
            cant_super = float(input("Ingrese la cantidad: "))
            self.cont_super += cant_super
            self.set_cantidad_super(self.cont_super)

            if validador_venta.validar_venta() :
                
                print("\nPago por efectivo")
                total_super = self.precio_super * cant_super
                self.set_super(total_super)
                factu.formato_super(nombre,apellido,cant_super,total_super)
            else :
                print("\t---------- Validacion Fallido --------\n")


        elif opcion_menu == "tarjeta" and tipo =="super" :
            fondo_super = randint(0,200)
            print(f"Su Valor de la Tarjeta de Credito es: {fondo_super}")
            cant_super = float(input("Ingrese la cantidad: "))
            self.cont_super += cant_super
            self.set_cantidad_super(self.cont_super)
            if validador_venta.validar_venta():
                
                print("\nPago por Tarjeta de  Credito\n")
                total_tempo_super = self.precio_super * cant_super
                descuento = total_tempo_super * self.descuento_super
                total_sp = total_tempo_super - descuento
                self.set_super(total_sp)        

                if fondo_super >= total_sp:
                    print("Existe Fondos")
                    print("\nLos datos han sidos enviados a la factura")
                    factu.formato_super(nombre,apellido,cant_super,total_sp)
                    print(f"Su nuevo monto de la Tarjeta de Credito es {round(fondo_super-total_sp,2)} $")
                else :
                    print("No Tiene Fondos no se puede efectuar la factura")
            else :
                print("\t---------- Validacion Fallido --------\n")

        elif opcion_menu == "efectivo" and tipo =="extra" :
            
            cant_extra = float(input("Ingrese la cantidad: "))
            self.cont_extra += cant_extra
            self.set_cantidad_extra(self.cont_extra)


            if validador_venta.validar_venta():
                
                print("\nPago por efectivo")
                total_extra = self.precio_extra * cant_extra
                self.set_extra(total_extra)
                factu.formato_extra(nombre,apellido,cant_extra,total_extra)
            else :
                print("\t---------- Validacion Fallido --------\n")
        
        elif opcion_menu == "tarjeta" and tipo =="extra" :
            fondo_extra = randint(0,200)
            print(f"Su Valor de la Tarjeta de Credito es: {fondo_extra}")
            cant_extra = float(input("Ingrese la cantidad: "))
            self.cont_extra += cant_extra
            self.set_cantidad_extra(self.cont_extra)
            if validador_venta.validar_venta() :
                
                print("\nPago por Tatjeta De Credito")
                total_tempo_extra = self.precio_extra * cant_extra
                descuento = total_tempo_extra * self.descuento_extra
                total_extr = total_tempo_extra - descuento
                self.set_extra(total_extr)   

                if fondo_extra >=total_extr :
                    print("Existe Fondos")
                    print("\nLos datos han sidos enviados a la factura")
                    factu.formato_extra(nombre,apellido,cant_extra,total_extr)
                    print(f"Su nuevo monto de la Tarjeta de Credito es {round(fondo_extra-total_extr,2)} $")
                else :
                    print("No Tiene Fondos no se puede efectuar la factura")   

            else :
                print("\t---------- Validacion Fallido --------\n")

        elif opcion_menu == "efectivo" and tipo =="diesel" :
            cant_diesel = float(input("Ingrese la cantidad: "))
            self.cont_diesel += cant_diesel 
            self.set_cantidad_diesel(self.cont_diesel)
            if validador_venta.validar_venta():
                
                print("\nPago por efectivo")
                total_diesel = self.precio_diesel * cant_diesel
                self.set_diesel(total_diesel) 

                factu.formato_diesel(nombre,apellido,cant_diesel,total_diesel)
            else :
                print("\t---------- Validacion Fallido --------\n")

        elif opcion_menu == "tarjeta" and tipo =="diesel" :
            fondos_diesel = randint(0,200)
            print(f"Su Valor de la Tarjeta de Credito es: {fondos_diesel}")
            cant_diesel = float(input("Ingrese la cantidad: "))
            self.cont_diesel += cant_diesel 
            self.set_cantidad_diesel(self.cont_diesel)

            if validador_venta.validar_venta():
                
                print("\nPago por Tatjeta De Credito")
                total_tempo_diesel = self.precio_diesel * cant_diesel
                descuento = total_tempo_diesel * self.descuento_diesel
                
                total_diesel = total_tempo_diesel - descuento
                self.set_diesel(total_diesel) 

                if fondos_diesel >= total_diesel:
                    print("Existe Fondos")
                    print("\nLos datos han sidos enviados a la factura")
                    factu.formato_diesel(nombre,apellido,cant_diesel,total_diesel)
                    print(f"Su nuevo monto de la Tarjeta de Credito es {round(fondos_diesel-total_diesel,2)} $")
                else:
                    
                    print("No Tiene Fondos no se puede efectuar la factura")    
            else :
                print("\t---------- Validacion Fallido --------\n")


pg = Pagos()