respuesta = 's'
while respuesta == 's':
    divisores = []
    numero = int(input('Ingrese un numero entero: '))

    for i in range(1,numero+1):
        if numero % i  == 0:
            divisores.append(i)

    if len(divisores) == 2:
        print('El numero %d es un numero primo' %numero)
    else:
        div_str = str(divisores)[1:-1]
        print('Los divisores de %d son %s' %(numero, div_str))
    
    respuesta = input('\n ¿Desea introducir otro numero? "s" "n" :   ').lower()
    if respuesta == 'n':
        break           
