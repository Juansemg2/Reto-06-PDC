#RETO06

#1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#n = 1
#while ( n>0 and n<101 ):
#  print(n**2)
#  n=n+1
#print("Fin")

#2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

#print("Lista de impares de 1 a 999")
#num = 1
#while (num>0 and num<1001 and num%2!=0):
#    print(num)
#    num=num+2

#print("Lista de pares de 2 a 1000")
#num = 2
#while(num>0 and num<1001 and num%2==0):
#    print(num)
#    num=num+2

#3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
#n= int(input("ingrese un numero entero mayor a 2: "))

#while (n>=2):
#    if(n%2==0):
#        print(n)
#    n=n-1

#4.Imprimir el factorial de un número natural n dado.
#n= int(input("Ingresa un numero entero: "))
#contador=1
#fact=1

#while(contador<=n):
#    fact=contador*fact
#    contador=contador+1
#print(fact)

#5.Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
#n= int(input("imprime un numero entre el 2 y el 50: "))
#mitad= n//2+1
#while (mitad>=2):
#    if (n%mitad==0):
#        print("el numero "+ str(mitad)+ " es divisor")
#    mitad=mitad-1

#6.Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones
#def primo(n):
#    divisor = 2
#    while divisor < n:
#        if n % divisor == 0:
#            return False
#        divisor = divisor+1
#    return True

#n = 1
#while n <= 100:
#    if primo(n):
#        print(n," ")
#    n += 1

