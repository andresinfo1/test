from datetime import date, datetime
fechaok = True

def validarfecha(fec):
    try:
        d=datetime.strptime(fec, '%Y/%m/%d')
        return(d)
    except ValueError:
        print("Fecha inválida")
        fechaok = False


fecha1 = input("Ingresa la primer fecha en el formato DD/MM/YYYY: ")
fecha1 = validarfecha(fecha1)

if fechaok == True:
    fecha2 = input("Ingresa la segunda fecha en el formato DD/MM/YYYY: ")
    fecha2 = validarfecha(fecha2)


if fecha1 > fecha2:
    print('La segunda fecha debe ser mayor a la primera')
else:
    fechafin = fecha2 - fecha1

print('La diferencia en dias entre las fechas es %s ' %str(fechafin)[:-14])        