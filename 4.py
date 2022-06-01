peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en m: '))

imc = peso / (altura**2)


if imc <= 17:
    print('Muy bajo peso')
elif 17 < imc <= 18.49:
    print('Bajo peso')
elif 18.49 < imc <= 24.99:
    print('Peso normal')
elif 24.99 < imc <= 29.99:
    print('Pasado de peso')    
elif 29.99 < imc <= 34.99:
    print('Obesidad I')
elif 34.99 < imc <= 39.99:
    print('Obesidad II (Severa)')
elif 39.99 < imc:
    print('Obesidad II (Morvida)')             