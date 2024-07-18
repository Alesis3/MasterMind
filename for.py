
vocales = ("A", "E", "I", "O", "U")
#vocales = ("a", "e", "i", "o", "u")
frase = "Aqui con el famoso kiricu"
vocales_encontradas = 0

for letras in frase:
    if letras.upper() in vocales:
        print("Se han encontrado {}".format(letras))
        vocales_encontradas += 1

print("En total son {}".format(vocales_encontradas))

repeticiones = int(input("Numero de repeticiones?"))
for a in range(repeticiones + 1):
    print(a)


