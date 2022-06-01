import numpy as np

vector2 = np.array([['jose','luis','maria','pablo','eva'],[20,31,49,42,30]])

mayor = max(vector2[1])

lugar = int(np.where(vector2[1] == mayor)[0]) 
# np.where devuelve el indice del elemento en forma de tupla, donde el segundo elemento de la tupla esta vacio.
# para eso se agrega al final [0] 
# como vector2 está compuesto por 2 array mediante vector2[1] especifico que busque en el segundo array
# finalmente con int lo parseo a entero

nombre = vector2[:,lugar]

print(mayor,lugar,nombre)
