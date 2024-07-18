
dolar = 0.91
libra = 1.18

conversion = input("¿Que quieres convertir a euro?\n"
                   "A=Euro a dolar\n"
                   "B=Dolar a euro\n"
                   "C=Euro a libra\n"
                   "D=Libra a Euro")
texto_usuario = "Ingrese la cantidad de {}:  "

if conversion == "A":
    cantidad_conver = int(input(texto_usuario.format("Dolares")))
    dolar_euro = cantidad_conver * dolar
    print("La conversion es: {} Dolares".format(dolar_euro))

elif conversion == "B":
    cantidad_conver = int(input(texto_usuario.format("Euros")))
    dolar_euro = cantidad_conver / dolar
    print("La conversion es: {} Euros".format(dolar_euro))

elif conversion == "C":
    cantidad_conver = int(input(texto_usuario.format("Libras")))
    libra_euro = cantidad_conver * libra
    print("La conversion es: {} Libras".format(libra_euro))

elif conversion == "D":
    cantidad_conver = int(input(texto_usuario.format("Euros")))
    libra_euro = cantidad_conver / libra
    print("La conversion es: {} Euros".format(libra_euro))





