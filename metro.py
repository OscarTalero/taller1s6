""" Funciones para el manejo de las lineas       de metro con matrices
    Oscar Talero
    Junio 8-2021 """

def leer_numero_estaciones():
  #TODO Comentar código
  #TODO Implementar la función
  estacion = int(input('Ingrese el numero de estaciones: '))
  return estacion


def leer_conexiones(numero_estaciones):
  #TODO Comentar código
  #TODO Implementar la función
  for i in range (len(numero_estaciones)):
    for j in range (len(numero_estaciones[i])):
      if i == j:
        continue
      elif numero_estaciones[i][j] == 1:
        print('La estacion ',i,' tiene conexion con ' ,j)
  print()


def obtener_lista_conexiones_estacion(matriz_conexiones,numero_estacion):
  #TODO Comentar código
  #TODO Implementar la función
  cont = 0
  for i in range (len(matriz_conexiones[numero_estacion])):
    if i == numero_estacion:
        continue
    elif matriz_conexiones[numero_estacion][i] == 1:
      cont += 1
  print('La estacion ',numero_estacion,' tiene ',cont,' conexiones','\n')


def obtener_wstacion_mas_conectada(matriz_conexiones):
  #TODO Comentar código
  #TODO Implementar la función
  cont = 0
  contmax = 0
  for i in range (len(matriz_conexiones)):
    for j in range (len(matriz_conexiones[i])):
      if i == j:
        continue
      elif matriz_conexiones[i][j] == 1:
        cont += 1
    if contmax < cont:
      contmax = cont
      mayor = i
    cont = 0
  print('La estacion con mas conexiones es: ',mayor)