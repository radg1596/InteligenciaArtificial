from vector import *
"""
Función escalón unitario
-Recibe como parámetro un número flotante

-Retorna 1.0 si el número recibido es mayor o igual a cero,
	en caso contrario -1.0
"""
def f_escalon(numero):
	return 1.0 if numero>=0.0 else -1.0
"""
Clase muestra
Tiene dos atributos:
	x: Es el vector de entrada de la muestra
	resultado: Es la clase a la que pertenece la muestra
"""
class Muestra():
	"""
	Inicialización
	-Recibe como parámetro un vector x, así como la clase
		a la que pertenece.
	"""
	def __init__(self, x, clase):
		self.x = x
		self.resultado = clase
"""
Clase perceptron
Tiene los siguientes atributos:
	-listaMuestras: Es una lista que contiene cada una de las muestras que serán utilizadas.
	-dimensionW: Es la dimensión que debe tener el vector W al ser inicializado a cero.
	-w: Es el vector de pesos.
	-n: Es la tasa de aprendizaje.
	-max_ite: Es el número máximo de iteraciones
"""		
class Perceptron():
	"""
	Inicialización
	-Recibe un nombre de archivo
	-Carga los datos necesarios a partir de ese archivo y estable en 0.1
		la tasa de aprendizaje como default. Además establece un máximo
		de 1000 iteraciones.
	"""
	def __init__(self, nombre):
		self.listaMuestras, self.dimensionW = self.cargar_datos(nombre)
		self.n = 0.1
		self.max_ite = 1000
	"""
	Recibe un vector de entrada
	Lo evalua en la red neuronal y obtiene su salida 
	"""
	def reconocer(self, entrada):
		try:
			x = V("1 " + entrada)
			return f_escalon(self.w * x)
		except:
			return "Error en el formato de entrada o la red no ha sido entrenada"
		
	"""
	No recibe parámetros
	Se encarga de ejecutar el algoritmo de aprendizaje del perceptrón. 
			se detiene cuando el vector de pesos deja de tener cambios.
	"""
	def aprender(self):
		w = self.w = self.inicializar_pesos(); ite =0; pesos = ""
		for i in range(0, self.max_ite):
			for muestra in self.listaMuestras:
				salida = f_escalon(w * muestra.x)
				deltaW = self.n * ( muestra.resultado - salida )
				w = w + muestra.x.esc(deltaW)
				cambio_pesos = True if self.w != w else False
				self.w = w
			pesos = pesos +"Pesos: " + str(self.w) + "\n"
			if cambio_pesos==False:
				return pesos	
		return "Se soprepasó el máximo de iteraciones"
	"""
	-Recibe como parámetro el nombre de un archivo.
	-Se encarga de cargar las muestras a partir de ese archivo. Además, averigua
		que dimensión debería tener el vector de pesos.
	-Retorna una lista de muestras y la dimension adecuada del vector de pesos (entero).
	"""
	def cargar_datos(self, nombre):
		listaMuestras = []
		arch = open(nombre+".txt", "r")
		linea = arch.readline()
		while linea!="":
			x = linea[0:linea.find('|')]
			clase = linea[linea.find('|')+1: len(linea)]
			listaMuestras.append( Muestra(V(x), float(clase)) )
			linea = arch.readline()
		dimensionW = len(x.split())
		return listaMuestras, dimensionW
	"""
	Se encarga de inicializar el vector de pesos a cero. De tal manera que
	tenga una dimensión compatible con las muestras.
	"""	
	def inicializar_pesos(self):
		aux = ""
		for i in range (0, self.dimensionW ):
			aux = aux + " 0"
		return V(aux)
			

"""
Es la función principal
Se encarga de desplegar un menu, así como controlar el flujo de
todo el programa.
"""
def principal():
	perceptron = Perceptron("nand2")
	while True:
		print ("********************Perceptron**************************")
		print("\nSelecciona una opcion: \n1.Entrenar \n2.Selecciona otro archivo \n3.Cambiar la tasa de aprendizaje \n4.Reconocer \n5.Salir ")
		opc = int(input("\nOpcion: "))
		if opc == 1:
			print(perceptron.aprender())
		elif opc ==2: 
			nombre = input("\nNombre de archivo:")
			perceptron.listaMuestras, perceptron.dimensionW  = perceptron.cargar_datos(nombre)
			print("\nSe recargaron los datos")
		elif opc == 3:
			perceptron.n = float(input("\nNueva tasa de aprendizaje: "))
		elif opc == 4:
			while True:
				en = input("Vector de entrada: ")
				if en == "salir":
					break
				print("Salida: " + str(perceptron.reconocer(en)))
		else:
			break
		
principal()