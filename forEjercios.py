
"""
texto = input("Introduzca el texto")
espacios = " "
comas = ","
puntos = "."

num_espacios = 0
num_comas = 0
num_puntos = 0

for letras in texto:
    if letras in espacios:
        num_espacios += 1
    elif letras in comas:
        num_comas += 1
    elif letras in puntos:
        num_puntos += 1

print("Este es el numero de espacios {}".format(num_espacios))
print("Este es el numero de comas {}".format(num_comas))
print("Este es el numero de puntos {}".format(num_puntos))

import string
texto = input("Introduzca el texto")

mayusculas = 0

for letras in texto:
    if letras in string.ascii_uppercase:
        mayusculas += 1
print("El total de mayusculas es {}".format(mayusculas))"""

"""
tabla = int(input("introduzca la tabla que quiera saber"))

for numero in range (1,11):
    a = numero % 2
    if a == 0:
        print("{} x {}= {}" .format(numero, tabla, numero * tabla))"""

numero_usuario = input("Introduzca lista de numeros ")
numero_introducido = [int(numero) for numero in numero_usuario.split(",")]

print(numero_introducido)

print(min(numero_introducido))
print(max(numero_introducido))
