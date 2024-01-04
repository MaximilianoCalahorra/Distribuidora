from Cliente import Cliente

#Clase ClienteCorporativo:
class ClienteCorporativo(Cliente):
    #Constructor:
    def __init__(self, id, numero_cliente, cuit, razon_social):
        super().__init__(id, numero_cliente)
        self.__cuit = cuit
        self.__razon_social = razon_social
        
    #Getters:
    @property
    def cuit(self):
        return self.__cuit
    
    @property
    def razon_social(self):
        return self.__razon_social
    
    #Setters:
    @cuit.setter
    def cuit(self, nuevo_cuit):
        self.__cuit = nuevo_cuit
        
    @razon_social.setter
    def razon_social(self, nueva_razon_social):
        self.__razon_social = nueva_razon_social
    
    #__str__:
    def __str__(self):
        cliente_corporativo = "Cliente corporativo:\n"
        cliente_corporativo += super().__str__()
        cliente_corporativo += f"CUIT: #{self.__cuit}\n"
        cliente_corporativo += f"Razón social: {self.__razon_social}\n"
        return cliente_corporativo