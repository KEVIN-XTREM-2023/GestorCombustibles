class Validar_compra:

    def validar_compra(self):
        compra = input("Esta seguro que quiere validar la compra ( s - n ):")

        if compra == 's':
            return True
        else :
            return False


validador_compra = Validar_compra()