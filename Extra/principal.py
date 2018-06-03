from funciones import *
"""
Recibe el nombre del archivo
Se encarga de leer los puntos de cada clase
Retorna una lista de muestras
"""
def leer_datos(nombre):
	arch = open(nombre)
	linea = arch.readline()
	puntos_clase = []
	lista_muestras = []
	while linea!="":
		pl = linea.split()
		if pl[0] == ";":
			lista_muestras.append(W(list(puntos_clase)))
			puntos_clase.clear()
		else:
			for p in pl:
				xy = p.split(',')
				x = float(xy[0]); y = float(xy[1])
				puntos_clase.append(P(x,y))
		linea = arch.readline()
	return list(lista_muestras)
		
#No olvidar los ';' al final de cada clase en el archivo
"""
Recibe una lista de muestras
Dependiendo del caso, imprime la funcion discriminante
correspondiente
"""
def ejecutar(muestras):
	i = 0
	if cov_igual(muestras):
		for muestra in muestras:
			i = i+1
			if mat_diagonal(muestra):
				print("\nfd" + str(i) +"=\n" + caso_sencillo(muestra))
			else:
				print("\nfd" + str(i) +"=\n" + x1_x2(muestra) +  str(real(muestra)))
	else:
		for muestra in muestras:
			i = i+1
			print("\nfd" + str(i) + "=\n" + peor_caso(muestra))

"""
Funcion pricipal
Es la interaccion entre el usuario y el programa, controla
el flujo del mismo
"""
def menu():
	l_muestras = leer_datos("clase")
	while True:
		print ("\n1.Ejecutar\n2.Elegir otro archivo\n3.Salir")
		op = input("Opcion: ")
		if op == "1":
			if l_muestras:
				ejecutar(l_muestras)
			else:
				print("Introduce un archivo valido\n")
		elif op == "2":
			nombre = input("Archivo: ")
			try:
				l_muestras.clear()
				l_muestras = leer_datos(nombre)
				print ("\nSe recargaron los datos")
			except OSError:
				print("El archivo no existe!")
		elif op == "3":
			break
		else:
			pass
		
menu()