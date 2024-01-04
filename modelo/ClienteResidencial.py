from Cliente import Cliente

#Clase ClienteResidencial:
class ClienteResidencial(Cliente):
    #Constructor:
    def __init__(self, id, numero_cliente, nombre, apellido, dni, kWh_subsidio):
        super().__init__(id, numero_cliente)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__kWh_subsidio = kWh_subsidio
        
    #Getters:
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def dni(self):
        return self.__dni
    
    @property
    def kWh_subsidio(self):
        return self.__kWh_subsidio
    
    #Setters:
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
        
    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni
    
    @kWh_subsidio.setter
    def kWh_subsidio(self, nuevo_kWh_subsidio):
        self.__kWh_subsidio = nuevo_kWh_subsidio
        
    #__str__:
    def __str__(self):
        cliente_residencial = "Cliente residencial:\n"
        cliente_residencial += super().__str__()
        cliente_residencial += f"Nombre: {self.__nombre}\n"
        cliente_residencial += f"Apellido: {self.__apellido}\n"
        cliente_residencial += f"DNI: #{self.__dni}\n"
        cliente_residencial += f"Subsidio: {self.__kWh_subsidio}kWh\n"
        return cliente_residencial