from Validar_Compra import validador_compra\

class Compra_combustible:
    
    def __init__(self):
        self.precio_super = 2.28
        self.precio_extra = 1.75
        self.precio_diesel = 1.18
        self.cantidad_super = 0
        self.cantidad_extra = 0
        self.cantidad_diesel = 0  
        self.tot_super = 0
        self.tot_extra = 0
        self.tot_diesel = 0

    def set_canti_super(self):

        self.cantidad_super = input("Ingrese Cantidad Super :")

    def set_canti_extra(self):
        self.cantidad_extra =input("Ingrese Cantidad Extra :")

    def set_canti_diesel(self):
        self.cantidad_diesel = input("Ingrese Cantidad Diesel :")

    def get_cant_super(self):
        return self.cantidad_super

    def get_cant_extra(self):
        return self.cantidad_extra

    def get_cant_diesel(self):
        return self.cantidad_diesel


    def menu_venta(self):
        print("1. Super ")
        print("2. Extra ")
        print("3. Diesel")

    def set_precio_super(self,valor):
        self.tot_super = valor

    def get_precio_super(self):
        return self.tot_super 

    
    def set_precio_extra(self,valor):
        self.tot_extra = valor

    def get_precio_extra(self):
        return self.tot_extra 

    
    def set_precio_diesel(self,valor):
        self.tot_diesel = valor

    def get_precio_diesel(self):
        return self.tot_diesel

    

    def compra_gasolina(self, nombre, apellido):
        print(f"\nBienvenido Admin {nombre} {apellido} \n")
        self.menu_venta()
        op = int(input("Ingrese Tipo de Gasolina :"))


        if op ==1 :
            print("----------- Super -----------")
            
            self.set_canti_super()
            if validador_compra.validar_compra() :
                
                total_super = float(self.get_cant_super()) * self.precio_super
                
                self.set_precio_super(total_super)
                
                print(f"\nEl Admin {nombre} {apellido} compro {self.get_cant_super()} litros")
                print(f"El precio ha pagar es {round(total_super,3)} $\n")

            else :
                print("\n\tValidacion Cancelada  y Compra Cancelada\n")
            

        elif op ==2:
            print("----------- Extra -----------")
            self.set_canti_extra()
            if validador_compra.validar_compra() :
                total_extra = float(self.get_cant_extra()) * self.precio_extra
                self.set_precio_extra(total_extra)
                print(f"\nEl Admin {nombre} {apellido} compro {self.get_cant_extra()} litros")
                print(f"El precio ha pagar es { total_extra} $\n")
            else:
                print("Validacion Cancelada y Compra Cancelada")
        elif op ==3:
            print("----------- Diesel -----------")
            self.set_canti_diesel()
            if validador_compra.validar_compra() :
                
                total_diesel = float(self.get_cant_diesel())  * self.precio_diesel
                self.set_precio_diesel(total_diesel)
                print(f"\nEl Admin {nombre} {apellido} compro {self.get_cant_diesel()} litros")
                print(f"El precio ha pagar es { total_diesel} $\n")

            else :
                print("Validacion Cancelada y Compra Cancelada")


compra = Compra_combustible()
#compra.compra_gasolina("xxxxx","xxxxxx")