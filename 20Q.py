def adivinar_persona():

    resp = input("¿Es una figura histórica o actual? ")
    if resp == "si":
        # artista
        resp = input("¿Es famoso en el arte? ")
        if resp == "si":

            resp = input("")  

        else:
            # científico
            resp = input("¿Es reconocido por sus descubrimientos científicos? ")
            if resp == "si":

                resp = input("")

            else:
                # político
                resp = input("¿Es una figura política reconocida? ")
                if resp == "si":

                    resp = input("")

                else:
                    # actor
                    resp = input("¿Es actor o actriz? ")
                    if resp == "si":
                        resp = input("")
    else:
        resp = input("")


def adivinar_ave():

    resp = input("¿Es un ave de gran tamaño? ")
    if resp == "si":

        resp = input("¿Tiene un cuello largo? ")
        if resp == "si":
            resp = input("")

    else:
        # paloma
        resp = input("¿Suele vivir cerca de humanos? ")
        if resp == "si":

            print("Tu animal es un paloma") 

        else:
            resp = input("¿Tiene colores llamativos? ")
            if resp == "si":

                resp = input("")


def adivinar_acuatico():

    resp = input("¿Es un mamífero marino? ")
    if resp == "si":

        resp = input("¿Es muy grande? ")
        if resp == "si":

            resp = input("")
    else:

        # tortuga
        resp = input("¿Tiene concha o caparazón? ")
        if resp == "si":

            print("Tu animal es una tortuga marina")
        else:
            # cangrejo
            resp = input("¿Tiene pinzas o tenazas? ")
            if resp == "si":

                print("Tu animal es un cangrejo")
            else:
                # pulpo
                resp = input("¿Tienetentáculos? ")
                if resp == "si":

                    print("Tu animal es un pulpo")
                else:

                    resp = input("¿Tiene cuerpo alargado y aletas? ")
                    if resp == "si":

                        # tiburón
                        resp = input("¿Es un pez depredador? ")
                        if resp == "si":

                            print("Tu animal es un tiburón")
                    else:

                        # medusa
                        print("Tu animal es una medusa")


def adivinar_terrestre():

    resp = input("¿Es carnívoro? ")
    if resp == "si":

        # felinos
        resp = input("¿Es un felino? ")
        if resp == "si":
            #LEON
            resp = input("¿Tiene melena? ")
            if resp == "si":

                print("Es un león")

            else:
                
                resp = input(" ")
                if resp == "si":

                    resp = input(" ")

        else:

            resp = input("¿Es un canino? ")
            if resp == "si":

                resp = input("")

    else:
        resp = input("¿Es un animal de granja? ")
        if resp == "si":

            # vaca
            resp = input("¿Da leche? ")
            if resp == "si":

                print("Es una vaca")

            resp = input("")
        else:

            resp = input("¿Es un roedor? ")
            if resp == "si":

                resp = input("")
            

def adivinar_animal():

    resp = input("¿Puede volar? ")
    if resp == "si":
        adivinar_ave()
    else:
        resp = input("¿habita en el agua? ")
        if resp == "si":
            adivinar_acuatico()
        else:
            adivinar_terrestre()


def adivinar_planta():
    resp = input("¿ ? ")
    if resp == "si":

        resp = input("")


def Juego():

    activo = "si"
    print("Recuerda que tus respuestas se deben limitar a 'si' y 'no'.")

    while activo == "si":
        #ANIMAL ----------------------------------------------------------------------------

        resp = input("¿Es un ser vivo? ")
        if resp == "si":

            resp = input("¿Es capaz de moverse por sí mismo? ")
            if resp == "si":

                #PERSONAS
                resp = input("¿Tiene una alta capacidad de razonamiento? ")
                if resp == "si":

                    adivinar_persona()
                else:
                    adivinar_animal()
            else:
                #PLANTAS
                adivinar_planta()
        else:
            # COMIDA -------------------------------------------------------------------------
            resp = input("")



        activo = input("Acabó el juego, ¿quieres volver a jugar? (si/no) ")


print("Bienvenido a 20 Preguntas.")
print("Antes de iniciar, piensa en una palabra y yo trataré de adivinarla con 20 preguntas (o menos)")
print("¿Listo? Vamos!")
Juego()
