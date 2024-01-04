import sys
sys.path.append("D:\\Curso POO Python\\Distribuidora\\modelo")

import datetime
from SistemaDistribuidora import SistemaDistribuidora

#Test:
sistema_distribuidora = SistemaDistribuidora()

#Test 1:
print("Test 1:")
sistema_distribuidora.agregar_cliente_residencial(4483979, "Pérez", "Juan", 11111111, 500)
sistema_distribuidora.agregar_cliente_residencial(4971920, "Rodríguez", "Marcela", 22222222, 0)
sistema_distribuidora.agregar_cliente_corporativo(7324211, 33333333333, "UTT")
sistema_distribuidora.agregar_cliente_corporativo(7329827, 44444444444, "Cooperativa El Grito Sagrado")
print("Clientes:")
for cliente in sistema_distribuidora.clientes:
    print(cliente)
    
#Test 2:
print("Test 2:")
sistema_distribuidora.agregar_tarifa(0, 50, 300.0, 2.0)
sistema_distribuidora.agregar_tarifa(51, 100, 350.0, 2.1)
sistema_distribuidora.agregar_tarifa(101, 200, 450.0, 2.5)
sistema_distribuidora.agregar_tarifa(201, 400, 500.0, 3.0)
sistema_distribuidora.agregar_tarifa(401, 2000, 1000.0, 4.0)
print("Tarifas:")
for tarifa in sistema_distribuidora.tarifas:
    print(tarifa)
    
#Test 3:
print("Test 3:")
sistema_distribuidora.agregar_lectura(datetime.date(2021, 12, 25), sistema_distribuidora.traer_cliente(4483979), 180)
sistema_distribuidora.agregar_lectura(datetime.date(2022, 1, 25), sistema_distribuidora.traer_cliente(4483979), 255)
sistema_distribuidora.agregar_lectura(datetime.date(2021, 12, 25), sistema_distribuidora.traer_cliente(4971920), 100)
sistema_distribuidora.agregar_lectura(datetime.date(2022, 1, 25), sistema_distribuidora.traer_cliente(4971920), 165)
sistema_distribuidora.agregar_lectura(datetime.date(2021, 12, 25), sistema_distribuidora.traer_cliente(7324211), 3526)
sistema_distribuidora.agregar_lectura(datetime.date(2022, 1, 25), sistema_distribuidora.traer_cliente(7324211), 4385)
sistema_distribuidora.agregar_lectura(datetime.date(2021, 12, 25), sistema_distribuidora.traer_cliente(7329827), 10862)
sistema_distribuidora.agregar_lectura(datetime.date(2022, 1, 25), sistema_distribuidora.traer_cliente(7329827), 11981)
print("Lecturas:")
for lectura in sistema_distribuidora.lecturas:
    print(lectura)
    
#Test 4:
print("Test 4:")
print("Lectura de 1/2022 del cliente #4483979:")
lectura1 = sistema_distribuidora.traer_lectura(1, 2022, sistema_distribuidora.traer_cliente(4483979))
print(lectura1)

#Test 5:
print("Test 5:")
print("Lectura de 12/2021 del cliente #4483979:")
lectura2 = sistema_distribuidora.traer_lectura(12, 2021, sistema_distribuidora.traer_cliente(4483979))
print(lectura2)

#Test 6:
print("Test 6:")
consumo = lectura1.calcular_consumo(lectura2)
print(f"Consumo del cliente #4483979 entre la lectura de 12/2021 y 1/2022: {consumo}kWh\n")

#Test 7:
print("Test 7:")
print(f"Tarifa según un consumo de {consumo}kWh:")
print(sistema_distribuidora.traer_tarifa(consumo))

#Test 8:
print("Test 8:")
print(f"Total a cobrar cliente #4483979 en el período 1/2022: ${sistema_distribuidora.calcular_total_a_cobrar(1, 2022, sistema_distribuidora.traer_cliente(4483979))}")

