#ejercicio 7
list=[0]
fibo = 0
n=int(input('ingrese el valor n: '))

if 0 <= n == 1:
    for i in range(n):
        list.append(n)
        fibo=sum(list)
elif n >= 2:
    list=[0,1]
    for i in range(n-2):
        list.append(list[-1]+list[-2])
    fibo=list[-1]+list[-2]

print('\nLa serie Fibonacci es: %s' %list)
print('F(%d) = %s\n' %(n,fibo))


