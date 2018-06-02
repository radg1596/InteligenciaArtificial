def cov(clase):
	puntos = clase.l_puntos
	media = clase.media
	total = len(clase.l_puntos)
	c11 = 0; c22 = 0; c12 = 0
	for punto in puntos:
		c11 = c11 + (punto.x - media.x) * (punto.x - media.x)
		c22 = c22 + (punto.y - media.y) * (punto.y - media.y)
		c12 = c12 + (punto.x - media.x) * (punto.y - media.y)
	c11=round(c11/total,4); c22 = round(c22/total,4)
	c12 = round(c12/total, 4)
	c = [[c11, c12],[c12, c22]]
	ci = inversa(c)
	return ci
	
def inversa(mat):
	c11 = mat[0][0]; c22 = mat[1][1]
	c12 = mat[0][1]
	det =  (c11*c22) - (c12 * c12)
	ci = [[round(c22/det,4), round((c12*-1)/det,4)], 
		[round((c12*-1)/det,4), round(c11/det,4)]]	
	return ci
	
	
	
	
	
	