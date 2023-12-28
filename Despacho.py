from Pagos import pg
from Compra_combustible import compra


class Despacho:
    def __init__(self):
        self.super = 100
        self.extra = 100
        self.diesel = 100
        self.cont_super = 0
        self.cont_extra = 0
        self.cont_diesel = 0

    def get_super(self):
        return self.super
    def get_extra(self):
        return self.extra
        
    def get_diesel(self):
        return self.diesel

    def cont_gasolina_super(self):
        self.cont_super += (float(compra.get_cant_super()) + self.get_super() )
        return self.cont_super

    def cont_gasolina_extra(self):
        self.cont_extra += (float(compra.get_cant_extra()) + self.get_extra())
        return self.cont_extra

    def cont_gasolina_diesel(self):
        self.cont_diesel += (float(compra.get_cant_diesel()) +  self.get_diesel())
        return self.cont_diesel

    def despacho_super(self):
         
        gasolina_super = self.get_super() + float(compra.get_cant_super())
        print(f"\t Despacho SUPER Inicial {gasolina_super} litros")
        despacho_nuevo_super = gasolina_super - pg.get_cantidad_super()
        print(f"\t Despacho Actualizado {despacho_nuevo_super} litros")
        pass
        

    def despacho_extra(self):
        gasolina_extra = self.get_extra() + float(compra.get_cant_extra())
        
        print(f"\t Despacho EXTRA Inicial {gasolina_extra} litros")
        despacho_nuevo_extra = gasolina_extra - pg.get_cantidad_extra()
        print(f"\t Despacho Actualizado {despacho_nuevo_extra} litros")
        
        

    def despacho_diesel(self):
        gasolina_diesel = self.get_diesel() + float(compra.get_cant_diesel())
        
        print(f"\t Despacho DIESEL Inicial {gasolina_diesel} litros")
        despacho_nuevo_diesel = gasolina_diesel - pg.get_cantidad_diesel()
        print(f"\t Despacho Actualizado {despacho_nuevo_diesel} litros")


despa = Despacho()