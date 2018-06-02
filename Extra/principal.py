from muestra import *

def peor_caso(clase):
	ci = clase.mat_cov
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	# x1^2, x2^2, x1x2 
	fd = str(round(-c11/2, 4)) + " x1^2\n " 
	fd = fd + str(round(-(c12), 4)) + " x1 x2 \n"
	fd = fd + str(round(-c22/2, 4))  + " x2^2 \n"
	fd = fd + x1_x2(clase)
	fd = fd + str(round( real(clase) + log(clase),4 ))
	return fd
	
def x1_x2(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	fd = str(round((m.x*c11) + (m.y*c12),4)) + " x1\n"
	fd = fd + str(round((m.x*c12) + (m.y*c22),4)) + " x2\n"
	return fd
	
def real(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	suma = (-(m.x*m.x*c11)/2)-(m.x*m.y*c12)
	#agrege un /2
	suma = suma + (-(m.y*m.y*c22)/2)
	return suma

#Parte de logaritmo	
def log(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	arg = c11 * c22 - 2*c12
	log = (-1/2) * math.log(math.e, arg)
	return log
	
#El caso que es igual al euclideano
def caso3(clase):
	ci = clase.mat_cov
	m = clase.media
	c11 = ci[0][0]; c22 = ci[1][1]
	c12 = ci[0][1]
	fd = str(round(m.x,4)) + " x1\n" + str(round(m.y,4))+ " x2\n"
	fd = fd + str(round((-1/2) * (m.x*m.x + m.y*m.y),4))
	return fd

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

def mat_diagonal(clase):
	mc = clase.mat_cov
	m11 = mc[0][0]; m22 = mc[1][1]
	m12 = mc[0][1]
	#Matriz diagonal, con diagonal principal cercana a cero
	if m11<=1 and m11 >=-1 and  m22<=1 and m22 >=-1 and m12==0:
		return True
	return False

#EjercicioTarea
puntos2 = [P(6,9), P(8,10), P(9,11), P(8.5,12), P(7,13.5), P(8,16)]
puntos = [P(0.5,10.5), P(1,12.5), P(3,10.5), P(3,12.5), P(3,14.5), 
	P(3,18), P(5,18), P(5,16), P(5,14.5), P(5,13), ]
#EjercicioClase
puntosc = [P(1,2), P(2,2), P(3,1), P(2,3), P(3,2)]
puntosc2 = [P(8,10), P(9,8), P(9,9), P(8,9), P(7,9)]

l_muestras = [W(puntos), W(puntos2)]

if cov_igual(l_muestras):
	for muestra in l_muestras:
		if mat_diagonal(muestra):
			print("Fucion discriminante\n" + caso3(muestra))
		else:
			print("Fucion discriminante\n" + x1_x2(muestra) +  str(real(muestra)))
else:
	for muestra in l_muestras:
		print("Fucion discriminante\n" + peor_caso(muestra))