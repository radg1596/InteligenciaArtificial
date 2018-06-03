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
def caso_sencillo(clase):
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