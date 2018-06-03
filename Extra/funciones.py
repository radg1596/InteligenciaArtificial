from muestra import *
"""
Es la f'ormula m'as larga para calcular la funci''on discriminante
Recibe como parametro una clase
Retorna si funci'on discriminante como cadena.
"""
def peor_caso(clase):
	ci = clase.mat_covi
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	# x1^2, x2^2, x1x2 
	fd = str(round(-c11/2, 4)) + " x1^2\n " 
	fd = fd + str(round(-(c12), 4)) + " x1 x2 \n"
	fd = fd + str(round(-c22/2, 4))  + " x2^2 \n"
	fd = fd + x1_x2(clase)
	fd = fd + str(round( real(clase) + log(clase),4 ))
	return fd
"""
Esta funcion recibe una clase y solo calcula los coeficientes 
correspondientes a x1 y x2 de la funcion discriminante.
"""	
def x1_x2(clase):
	ci = clase.mat_covi
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	fd = str(round((m.x*c11) + (m.y*c12),4)) + " x1\n"
	fd = fd + str(round((m.x*c12) + (m.y*c22),4)) + " x2\n"
	return fd
"""
Esta funcion recibe una clase y solo calcula los coeficientes 
correspondientes a la parte real (sin log) de la funcion discriminante.
"""	
def real(clase):
	ci = clase.mat_covi
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	suma = (-(m.x*m.x*c11)/2)-(m.x*m.y*c12)
	#agrege un /2
	suma = suma + (-(m.y*m.y*c22)/2)
	return suma
"""
Esta funcion recibe una clase y solo calcula los coeficientes 
correspondientes a log de la funcion discriminante.
"""
#Parte de logaritmo	
def log(clase):
	ci = clase.mat_covi
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	arg = c11 * c22 - 2*c12
	log = (-1/2) * math.log(math.e, arg)
	return log
"""
Esta funcion recibe una clase y solo calcula los coeficientes 
correspondientes del caso euclideano de la funcion discriminante.
"""
#El caso que es igual al euclideano
def caso_sencillo(clase):
	ci = clase.mat_covi
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	fd = str(round(m.x,4)) + " x1\n" + str(round(m.y,4))+ " x2\n"
	fd = fd + str(round((-1/2) * (m.x*m.x + m.y*m.y),4))
	return fd
"""
Recibe una lista de muestras
Retorna:
	True: Si las matrices de covarianzas son todas iguales
	False: En caso contrario
"""
def cov_igual(l_muestras):
	res = True
	pivote = l_muestras[0].mat_cov
	for muestra in l_muestras:
		if pivote == muestra.mat_cov:
			pass
		else:
			res = False
			break
	return res
"""
Recibe una clase
Comprueba si su matriz de covarianzas es diagonal. Retorna True o False.
"""	
def mat_diagonal(clase):
	mc = clase.mat_cov
	m11 = mc[0][0]; m22 = mc[1][1]
	m12 = mc[0][1]
	#Matriz diagonal, con diagonal principal cercana a cero
	if m11<=1 and m11 >=-1 and  m22<=1 and m22 >=-1 and m12==0:
		return True
	return False