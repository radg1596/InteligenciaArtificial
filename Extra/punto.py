"""Clase Punto
Cuenta con los atributos:
	-x
	-y
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