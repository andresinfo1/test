from math import prod
def menu():
	print ('Selecciona una opción para la operación que quieras realizar')
	print ('\t1 - Suma')
	print ('\t2 - Resta')
	print ('\t3 - Multiplicación')
	print ('\t4 - División')
	print ('\t0 - Salir')

def num_ing(cadena):
	numeros = []
	texto = False
	lista = list(cadena.split(" "))
	for i in range(len(lista)):
		if lista[i] != '':
			try:
				numero = float(lista[i])
				numeros.append(numero)
			except:
					texto = True
					numeros= []
					return(numeros)
	if texto == False:
		return(numeros)

def dividir():
	texto = False
	try:
		dividendo = float(input('Ingrese el dividendo: '))
		divisor = float(input('Ingrese el divisor: '))
	except:
		print('\n¡Ingreso caracteres no numericos!\n')
		texto = True
		resultado = 0
		return(resultado,texto)

	if texto == False:
			resultado = dividendo / divisor
	return(resultado,texto)

def restar():
	texto = False
	try:
		minuendo = float(input('Ingrese el minuendo: '))
		sustraendo = float(input('Ingrese el sustraendo: '))
	except:
		print('\n¡Ingreso caracteres no numericos!\n')
		texto = True
		resultado = 0
		return(resultado,texto)

	if texto == False:
			resultado = minuendo - sustraendo

	return(resultado,texto)		


while True:
	menu()
	opcionMenu = input('Ingrese el numero de la operacion que quiere realizar: ')
	if opcionMenu=='1':
		ingreso = input('\nIngrese los numeros que quiere sumar separados por espacios \n')
		numeros = num_ing(ingreso)
		if numeros == []:
			print('\n¡Ingreso caracteres no numericos!\n')
		else:	
			print('El resultado de la suma es: %.2f 1\n' %sum(numeros))
		input('Presione una tecla para continuar')
	elif opcionMenu=='2':
		resultado,texto = restar()
		if texto == False:
			print('El resultado de la división es: %.2f \n' %resultado)
		input('\nPresione una tecla para continuar')
	elif opcionMenu=='3':
		ingreso = input('\nIngrese los numeros que quiere multiplicar separados por espacios \n')
		numeros = num_ing(ingreso)
		if numeros == []:
			print('\n¡Ingreso caracteres no numericos!\n')
		else:	
			print('El resultado de la multiplicación es: %.2f \n' %prod(numeros))
		input('Presione una tecla para continuar')
	elif opcionMenu=='4':
		resultado,texto = dividir()
		if texto == False:
			print('El resultado de la división es: %.2f \n' %resultado)
		input('Presione una tecla para continuar')
	elif opcionMenu=='0':
		break
	else:
		print ('')
		input('No presiono ninguna opción correcta...\nPresione una tecla para continuar')