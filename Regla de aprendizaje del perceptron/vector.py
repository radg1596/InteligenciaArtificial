"""
Clase Vector
Cada instancia de esta clase cuenta con dos atributos:
	-dimension: Es un número entero que indica la dimensión del vector
	-numeros: Es una lista que contiene las componentes del vector (flotantes)
También, cada instancia de esta clase cuenta con los siguientes métodos:
	-Convertir a tipo "cadena"
	-Suma
	-Producto punto
	-Multiplicación por un escalar
	-Diferencia
	-nulo
"""
class V():
	"""
	Inicialización
	-Recibe como parámetro una cadena, la cual contiene las componentes del
		vector. Por ejemplo: "4 6 -3 6 5" (vector de dimensión 5).
	
	-Se encarga de guardar las componentes del vector como tipo flotantes 
		en una lista llamada "numeros". Además obtiene y guarda su dimensión.
		
	-No retorna nada.
	"""
	def __init__(self, entrada):
		self.numeros = []
		self.dimension = len(entrada.split())
		for numero in entrada.split():
			self.numeros.append(float(numero))
	"""
	Convertir a tipo cadena(str())
	-No recibe ningún parámetro.
	
	-Se encarga de construir una cadena para representar al vector, de tal 
		forma que pueda imprimirse con "print".
		
	-Retorna la instancia representada como tipo cadena.
	
	-Ejemplo:
		Si creamos un vector
		vect = V("0 0 1")
		E intentamos imprimirlo
		print (vect)
		Este método es llamado y retorna:
		"[ 0, 0, 1]"
	"""	
	def __str__(self):
		aux = "[ "
		for numero in self.numeros:
			aux = aux + str(round(numero,2)) + ", "
		return aux[0:len(aux)-2]+" ]"
	"""
	Suma de dos vectores (+)
	-Recibe como parámetro a un vector
	
	-Se encarga de sumar componente a componente a la instancia 
		con el vector recibido (debe ser de dimensión compatible).
		
	-Retorna un vector, el cual es la suma del recibido con la instancia.
	
	-Este método es llamado cuando intentamos sumar dos instancias de tipo V (vector)
		Por ejemplo:
			v1 = V("1 2 3")
			v2 = V("3 4 5")
			v3 = v1 + v2
	"""
	def __add__(self, vectb):
		if self.dimension == vectb.dimension:
			vectc = V(""); vectc.dimension = self.dimension
			for i in range(0,self.dimension):
				vectc.numeros.append(self.numeros[i]+vectb.numeros[i])
			return vectc
		else:
			print("Error de dimension en la suma de vectores.")
	"""
	Producto punto de dos vectores (*)
	-Recibe como parámetro a un vector (debe ser de dimensión compatible).
	
	-Se encarga de multiplicar componente a componente (de la instancia 
		y del vector recibido) y va acumulando la suma.
		
	-Retorna un flotante, el cual producto punto del vector recibido con la instancia.
	
	-Este método es llamado cuando intentamos multiplicar dos instancias de tipo V (vector)
		Por ejemplo:
			v1 = V("4 5 6")
			v2 = V("8 6 7")
			v3 = v1 * v2
	"""
	def __mul__(self, vectb):
		if self.dimension == vectb.dimension:
			producto = 0
			for i in range(0,self.dimension):
				producto = producto + self.numeros[i]*vectb.numeros[i]
			return producto
		else:
			print("Error de dimension en el producto punto de vectores.")
	"""
	Multiplicación de un vector por un escalar
	-Recibe un escalar de tipo flotante
	
	-Se encarga de multiplicar cada una de las componentes de la instancia con el
		escalar recibido
	
	-Retorna un vector, el cual es el vector resultante
	
	-Ejemplo:
		v = V("1 2 3")
		v.esc(2)
		Retorna:
		V("2 4 6")
	"""	
	def esc(self, esc):
		vectb = V(""); vectb.dimension = self.dimension
		for numero in self.numeros:
			vectb.numeros.append(numero*esc)
		return vectb
	"""
	Diferencia ( != ) 
	-Recibe a un vector como parámetro
	-Compara a la instancia con el vector recibido
	-Retorna True si son diferentes, en caso contrario False
	"""
	def __ne__(self, vectb):
		if (self + vectb.esc(-1.0)).nulo()== False:
			return True
		return False
	"""
	Nulo
	No recibe ningun parámetro
	Retorna True si las componentes del vector son todas ceros.
		y en caso contrario False.
	"""
	def nulo(self):
		for numero in self.numeros:
			if numero!=0.0:
				return False
		return True