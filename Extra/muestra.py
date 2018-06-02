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

def peor_caso(clase):
	ci = clase.mat_cov
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	# x1^2, x2^2, x1x2 
	fd = str(-c11/2) + " x1^2\n " + str(-(c12)) + " x1x2 \n"
	fd = fd + str(-c22/2) + " x2^2 \n"
	fd = fd + x1x2(clase)
	fd = fd + str(parte_3(clase) + parte_log(clase))
	return fd
	
def x1x2(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	fd = str((m.x*c11) + (m.y*c12)) + " x1\n"
	fd = fd + str((m.x*c12) + (m.y*c22)) + " x2\n"
	return fd
	
def parte_3(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	suma = (-(m.x*m.x*c11)/2)-(m.x*m.y*c12)
	suma = suma + (-(m.y*m.y*c22))
	return suma
	
def parte_log(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	arg = c11 * c22 - 2*c12
	log = (-1/2) * math.log(math.e, arg)
	return log

#EjercicioTarea
puntos = [P(6,9), P(8,10), P(9,11), P(8.5,12), P(7,13.5), P(8,16)]
puntos2 = [P(0.5,10.5), P(1,12.5), P(3,10.5), P(3,12.5), P(3,14.5), 
	P(3,18), P(5,18), P(5,16), P(5,14.5), P(5,13), ]
#EjercicioClase
puntosc = [P(1,2), P(2,2), P(3,1), P(2,3), P(3,2)]
puntosc2 = [P(8,10), P(9,8), P(9,9), P(8,9), P(7,9)]
w = W(puntosc2)
w2 = W(puntosc)
print (w.mat_cov)
print(w2.mat_cov)
if w.mat_cov == w2.mat_cov:
	print (x1x2(w))
	print (x1x2(w2))
#Hacer caso 2, completar
#Hacer el tercer caso
#print (peor_caso(w))








