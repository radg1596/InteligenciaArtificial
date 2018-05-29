"""Clase Punto
Cuenta con los atributos:
	-x
	-y
Y los métodos:
	-Convertir a string
	-Comprobar diferencia
"""
class P():
	"""incializacion
	Recibe la coordenada x, y la coordenada y como enteros o flotantes
	Guarda estos datos como flotantes en la instancia
	"""
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
	"""
	A String
	Se encarga de retornar una cadena que representa al punto.
		-> "( 1, 2 )"
	"""
	def __str__ (self):
		return "(" + str(round(self.x, 3)) + ", "+str(round(self.y,3))+")"
	"""
	Diferencia
	Nos dice si dos instancias de tipo P() (punto) son diferentes
	Retorna True si son diferentes, en otro caso False
	Ejemplo:
	p1 = P(1,2)
	p2 = P(3,4)
	p1 != p2 -> True
	"""	
	def __ne__(self, puntoB):
		if puntoB.x != self.x or puntoB.y != self.y:
				return True
		return False