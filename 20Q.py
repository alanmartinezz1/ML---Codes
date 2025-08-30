# Machine Learning - Práctica 1: 20 Preguntas

def Juego():
    activo = "si"
    print("Recuerda que tus respuestas se deben limitar a 'si' y 'no'.")

    while activo == "si":
        
        #seres vivos ---------------------------
        resp = input("¿Es un ser vivo? ")
        if resp == "si":

            #animales ------------------------
            resp = input("¿Es capaz de moverse por sí mismo? ")
            if resp == "si":

                #personas ---------------------------
                resp = input("¿Tiene una alta capacidad de razonamiento? ")
                if resp == "si":

                    resp = input("¿Es una figura histórica o actual? ")
                    if resp == "si":

                        #artista
                        resp = input("¿Es famoso en el arte? ")
                        if resp == "si":

                            resp = input("")
                            
                        else:
                            #Cientifico
                            resp = input("¿Es reconocido por sus descubrimientos científicos? ")
                            if resp == "si":

                                resp = input("")

                            else:
                                #politico
                                resp = input("¿Es una figura política reconocida? ")
                                if resp == "si":

                                    resp = input("")
                                else:
                                    #actor
                                    resp = input("¿Es actor o actriz? ")
                                    if resp == "si":

                                        resp = input("")

                    else:
                        resp = input("")

                else:

                    #animales aéreos ----------------------------------
                    resp = input("¿Puede volar? ")
                    if resp == "si":

                        resp = input("¿Es un ave de gran tamaño? ")
                        if resp == "si":

                            resp = input("¿Tiene un cuello largo? ")
                            if resp == "si":

                                resp = input("")
                        else:
                            #PALOMA
                            resp = input("¿Suele vivir cerca de humanos? ")
                            if resp == "si":
                                
                                print("Tu animal es una paloma")

                            else:
                                resp = input("¿Tiene colores llamativos? ")
                                if resp == "si":

                                    resp = input("")

                    else:
                        #animales acuáticos ---------------------------------------
                        resp = input("¿habita en el agua?")
                        if resp == "si":

                            resp = input("¿Es un mamífero marino?")
                            if resp == "si":

                                resp = input("¿Es muy grande?")
                                if resp == "si":

                                    resp = input("")
                            else:
                                #TORTUGA
                                resp = input("¿Tiene concha o caparazón?")
                                if resp == "si":

                                    print("Tu animal es una tortuga marina")
                                else:
                                    #CANGREJO
                                    resp = input("¿Tiene pinzas o tenazas?")
                                    if resp == "si":

                                        print("Tu animal es un cangrejo")
                                    else:

                                        #PULPO
                                        resp = input("¿Tienetentáculos?")
                                        if resp == "si":

                                            print("Tu animal es un pulpo")
                                        else:

                                            resp = input("¿Tiene cuerpo alargado y aletas?")
                                            if resp == "si":

                                                #TIBURON
                                                resp = input("¿Es un pez depredador?")
                                                if resp == "si":
                                                    
                                                    print("Tu animal es un tiburón")
                                                
                                            else:
                                                #MEDUSA
                                                print("Tu animal es una medusa")


                        else:
                            #animales terrestres -------------------------------
                            resp = input("¿Es carnívoro? ")
                            if resp == "si":

                                #Felino
                                resp = input("¿Es un felino? ")
                                if resp == "si":

                                    #LEON
                                    resp = input("¿Tiene melena? ")
                                    if resp == "si":

                                        print("Es un león")

                                    else:
                                        #TIGRE
                                        print("Es un tigre")
                                else:
                                    resp = input("¿Es un canino? ")
                                    if resp == "si":

                                        resp = input("")

                                    else:
                                        resp = input("")

                            else:

                                resp = input("¿Es un animal de granja? ")
                                if resp == "si":

                                    #VACA
                                    resp = input("¿Da leche? ")
                                    if resp == "si":

                                        print("Es una vaca")
                                    
                                    resp = input("")


                                else:
                                    resp = input("¿Es un roedor? ")
                                    if resp == "si":

                                        resp = input("")
                                    
                                    resp = input("")

            else:
                #plantas -------------------------------------------------------------
                resp = input("¿? ")
                if resp == "si":

                    resp = input("")
                   


        #comida

            resp = input("")

        #instrumentos musicales


        #transporte


        #electrónicos



        
    activo = input("Acabó el juego, ¿quieres volver a jugar? (si/no)")


print("Bienvenido a 20 Preguntas.")
print("Antes de iniciar, piensa en una palabra y yo trataré de adivinarla con 20 preguntas (o menos)")
print("¿Listo? ¡Vamos! :D")
Juego()