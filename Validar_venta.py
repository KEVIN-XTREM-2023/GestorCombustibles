class Validar_venta:
    
    def validar_venta(self):
        venta = input("Esta seguro que los datos han sido correctos ( s - n ):")

        if venta == 's':
            #print("\n\t---------- Los datos han sidos enviados a la factura ---------")
            return True
        else :
            print("\n\t----------- Venta cancelada ----------")
            return False


validador_venta = Validar_venta()