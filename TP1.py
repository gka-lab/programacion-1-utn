#Ej 1

print("Ejercicio 1: ")
print("Hola Mundo!")

#Ej 2

print("Ejercicio 2: ")
nombre = input("Ingrese su nombre: ")
print(f"¡Hola {nombre}!")

#Ej 3

print("Ejercicio 3: ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

#Ej 4

print("Ejercicio 4: ")
radio = int(input("Ingrese el radio de un círculo: "))
pi = 3.14159
area = pi * radio**2
perimetro = 2 * pi * radio

print(f"Para el radio ingresado, el área es {area} y el perímetro es {perimetro}")

#Ej 5

print("Ejercicio 5: ")
segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = segundos / 60
horas = minutos / 60

print(f"{segundos} segundos equivalen a {horas} hora/horas.")

#Ej 6

print("Ejercicio 6: ")
numero = int(input("Ingrese un número: "))

multiplicador = 1

while multiplicador < 11:
    print(f"{numero} x {multiplicador} = {numero*multiplicador}")
    multiplicador = multiplicador + 1

#Ej 7

print("Ejercicio 7: ")
num1 = int(input("Escriba un número distinto de cero: "))

while num1 == 0:
 num1 = int(input("El número debe ser distinto de 0. Vuelva a ingresarlo: "))
            
num2 = int(input("Escriba otro número distinto de cero: "))

while num2 == 0:
 num2 = int(input("El número debe ser distinto de 0. Vuelva a ingresarlo: "))
            
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} x {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")

#Ej 8

print("Ejercicio 8: ")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))

imc = peso / altura**2

print(f"El índice de masa muscular que usted posee es de {imc}.")


#Ej 9

print("Ejercicio 9: ")
celcius = float(input("Ingrese la temperatura en grados Celcius: "))

fahrenheit = (9/5) * celcius + 32

print(f"{celcius} grados Celcius equivalen a {fahrenheit} grados Fahrenheit")

#Ej 10

print("Ejercicio 10: ")
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
num3 = float(input("Ingrese otro número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de {num1}, {num2} y {num3} es {promedio}.")