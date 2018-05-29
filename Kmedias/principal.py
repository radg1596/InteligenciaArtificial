from funcionesApoyo import *
"""
Clase
Representa a una clase. Tiene su media asociada, su
lista de distancias a cada uno de los puntos y su
lista de atributos seleccionados que usar'a en cada 
iteraci'on
"""
class Kclase():
	"""
	Recibe una media inicial (de tipo P(punto))
	"""
	def __init__(self, media_inicial):
		self.media = media_inicial
		self.distancias = []
		self.seleccionados = []
"""
Abstracci'on que Representa al algoritmo como objeto. Tiene
su lista de puntos, as'i como su lista de clases.
"""
class Kmedias():
	"""
	Inicializaci'on
	Recibe un nombre de archivo
	Crea la lista de clases (vacia)
	Guarda en una lista los puntos le'idos del archivo
	"""
	def __init__(self, nombre):
		self.puntos = self.leer_archivo(nombre)
		self.clases = []
	"""
	No recibe parametros
	Ejecuta el algoritmo kmedias:
		Mientras las medias tengan cambios
			-calcula distancias
			-agrupa puntos en las clases
			-recalcula medias
			-compara las nuevas medias con las anteriores
	"""
	def ejecutar(self):
		continuar = True; ite = 1	
		while continuar:
			input("\nIteracion " + str(ite))
			medias = self.medias_actuales()
			self.calcular_distancias()
			self.imprimir_distancias()
			self.agrupar_puntos()
			self.imprimir_seleccionados()
			nuevas_medias = self.recalcular_medias()
			continuar = comprobar_cambio_medias(medias, nuevas_medias)
			self.imprimir_medias()
			ite = ite+1
	"""
	Recibe una lista de medias
	Guarda cada una de esas medias en la lista "clases" del objeto
	"""
	def inicializar_medias(self, lista):
		self.clases.clear()
		for e in lista:
			self.clases.append(Kclase(e))
	"""
	Recibe un n'umero entero K 
	Introduce k medias seleccionadas aleatoriamente de los puntos
	"""	
	def inicializar_medias_A(self, k):
		self.clases.clear()
		aux = list(self.puntos)
		for i in range(0,k):
			indice_al = random.randrange(0,len(aux))
			self.clases.append( Kclase(aux.pop( indice_al )) )
	"""
	Para cada clase, calcula las distancias a cada uno de los puntos
	"""		
	def calcular_distancias(self):
		for clase in self.clases:
			clase.distancias.clear()
			for punto in self.puntos:
				clase.distancias.append( dist(clase.media, punto) )
	"""
	Asigna cada punto a la clase cuya distancia sea menor a dicho punto.
	"""			
	def agrupar_puntos(self):
		puntos_disponibles = list(self.puntos)
		for clase in self.clases:
			clase.seleccionados.clear()
			clases = list(self.clases); clases.remove(clase)
			clases_restantes = clases
			for i in range(0, len(self.puntos)):
				minimo = min(dist_clases(clases_restantes, i))
				if clase.distancias[i]<minimo and self.puntos[i] in puntos_disponibles:
					clase.seleccionados.append(self.puntos[i])
					puntos_disponibles.remove(self.puntos[i])
				else:
					pass
	"""
	Recalcula las medias de cada clase en base a los puntos
		seleccionados en cada iterac'on
	Retorna una lista, la de nuevas medias	
	"""	
	def recalcular_medias(self):
		nuevas_medias = []
		for clase in self.clases:
			if clase.seleccionados:
				total = len(clase.seleccionados)
				x = 0; y = 0
				for seleccionado in clase.seleccionados:
					x = x + seleccionado.x
					y = y + seleccionado.y
				clase.media = P(x/total, y/total)
				nuevas_medias.append(clase.media)
			else:
				nuevas_medias.append(clase.media)
		return nuevas_medias
	"""
	Toma las medias de la instancia y devuelve una lista de esas medias
	"""
	def medias_actuales(self):
		med_act = []
		for clase in self.clases:
			med_act.append(clase.media)
		return med_act
	"""
	Las siguientes 3 funciones son auxiliares para la impresion de
		los resultados
	"""
	def imprimir_distancias(self):
		for clase in self.clases:
			print ("\nPara la media: "+ str(clase.media))
			print("Distancias: ")
			for i in range(0,len(self.puntos)):
				dis = str(round(clase.distancias[i], 2))
				print("Al punto " + str(self.puntos[i]) + " -> " + dis) 
				
	def imprimir_seleccionados(self):
		for clase in self.clases:
			if clase.seleccionados:
				print("\nPara la media: " + str(clase.media )+ " se seleccionaron los puntos: ")
			else:
				print("Para " + str(clase.media )+ " no hay seleccionados")
			for seleccionado in clase.seleccionados:
				print (seleccionado)
				
	def imprimir_medias(self):
		print ("\nNuevas medias:")
		for clase in self.clases:
			print ("Media"+ str(clase.media))
	"""
	Recibe el nombre de archivo
	retorna una lista de los puntos le'idos de ese archivo
	"""
	def leer_archivo(self, nombre):
		puntos = []
		arch = open(nombre+".txt", "r")
		linea = arch.readline()
		while linea!="":
			lista = linea.split()
			x = lista[0]; y = lista[1]
			puntos.append(P(x,y))
			linea = arch.readline()
		return puntos

"""
Funcion principal
Controla el flujo del programa
"""
def principal():
	kmedias = Kmedias("defaultPuntos")
	kmedias.inicializar_medias(kmedias.leer_archivo("defaultMedias"))
	while True:
		print ("********************KMEDIAS***************************************")
		print("\n1. Ejecutar\n2. Cargar otros puntos\n3. Cargar otras medias\n4. Medias aleatorias\n5. Salir\n")
		leer = input("Opcion: ")
		opcion = int(leer)
		if opcion == 1:
			kmedias.ejecutar()
		elif opcion == 2:
			nombre = input("Nombre archivo: ")
			kmedias.puntos = kmedias.leer_archivo(nombre)
		elif opcion == 3:
			nombre = input("Nombre archivo: ")
			medias = kmedias.leer_archivo(nombre)
			kmedias.medias = kmedias.inicializar_medias(medias)
		elif opcion == 4:
			k = int(input("K: "))
			kmedias.medias =kmedias.inicializar_medias_A(k)
		else:
			break

			
principal()