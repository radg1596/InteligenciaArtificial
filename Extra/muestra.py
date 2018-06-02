import math
from punto import *
from mat import *
"""
Clase muestra
Atributos:
	-l_puntos: Es una lista que contiene todos los puntos de la muestra
	-media: Es el centroide de su lista de puntos
"""
class W():
	def __init__(self, l_puntos):
		self.l_puntos = l_puntos
		self.media = self.cal_media()
		self.mat_cov = cov(self)
		
	def cal_media(self):
		x=0.0;y=0.0
		for punto in self.l_puntos:
			total = len (self.l_puntos)
			x = x + punto.x
			y = y + punto.y
		return P(x/total, y/total)