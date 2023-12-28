from Pagos import pg
import datetime
from Compra_combustible import compra

class Reporte :


    #Venta de combustible
    def reportes_ventas_super(self,nombre,apellido):
        
        control = True
        
        diccionario_clientes_super = {}
        diccionario_ventas_super = {}
        diccionario_ventas_super["Cantidad"] = pg.get_cantidad_super()
        diccionario_ventas_super["Precio"] = round(pg.get_precio_super(),4)
        diccionario_clientes_super["Cliente" + ' ' +  nombre + ' ' + apellido] = diccionario_ventas_super

        for llave in diccionario_clientes_super:
            print(llave)
            print(diccionario_clientes_super[llave])

    def reportes_ventas_extra(self,nombre,apellido):
       
        diccionario_clientes_extra = {}
        diccionario_ventas_extra = {}
        diccionario_ventas_extra["Cantidad"] = pg.get_cantidad_extra()
        diccionario_ventas_extra["Precio"] = round(pg.get_precio_extra(),4)
        diccionario_clientes_extra["Cliente" + ' ' +  nombre + ' ' + apellido] = diccionario_ventas_extra

        for llave in diccionario_clientes_extra:
            print(llave)
            print(diccionario_clientes_extra[llave])


    def reportes_ventas_diesel(self,nombre,apellido):
       
        diccionario_clientes_diesel = {}
        diccionario_ventas_diesel = {}
        diccionario_ventas_diesel["Cantidad"] = pg.get_cantidad_diesel()
        diccionario_ventas_diesel["Precio"] = round(pg.get_precio_diesel(),4)
        diccionario_clientes_diesel["Cliente" + ' ' +  nombre + ' ' + apellido] = diccionario_ventas_diesel

        for llave in diccionario_clientes_diesel:
            print(llave)
            print(diccionario_clientes_diesel[llave])


    #-----------------------------------------




    def reporte_compras_super(self,nombre,apellido):
        diccionario_admin_super = {}
        diccionario_compra_super = {}
        diccionario_compra_super["Cantidad"] = compra.get_cant_super()
        diccionario_compra_super["Precio"] = round(compra.get_precio_super(),4)
        diccionario_admin_super["Administrador" + ' ' +  nombre + ' ' + apellido] = diccionario_compra_super

        for llave in diccionario_admin_super:
            print(llave)
            print(diccionario_admin_super[llave])



    def reporte_compras_extra(self,nombre,apellido):
        diccionario_admin_extra = {}
        diccionario_compra_extra = {}
        diccionario_compra_extra["Cantidad"] = compra.get_cant_extra()
        diccionario_compra_extra["Precio"] = round(compra.get_precio_extra(),4)
        diccionario_admin_extra["Administrador" + ' ' +  nombre + ' ' + apellido] = diccionario_compra_extra

        for llave in diccionario_admin_extra:
            print(llave)
            print(diccionario_admin_extra[llave])

    def reporte_compras_diesel(self,nombre,apellido):
        diccionario_admin_diesel = {}
        diccionario_compra_diesel = {}
        diccionario_compra_diesel["Cantidad"] = compra.get_cant_diesel()
        diccionario_compra_diesel["Precio"] = round(compra.get_precio_diesel(),4)
        diccionario_admin_diesel["Administrador" + ' ' +  nombre + ' ' + apellido] = diccionario_compra_diesel

        for llave in diccionario_admin_diesel:
            print(llave)
            print(diccionario_admin_diesel[llave])





repor = Reporte()
#repor.reportes_dias_ventas()




