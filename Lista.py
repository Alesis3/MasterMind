
lista_de_compras = []
respuesta = None

while respuesta != "Q":
    respuesta = input("Que desea comprar? [Q]Para salir")

    if respuesta == "Q":
        pass

    elif respuesta in lista_de_compras:
        print("{} Ya esta en la lista de compra".format(respuesta))

    else:
        confirmacion = input("Seguro que desea comprar {}? [S]Si, [N]No".format(respuesta))
        if confirmacion == "S":
            lista_de_compras.append(respuesta)

print("Salio del supermercado \n "
      "La lista de compra es {}".format(lista_de_compras))
