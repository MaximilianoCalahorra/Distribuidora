from Tarifa import Tarifa
from Lectura import Lectura
from ClienteResidencial import ClienteResidencial
from ClienteCorporativo import ClienteCorporativo
import datetime

#Clase SistemaDistribuidora:
class SistemaDistribuidora:
    #Constructor:
    def __init__(self):
        self.__lst_tarifa = []
        self.__lst_lectura = []
        self.__lst_cliente = []
    
    #Getters:
    @property
    def tarifas(self):
        return self.__lst_tarifa
    
    @property
    def lecturas(self):
        return self.__lst_lectura
    
    @property
    def clientes(self):
        return self.__lst_cliente
    
    #__str__:
    def __str__(self):
        sistema_distribuidora = "Lista de tarifas:\n"
        for tarifa in self.__lst_tarifa:
            sistema_distribuidora += tarifa.__str__()
        sistema_distribuidora += "Lista de lecturas:\n"
        for lectura in self.__lst_lectura:
            sistema_distribuidora += lectura.__str__()
        sistema_distribuidora += "Lista de clientes:\n"
        for cliente in self.__lst_cliente:
            sistema_distribuidora += cliente.__str__()
        return sistema_distribuidora
    
    #Métodos:
    #CU 1:
    def agregar_cliente_residencial(self, numero_cliente, nombre, apellido, dni, kWh_subsidio):
        id = 1
        if len(self.__lst_cliente) > 0:
            tamanio = len(self.__lst_cliente)
            id = self.__lst_cliente[tamanio - 1].id + 1
        return self.__lst_cliente.append(ClienteResidencial(id, numero_cliente, nombre, apellido, dni, kWh_subsidio))

    #CU 2:
    def agregar_cliente_corporativo(self, numero_cliente, cuit, razon_social):
        id = 1
        if len(self.__lst_cliente) > 0:
            tamanio = len(self.__lst_cliente)
            id = self.__lst_cliente[tamanio - 1].id + 1
        return self.__lst_cliente.append(ClienteCorporativo(id, numero_cliente, cuit, razon_social))    
    
    #CU 3:
    def agregar_tarifa(self, consumo_desde, consumo_hasta, cargo_fijo, cargo_variable):
        id = 1
        if len(self.__lst_tarifa) > 0:
            tamanio = len(self.__lst_tarifa)
            id = self.__lst_tarifa[tamanio - 1].id + 1
        return self.__lst_tarifa.append(Tarifa(id, consumo_desde, consumo_hasta, cargo_fijo, cargo_variable))
    
    #CU 4:
    def traer_cliente(self, numero_cliente):
        cliente_auxiliar = None
        cliente_buscado = None
        i = 0
        while i < len(self.__lst_cliente) and cliente_buscado == None:
            cliente_auxiliar = self.__lst_cliente[i]
            if cliente_auxiliar.numero_cliente == numero_cliente:
                cliente_buscado = cliente_auxiliar
            i += 1
        return cliente_buscado
    
    #CU 5:
    def agregar_lectura(self, fecha, cliente, estado_medidor):
        id = 1
        if len(self.__lst_lectura) > 0:
            tamanio = len(self.__lst_lectura)
            id = self.__lst_lectura[tamanio - 1].id + 1
        return self.__lst_lectura.append(Lectura(id, fecha, cliente, estado_medidor))
    
    #CU 6:
    def traer_lectura(self, mes, anio, cliente):
        lectura_auxiliar = None
        lectura_buscada = None
        i = 0
        while i < len(self.__lst_lectura) and lectura_buscada == None:
            lectura_auxiliar = self.__lst_lectura[i]
            if lectura_auxiliar.cliente.numero_cliente == cliente.numero_cliente and lectura_auxiliar.fecha.year == anio and lectura_auxiliar.fecha.month == mes:
                lectura_buscada = lectura_auxiliar
            i += 1
        return lectura_buscada
    
    #CU 8:
    def traer_tarifa(self, consumo):
        tarifa_auxiliar = None
        tarifa_buscada = None
        i = 0
        while i < len(self.__lst_tarifa) and tarifa_buscada == None:
            tarifa_auxiliar = self.__lst_tarifa[i]
            if tarifa_auxiliar.consumo_desde <= consumo and consumo <= tarifa_auxiliar.consumo_hasta:
                tarifa_buscada = tarifa_auxiliar
            i += 1
        return tarifa_buscada
    
    #CU 9:
    def calcular_total_a_cobrar(self, mes, anio, cliente):
        lectura_actual = self.traer_lectura(mes, anio, cliente)
        fecha_lectura_anterior = lectura_actual.fecha - datetime.timedelta(28)
        lectura_anterior = self.traer_lectura(fecha_lectura_anterior.month, fecha_lectura_anterior.year, cliente)
        consumo = lectura_actual.calcular_consumo(lectura_anterior)
        tarifa = self.traer_tarifa(consumo)
        total_variable = tarifa.cargo_variable * consumo
        if isinstance(lectura_actual.cliente, ClienteResidencial):
            descuento = tarifa.cargo_variable * lectura_actual.cliente.kWh_subsidio
            if total_variable >= descuento:
                total_variable -= descuento
            else:
                total_variable = 0
        return tarifa.cargo_fijo + total_variable