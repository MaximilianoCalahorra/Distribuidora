from abc import ABC, abstractclassmethod

#Clase Cliente:
class Cliente(ABC):
    #Constructor:
    def __init__(self, id, numero_cliente):
        self._id = id
        self._numero_cliente = numero_cliente
    
    #Getters:
    @property
    def id(self):
        return self._id
    
    @property
    def numero_cliente(self):
        return self._numero_cliente
    
    #Setters:
    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id
        
    @numero_cliente.setter
    def numero_cliente(self, nuevo_numero_cliente):
        self._numero_cliente = nuevo_numero_cliente
        
    #__str__:
    def __str__(self):
        cliente = f"ID: #{self._id}\n"
        cliente += f"Número de cliente: #{self._numero_cliente}\n"
        return cliente 