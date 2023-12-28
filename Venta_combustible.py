from Pagos import pg
from Facturacion import factu
class Venta:


    def menu_ventas(self):
        print("-------------- Combustible ---------------")
        print("1. Super")
        print("2. Extra")
        print("3. Diesel")
    
    def venta(self,nombre, apellido):
        self.menu_ventas()
        op = int(input("Ingrese Opcion:"))
        print(" ")
        if op ==1 :
            print("----------- Super -----------")
            pg.pagos(nombre,apellido,"super")
        elif op ==2:
            print("----------- Extra -----------")
            pg.pagos(nombre,apellido,"extra")
        elif op ==3:
            print("----------- Diesel -----------")
            pg.pagos(nombre,apellido,"diesel")

vent = Venta()