class Validar_datos:
    


    def validor(self,nombre, apellido, contra):
        try:
            if len(nombre) > 30  or len(apellido) > 30 or len(contra) > 20 :
                print("----------  Datos No Validos ------------")
                return False
            else:
                print("----------  Datos Validos ------------")
                return True

        except TypeError:
            print("--------- Error formato de datos incorrectos ------------")

        

validar = Validar_datos()
#validar.validor(1234,"xxx",456565)


