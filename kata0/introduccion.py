#program.py
sum = 1 + 2
print(sum)

#variables

sum = 1 + 2 #3
product = sum * 2
print(product)


#dates
from datetime import date
date.today()
print(date.today())

print("Today's date is: " + str(date.today()))

#ENTRADA AL USUARIO

print("Bienvenido al programa de bienvenida")
name = input("Introduzca  su nombre")
#print("Saludos: " + name)

#TRABAJAR CON NÚMEROS

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))
