from Cliente import Cliente

#Clase Lectura:
class Lectura:
    #Constructor:
    def __init__(self, id, fecha, cliente, estado_medidor):
        self.__id = id
        self.__fecha = fecha
        self.__cliente = cliente
        self.__estado_medidor = estado_medidor
    
    #Getters:
    @property
    def id(self):
        return self.__id
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def estado_medidor(self):
        return self.__estado_medidor
    
    #Setters:
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
        
    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha
        
    @cliente.setter
    def cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente
    
    @estado_medidor.setter
    def estado_medidor(self, nuevo_estado_medidor):
        self.__estado_medidor = nuevo_estado_medidor
        
    #__str__:
    def __str__(self):
        lectura = "Lectura:\n"
        lectura += f"ID: #{self.__id}\n"
        lectura += f"Fecha: {self.__fecha}\n"
        lectura += self.__cliente.__str__()
        lectura += f"Estado del medidor: {self.__estado_medidor}kWh\n"
        return lectura
    
    #Métodos:
    #CU 7:
    def calcular_consumo(self, lectura_anterior):
        return self.estado_medidor - lectura_anterior.estado_medidor