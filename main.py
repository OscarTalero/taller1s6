""" Programa lineas de metro
    Programa para el manejo de conexiones entre estaciones de metro
    Oscar Talero
    Junio 8-2021 """

import metro as mt
from random import randint
import numpy as np

#solicita el numero de estaciones 
estaciones = mt.leer_numero_estaciones()
#crea la matriz de acuerdo con el numero de estaciones
metro = np.random.randint(0,2,(estaciones,estaciones))
print(metro,'\n')
mt.leer_conexiones(metro)
estacion = int(input('Ingrese el numero de la estacion a consultar: '))
mt.obtener_lista_conexiones_estacion(metro,estacion)
mt.obtener_wstacion_mas_conectada(metro)