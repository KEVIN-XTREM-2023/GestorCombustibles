
import Cliente

class Administrador(Cliente.Cliente):
    def __init__ (self):
        super().__init__()
        self.diccionario_administrador = {}
    
    def administradores(self, nombre, apellido, contra):
        self.diccionario_administrador = {
            'Admi1':'Kevin',
            'Apellido1':'Saquinga',
            'Contraseña':'123',
            'Admi2':'Bryan',
            'Apelldo2':'Oviedo',
            'Contraseña2':'123',

        }

        if  (self.diccionario_administrador['Admi1'] == nombre and self.diccionario_administrador['Apellido1'] == apellido and self.diccionario_administrador['Contraseña'] == contra or
        self.diccionario_administrador['Admi2'] == nombre and self.diccionario_administrador['Apelldo2'] == apellido and self.diccionario_administrador['Contraseña2'] == contra):

            print(self.diccionario_administrador['Admi1'])
            print("Dato encontrado")
            return True
        else:
            print("------- Dato No Encontrado ----------")
            return False



    

ad = Administrador()
#ad.administradores()