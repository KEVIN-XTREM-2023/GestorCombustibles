class Cliente:
    def __init__(self):
        self.nombre = " "
        self.apellido = " "
        self.password = " "

    def crear_cliente(self):
        
        self.nombre = input("Ingrese su nombre: ")
        #self.setNombre()
        self.apellido = input("Ingrese su apellido: ")
        self.password = input("Ingrese su contraseña: ")
        #print(f"Nombre {self.nombre} {self.apellido}")
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre


cl  = Cliente()

