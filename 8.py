inv_I = 100
interes_m = 1
interes_a = (1+(interes_m/100))

for i in range(11):
    interes_a = interes_a*(1+(interes_m/100))

saldo = inv_I*interes_a
print(saldo,interes_a)
