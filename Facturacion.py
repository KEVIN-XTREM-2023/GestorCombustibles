#from Pagos import pg
from Validar_venta import validador_venta

class Facturacion :

    def __init__(self):
        self.precio_super = 2.28
        self.descuento_super = 0.1 
        self.precio_extra = 1.75
        self.descuento_extra = 0.05
        self.precio_diesel = 1.18
        self.descuento_diesel = 0.05

    def formato_super(self, nombre, apellido ,cantidad, total):
        
        print("\n               ----------------- FACTURA SUPER ---------------")
        
        print(f"{nombre} {apellido} ha comprado {cantidad} litros ")
        print(f"El monto total de pagar de SUPER es {round(total,4)} $") 
    
    def formato_extra(self, nombre, apellido ,cantidad, total):
        
        print("\n               ----------------- FACTURA EXTRA ---------------")
        
        print(f"{nombre} {apellido} ha comprado {cantidad} litros de Extra")
        print(f"El monto total de pagar de EXTRA es {round(total,4)} $") 

    def formato_diesel(self,nombre, apellido ,cantidad, total):
        
        print("\n               ----------------- FACTURA DIESEL ---------------")
       
        print(f"{nombre} {apellido} ha comprado {cantidad} litros de Diesel")
        print(f"El monto total de pagar de DIESEL es {round(total,4)} $") 

   
    

factu = Facturacion()
#factu.factura("x","x")