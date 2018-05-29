from punto import *
import math
import random
"""
Distancia
Recibe dos puntos
Calcula la distancia entre ellos
Retorna un flotante, que es la distancia
"""
def dist(punto1, punto2):
	a = punto2.x - punto1.x
	b = punto2.y - punto1.y
	distancia = math.sqrt(a**2 + b**2)
	return distancia
"""
Recibe una lista de clases (una clase es un objeto) y un indice i
Para cada clase, toma su atributo distancias (es una lista)
	y selecciona el elemento i. Es decir se arma un arreglo de las distancias
	que tiene cada clase a un punto en particular.
Retorna la lista resultante
"""	
def dist_clases(clases, i):
	distancias = []
	for clase in clases:
		distancias.append(clase.distancias[i])
	return distancias
"""
Recibe dos listas de puntos (cada punto es una media)
Se encarga de comparar estas listas
Si son iguales, retorna False, en caso contrario True (No hubo cambios en las medias)
"""	
def comprobar_cambio_medias(median, media):
	for i in range(0, len(median)):
		if median[i] != media[i]:
			return True
	return False