
celular = input("¿Que sistema operativo quieres?\n"
                "A=Android \n"
                "B=iOS")

dinero = input("¿Tienes dinero? Si/No")
cel_recomendado = "Ninguno"

if celular == "A":
    if dinero == "Si":
     camara = input("¿Importa la camara? Si/No")
     if camara == "Si":
         cel_recomendado = "Google pixel supercamara"
     else:
         cel_recomendado = "Android calidad-precio"
    else:
        cel_recomendado =  "celular chino"

elif celular == "B":
    if dinero == "Si":
        cel_recomendado = "iPhone ultra pro max"
    else:
        cel_recomendado = "uno de segunda mano"

print("Te recomiendo el " + cel_recomendado)
