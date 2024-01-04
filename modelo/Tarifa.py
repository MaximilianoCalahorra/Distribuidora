#Clase Tarifa:
class Tarifa:
    #Constructor:
    def __init__(self, id, consumo_desde, consumo_hasta, cargo_fijo, cargo_variable):
        self.__id = id
        self.__consumo_desde = consumo_desde
        self.__consumo_hasta = consumo_hasta
        self.__cargo_fijo = cargo_fijo
        self.__cargo_variable = cargo_variable
        
    #Getters:
    @property
    def id(self):
        return self.__id
    
    @property
    def consumo_desde(self):
        return self.__consumo_desde
    
    @property
    def consumo_hasta(self):
        return self.__consumo_hasta
    
    @property
    def cargo_fijo(self):
        return self.__cargo_fijo
    
    @property
    def cargo_variable(self):
        return self.__cargo_variable
    
    #Setters:
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
        
    @consumo_desde.setter
    def consumo_desde(self, nuevo_consumo_desde):
        self.__consumo_desde = nuevo_consumo_desde
        
    @consumo_hasta.setter
    def consumo_hasta(self, nuevo_consumo_hasta):
        self.__consumo_hasta = nuevo_consumo_hasta
    
    @cargo_fijo.setter
    def cargo_fijo(self, nuevo_cargo_fijo):
        self.__cargo_fijo = nuevo_cargo_fijo
        
    @cargo_variable.setter
    def cargo_variable(self, nuevo_cargo_variable):
        self.__cargo_variable = nuevo_cargo_variable
    
    #__str__:
    def __str__(self):
        titulo = "Tarifa:\n"
        id = f"ID: #{self.__id}\n"
        consumo_desde = f"Consumo desde: {self.__consumo_desde}kWh\n"
        consumo_hasta = f"Consumo hasta: {self.__consumo_hasta}kWh\n"
        cargo_fijo = f"Cargo fijo: ${self.__cargo_fijo}\n"
        cargo_variable = f"Cargo variable: {self.__cargo_variable}\n"
        return titulo + id + consumo_desde + consumo_hasta + cargo_fijo + cargo_variable