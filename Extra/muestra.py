import math
from punto import *
"""
Clase muestra
Atributos:
	-l_puntos: Es una lista que contiene todos los puntos de la muestra
	-media: Es el centroide de su lista de puntos
	-mat_cov: Es la matriz de covarianzas
	-mat_covi: Es la matriz de covarianzas inversa
"""
class W():
	"""
	Incializar
	Recibe una lista de puntos, los almacena, calcula su media
		asi como su matriz de covarianzas de la muestra.
	"""
	def __init__(self, l_puntos):
		self.l_puntos = l_puntos
		self.media = self.cal_media()
		self.mat_cov = self.cov()
		self.mat_covi = self.inversa()
	"""
	Calcula la media del conjunto de punto de la 
	instancia
	"""	
	def cal_media(self):
		x=0.0;y=0.0
		total = len (self.l_puntos)
		for punto in self.l_puntos:
			x = x + punto.x
			y = y + punto.y
		return P(x/total, y/total)
	"""
	Calcula la matriz de covarianzas de la instancia
	Retorna una lista con dos listas [ [3,2], [2,3] ] 
	"""	
	def cov(self):
		puntos = self.l_puntos
		media = self.media
		total = len(self.l_puntos)
		c11 = 0; c22 = 0; c12 = 0
		for punto in puntos:
			c11 = c11 + (punto.x - media.x) * (punto.x - media.x)
			c22 = c22 + (punto.y - media.y) * (punto.y - media.y)
			c12 = c12 + (punto.x - media.x) * (punto.y - media.y)
		c11=round(c11/total,4); c22 = round(c22/total,4)
		c12 = round(c12/total, 4)
		c = [[c11, c12],[c12, c22]]
		return c
	"""
	Recibe la matriz de covarianzas y retorna su inversa
	como una lista de dos listas [[1,2][3,4]]
	"""	
	def inversa(self):
		c11 = self.mat_cov[0][0]; c22 = self.mat_cov[1][1]
		c12 = self.mat_cov[0][1]
		det =  (c11*c22) - (c12 * c12)
		ci = [[round(c22/det,4), round((c12*-1)/det,4)], 
			[round((c12*-1)/det,4), round(c11/det,4)]]	
		return ci