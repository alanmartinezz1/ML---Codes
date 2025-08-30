# Machine Learning - Práctica 1: 20 Preguntas

def Juego():
    activo = "si"
    print("Recuerda que tus respuestas se deben limitar a 'si' y 'no'.")

    while activo == "si":
        
        #seres vivos
            resp = input("¿Es un ser vivo?")
            if resp == "si":

                #animales
                resp = input("¿es capaz de moverse por sí mismo?")
                if resp == "si":

                    #personas
                    resp = input("¿Tiene una alta capacidad de razonamiento?")
                    if resp == "si":

                        #
                        resp = input("")

                    #aereos
                    resp = input("¿puede volar?")
                    if resp == "si":
                        #
                        resp = input("")
                
                    #acuatico
                    resp = input("¿habita en el agua?")
                    if resp == "si":
                        #
                        resp = input("")

                    #terrestre
                    resp = input("¿es carnivoro?")
                    if resp == "si":
                        resp = input("")
                
                #plantas
                resp = input("")
                if resp == "si":
                    
                    resp = input("")


        #comida
            if resp == "si":
                #
                resp = input("")

        #instrumentos musicales


        #transporte


        #electrónicos



        
    activo = input("Acabó el juego, ¿quieres volver a jugar? (si/no)")


print("Bienvenido a 20 Preguntas.")
print("Antes de iniciar, piensa en una palabra y yo trataré de adivinarla con 20 preguntas (o menos)")
print("¿Listo? ¡Vamos! :D")
Juego()