import numpy as np

vector = np.array([1,2,3,4,5,6,7,8,9,10])

numero = int(input('Ingrese el numero a buscar: '))

lugar = np.where(vector == numero)[0] #Busca el numero en el vector
lugar_str = str(lugar)[1:-1] #En este método, convierte una lista en string usando la función str() y luego elimina el primer y último carácter de esta cadena que son los corchetes.


if (lugar_str == ''):
    print ('\nEl numero no se encuentra en el vector')
else:    
    print ('\nEl numero se encuentra en el lugar: %s' %lugar_str)

vector.sort() #Este método ordena el vector de menor a mayor

print('\nEl vector ordenado queda de la siguiente forma: ', vector)