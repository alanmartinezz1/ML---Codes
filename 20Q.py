def pedir_si_no(pregunta):
    """Pide repetidamente hasta que el usuario responda 's' o 'n' (acepta 'si'/'no')."""
    while True:
        r = input(pregunta + " (s/n): ").strip().lower()
        if r in ("s", "si", "sí"):
            return "s"
        if r in ("n", "no"):
            return "n"
        print("Por favor responde 's' (sí) o 'n' (no).")

#--------------------------------------------  RAMAS PRINCIPALES --------------------------------------------#
def rama_abstracto():
    """Rama para conceptos abstractos e intangibles"""
    print("\n--- CATEGORÍA: ABSTRACTOS/INTANGIBLES ---")
    
    r = pedir_si_no("Q3: ¿Está relacionado con emociones o sentimientos?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es una emoción positiva?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Se siente hacia otras personas?")
            if r == "s":
                r = pedir_si_no("Q6: ¿afecto profundo?")
                if r == "s":
                    print("EMOCIÓN: amor")
                else:
                    r = pedir_si_no("Q7: ¿Implica agradecimiento hacia otro?")
                    if r == "s":
                        print("EMOCIÓN: gratitud")
                    else:
                        r = pedir_si_no("Q8: ¿Es admiración hacia alguien o algo?")
                        if r == "s":
                            print("EMOCIÓN: respeto")
                        else:
                            r = pedir_si_no("Q9: ¿Es entusiasmo o motivación?")
                            if r == "s":
                                print("EMOCIÓN: entusiasmo")
                            else:
                                print("EMOCIÓN POSITIVA GENERAL: felicidad/placer")
            else:
                r = pedir_si_no("Q6: ¿Es expectativa positiva hacia el futuro?")
                if r == "s":
                    print("EMOCIÓN: esperanza")
                else:
                    print("Q7: ¿Es sensación de paz y armonía?")
                    if r == "s":
                        print("EMOCIÓN: serenidad")
                    else:
                        print("EMOCIÓN POSITIVA GENERAL: placer, satisfacción, bienestar")
        else:
            # emociones negativas
            r = pedir_si_no("¿Involucra a otras personas?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Se relaciona con la comparación?")
                if r == "s":
                    r = pedir_si_no("Q7: ¿Es envidia o celos?")
                    if r == "s":
                        print("EMOCION NEGATIVA: envidia")
                    else:
                        r = pedir_si_no("Q8: ¿Es más una emoción de juicio social?")
                        if r == "s":
                            print("EMOCION NEGATIVA: Vergüenza o humillación")
                else:
                    r = pedir_si_no("Q7: ¿Puede provocar llanto y malestar?")
                    if r == "s":
                        print("EMOCION NEGATIVA: Tristeza")
                    else:
                        r = pedir_si_no("Q8: ¿causa irritación intensa?")
                        if r == "s":
                            print("EMOCION NEGATIVA: Enojo, odio o ira")
                        else:
                            print("Q9: ¿Es una respuesta ante una amenaza?")
                            if r == "s":
                                r = pedir_si_no("Q10: ¿la amenaza es un un peligro presente, claro y conocido?")
                                if r == "s":
                                    print("EMOCION NEGATIVA: miedo")
                                else:
                                    print("EMOCION NEGATIVA: ansiedad")
            else:
                r = pedir_si_no("Q6: ¿Se relaciona con el pasado?")
                if r == "s":
                    r = pedir_si_no("Q7: ¿Tiene que ver con recordar momentos buenos?")
                    if r == "s":
                        print("EMOCION NEGATIVA: Nostalgia")
                    else:
                        r = pedir_si_no("Q8: ¿Surge del remordimiento?")
                        if r == "s":
                            print("EMOCION NEGATIVA: Culpa")
                
        return
    
    r = pedir_si_no("Q3: ¿Es un concepto matemático o numérico?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es un número específico?")
        if r == "s":
            print("NÚMEROS: enteros, decimales, fracciones, números primos, π, e, etc")
        else:
            r = pedir_si_no("Q5: ¿Es una operación matemática?")
            if r == "s":
                print("OPERACIONES: suma, restas, multiplicacion, división, potencia, raíz, integral, derivada")
            else:
                r = pedir_si_no("Q6: ¿Se relaciona con magnitudes y medidas?")
                if r == "s":
                    print("MAGNITUDES: Longitud, area, volumen")
                else:
                    r = pedir_si_no("Q7: ¿Es una rama de las matemáticas?")
                    if r == "s":
                        print("RAMA MATEMATICA: Algebra, geometría, trigonometría, probabilidad, estadisitca, calculo, ")

        return
    
    r = pedir_si_no("Q3: ¿Es una idea filosófica o concepto abstracto?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Está relacionado con la existencia o la realidad?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Se refiere al mero hecho de existir?")
            if r == "s":
                print("ABSTRACTO: Existencia, Ser")
            else: 
                r = pedir_si_no("Q6: ¿Es lo opuesto (ausencia total)?")
                if r == "s":
                    print("ABSTRACTO: Nada")
                else:
                    r = pedir_si_no("Q7: ¿se refiere a la existencia real y efectiva de algo?")
                    if r == "s":
                        print("ABSTRACTO: Realidad")
                    else:
                        r = pedir_si_no("Q8: ¿Es el estado de conocimiento de la realidad interna?")
                        if r == "s":
                            print("ABSTRACTO: Consciencia")
        else:
            r = pedir_si_no("Q5: ¿Se relaciona con las Dimensiones Universales")
            if r == "s":
                r = pedir_si_no("Q6: ¿Es una medida continua?")
                if r == "s":
                    print("DIMENSIONES: Tiempo")
                else:
                    r = pedir_si_no("Q7: ¿Es la extensión que ocupa un objeto?")
                    if r == "s":
                        print("DIMENSIONES: Espacio")


        return
    
    r = pedir_si_no("Q3: ¿Está relacionado con el tiempo?")
    if r == "s":
        print("CONCEPTOS TEMPORALES: tiempo, eternidad, momento, pasado, presente, futuro")
        return
    
    r = pedir_si_no("Q3: ¿Es un concepto espiritual o religioso?")
    if r == "s":
        print("CONCEPTOS ESPIRITUALES: alma, fe, dios, karma, nirvana, reencarnación")
        return
    

def rama_seres_vivos():
    """Rama para seres vivos"""
    print("\n--- CATEGORÍA: SERES VIVOS ---")
    
    r = pedir_si_no("Q3: ¿Es un animal?")
    if r == "s":
        animales()
        return
    
    r = pedir_si_no("Q3: ¿Es una planta?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Tiene flores?")
        if r == "s":
            print("PLANTAS CON FLORES: rosas, girasoles, orquídeas, árboles frutales")
        else:
            print("PLANTAS SIN FLORES: helechos, musgos, coníferas, algas")
        return
    
    r = pedir_si_no("Q3: ¿Es un hongo?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es comestible?")
        if r == "s":
            print("HONGOS COMESTIBLES: champiñones, setas, levaduras")
        else:
            print("HONGOS NO COMESTIBLES: mohos, hongos venenosos, parásitos")
        return
    
    r = pedir_si_no("Q3: ¿Es un microorganismo?")
    if r == "s":
        print("MICROORGANISMOS: bacterias, virus, protozoos, amebas")
        return
    
    print("SER VIVO NO CLASIFICADO")

def rama_lugares():
    """Rama para lugares y construcciones"""
    print("\n--- CATEGORÍA: LUGARES/CONSTRUCCIONES ---")
    
    r = pedir_si_no("Q3: ¿Es un lugar natural?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Contiene agua?")
        if r == "s":
            print("LUGARES NATURALES ACUÁTICOS: ríos, lagos, océanos, playas, cascadas")
        else:
            print("LUGARES NATURALES TERRESTRES: montañas, desiertos, bosques, valles, cavernas")
        return
    
    r = pedir_si_no("Q3: ¿Es una construcción humana?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es para habitar?")
        if r == "s":
            print("CONSTRUCCIONES HABITACIONALES: casas, edificios, apartamentos, chozas")
        else:
            r = pedir_si_no("Q5: ¿Es para transporte?")
            if r == "s":
                print("INFRAESTRUCTURA DE TRANSPORTE: puentes, carreteras, aeropuertos, estaciones")
            else:
                print("CONSTRUCCIONES PÚBLICAS: hospitales, escuelas, museos, templos")
        return
    
    r = pedir_si_no("Q3: ¿Es una división geopolítica?")
    if r == "s":
        print("DIVISIONES GEOGRÁFICAS: países, ciudades, estados, pueblos, continentes")
        return
    
    print("LUGAR NO CLASIFICADO")

def rama_persona():
    """Rama para personas y personajes"""
    print("\n--- CATEGORÍA: PERSONAS/PERSONAJES ---")
    
    r = pedir_si_no("Q3: ¿Es una persona real?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es famosa o histórica?")
        if r == "s":
            print("PERSONAS FAMOSAS/HISTÓRICAS: científicos, artistas, líderes, deportistas")
        else:
            print("PERSONAS COMUNES: familiares, amigos, conocidos, personas anónimas")
        return
    
    r = pedir_si_no("Q3: ¿Es un personaje ficticio?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es de literatura?")
        if r == "s":
            print("PERSONAJES LITERARIOS: de novelas, cuentos, poesía, comics")
        else:
            print("PERSONAJES DE MEDIOS: de cine, TV, videojuegos, animación")
        return
    
    print("PERSONA/PERSONAJE NO CLASIFICADO")

def rama_fenomeno():
    
    
    r = pedir_si_no("Q3: ¿Es un FENÓMENO NATURAL observable?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es METEOROLÓGICO/ATMOSFÉRICO?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con la PRECIPITACIÓN?")
            if r == "s":
                print("METEOROLÓGICOS · PRECIPITACIÓN: lluvia, nieve, granizo, aguanieve, rocío")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con el VIENTO?")
            if r == "s":
                print("METEOROLÓGICOS · VIENTO: brisa, ventisca, huracán, tornado, tifón, ciclón")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con FENÓMENOS ELÉCTRICOS?")
            if r == "s":
                print("METEOROLÓGICOS · ELÉCTRICOS: rayo, relámpago, trueno, tormenta eléctrica")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con TEMPERATURA?")
            if r == "s":
                print("METEOROLÓGICOS · TÉRMICOS: calor, frío, ola de calor, helada, punto de rocío")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con EFECTOS ÓPTICOS?")
            if r == "s":
                print("METEOROLÓGICOS · ÓPTICOS: arcoíris, halo, espejismo, parhelio, corona solar")
                return
            print("METEOROLÓGICOS · PRESIÓN: alta presión, baja presión, frente climático")
            return
        
        r = pedir_si_no("Q4: ¿Es GEOLÓGICO/TERRESTRE?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con SISMOS o movimiento terrestre?")
            if r == "s":
                print("GEOLÓGICOS · SÍSMICOS: terremoto, temblor, tsunami, maremoto")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con VOLCANES?")
            if r == "s":
                print("GEOLÓGICOS · VOLCÁNICOS: erupción, lava, ceniza, fumarola, magma")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con EROSIÓN/DERRUMBES?")
            if r == "s":
                print("GEOLÓGICOS · EROSIÓN: deslizamiento, avalancha, derrumbe, alud")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con FORMACIÓN del relieve?")
            if r == "s":
                print("GEOLÓGICOS · FORMACIÓN: montañas, valles, cañones, placas tectónicas")
                return
            print("GEOLÓGICOS · SUBSUELO: magma, mineralización, géiser, termal")
            return
        
        r = pedir_si_no("Q4: ¿Es HIDROLÓGICO/ACUÁTICO?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con MAREAS?")
            if r == "s":
                print("HIDROLÓGICOS · MAREAS: marea alta, marea baja, maremoto")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con CORRIENTES?")
            if r == "s":
                print("HIDROLÓGICOS · CORRIENTES: corriente marina, corriente fluvial, remolino")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con OLAS/MAR?")
            if r == "s":
                print("HIDROLÓGICOS · OLAS: olas, tsunami, marejada, resaca")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con el CICLO DEL AGUA?")
            if r == "s":
                print("HIDROLÓGICOS · CICLO DEL AGUA: evaporación, condensación, precipitación, escorrentía")
                return
            print("HIDROLÓGICOS · ESTADOS/EVENTOS: congelación, deshielo, inundación, sequía")
            return
        
        r = pedir_si_no("Q4: ¿Es ASTRONÓMICO/ESPACIAL?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Se refiere al ESPACIO/medio?")
            if r == "s":
                print("ASTRONÓMICOS · ESPACIO: vacío cósmico, medio interestelar, gravedad cero")
                return
            r = pedir_si_no("Q5: ¿Se refiere a CUERPOS/EVENTOS orbitales?")
            if r == "s":
                print("ASTRONÓMICOS · CUERPOS: eclipse, conjunción, oposición, tránsito")
                return
            r = pedir_si_no("Q5: ¿Es un EVENTO astrofísico?")
            if r == "s":
                print("ASTRONÓMICOS · EVENTOS: supernova, agujero negro, nebulosa, galaxia")
                return
            r = pedir_si_no("Q5: ¿Es un FENÓMENO LUMINOSO?")
            if r == "s":
                print("ASTRONÓMICOS · LUMINOSOS: aurora boreal, luz zodiacal, lluvia de estrellas")
                return
            print("ASTRONÓMICOS · ORBITALES: rotación, traslación, perihelio, afelio")
            return
        
        r = pedir_si_no("Q4: ¿Es BIOLÓGICO/ECOLÓGICO?")
        if r == "s":
            
            r = pedir_si_no("Q5: ¿Está relacionado con CICLOS biológicos?")
            if r == "s":
                print("BIOLÓGICOS · CICLOS: fotosíntesis, respiración, descomposición")
                return
            r = pedir_si_no("Q5: ¿Está relacionado con COMPORTAMIENTOS?")
            if r == "s":
                print("BIOLÓGICOS · COMPORTAMIENTO: migración, hibernación, estivación, eclosión")
                return
            r = pedir_si_no("Q5: ¿Es un FENÓMENO ECOLÓGICO?")
            if r == "s":
                print("BIOLÓGICOS · ECOLÓGICOS: sucesión, simbiosis, depredación, competencia")
                return
            print("BIOLÓGICOS · BIOLUMINISCENCIA: luz natural en seres vivos")
            return
        
        print("FENÓMENO NATURAL NO ESPECIFICADO")
        return
    
   
    r = pedir_si_no("Q3: ¿Es una FORMA DE ENERGÍA?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es TÉRMICA?")
        if r == "s":
            print("ENERGÍA · TÉRMICA: calor, temperatura, conducción, convección, radiación")
            return
        r = pedir_si_no("Q4: ¿Es ELÉCTRICA?")
        if r == "s":
            print("ENERGÍA · ELÉCTRICA: electricidad, corriente, voltaje, resistencia, circuito")
            return
        r = pedir_si_no("Q4: ¿Es MAGNÉTICA?")
        if r == "s":
            print("ENERGÍA · MAGNÉTICA: magnetismo, campo magnético, electromagnetismo")
            return
        r = pedir_si_no("Q4: ¿Es LUMINOSA/RADIANTE?")
        if r == "s":
            print("ENERGÍA · LUMINOSA/RADIANTE: luz, fotones, espectro electromagnético, radiación")
            return
        r = pedir_si_no("Q4: ¿Es SONORA?")
        if r == "s":
            print("ENERGÍA · SONORA: sonido, onda sonora, eco, resonancia, ultrasonido")
            return
        r = pedir_si_no("Q4: ¿Es MECÁNICA?")
        if r == "s":
            print("ENERGÍA · MECÁNICA: movimiento, fuerza, trabajo, potencia, cinética, potencial")
            return
        r = pedir_si_no("Q4: ¿Es QUÍMICA?")
        if r == "s":
            print("ENERGÍA · QUÍMICA: reacción química, combustión, oxidación, fermentación")
            return
        r = pedir_si_no("Q4: ¿Es NUCLEAR?")
        if r == "s":
            print("ENERGÍA · NUCLEAR: fisión, fusión, radiactividad, desintegración")
            return
        print("ENERGÍA · CONCEPTOS COSMOLÓGICOS: energía oscura, materia oscura")
        return
    
    # TERCER NIVEL: FENÓMENOS FÍSICOS FUNDAMENTALES
    r = pedir_si_no("Q3: ¿Es un FENÓMENO FÍSICO fundamental?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Está relacionado con la ESTRUCTURA ATÓMICA?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Con ÁTOMOS?")
            if r == "s":
                print("FÍSICOS · ÁTOMOS: protones, neutrones, electrones")
                return
            r = pedir_si_no("Q5: ¿Con PARTÍCULAS subatómicas?")
            if r == "s":
                print("FÍSICOS · PARTÍCULAS: quark, leptón, bosón, hadrón")
                return
            r = pedir_si_no("Q5: ¿Con ESTADOS exóticos?")
            if r == "s":
                print("FÍSICOS · ESTADOS: plasma, condensado Bose-Einstein")
                return
            print("FÍSICOS · INTERACCIONES: fuerza nuclear fuerte/débil")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con los ESTADOS DE LA MATERIA?")
        if r == "s":
            r = pedir_si_no("Q5: ¿SÓLIDO?")
            if r == "s":
                print("FÍSICOS · SÓLIDO: cristalino, amorfo, polímero")
                return
            r = pedir_si_no("Q5: ¿LÍQUIDO?")
            if r == "s":
                print("FÍSICOS · LÍQUIDO: viscoso, fluido, superfluido")
                return
            r = pedir_si_no("Q5: ¿GASEOSO?")
            if r == "s":
                print("FÍSICOS · GASEOSO: comprimido, ideal, real")
                return
            print("FÍSICOS · PLASMA: ionizado, conductor")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con las FUERZAS FUNDAMENTALES?")
        if r == "s":
            r = pedir_si_no("Q5: ¿GRAVEDAD?")
            if r == "s":
                print("FÍSICOS · GRAVEDAD: atracción, curvatura del espaciotiempo")
                return
            r = pedir_si_no("Q5: ¿ELECTROMAGNETISMO?")
            if r == "s":
                print("FÍSICOS · ELECTROMAGNETISMO: campo EM, luz, electricidad, magnetismo")
                return
            r = pedir_si_no("Q5: ¿NUCLEAR FUERTE?")
            if r == "s":
                print("FÍSICOS · NUCLEAR FUERTE: núcleos atómicos, hadrones")
                return
            print("FÍSICOS · NUCLEAR DÉBIL: desintegración radiactiva")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con FENÓMENOS CUÁNTICOS?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Dualidad ONDA-PARTÍCULA?")
            if r == "s":
                print("CUÁNTICOS · DUALIDAD: onda-partícula")
                return
            r = pedir_si_no("Q5: ¿Principios (incertidumbre/exclusión)?")
            if r == "s":
                print("CUÁNTICOS · PRINCIPIOS: incertidumbre, exclusión")
                return
            r = pedir_si_no("Q5: ¿ENTRELAZAMIENTO?")
            if r == "s":
                print("CUÁNTICOS · ENTRELAZAMIENTO: no-localidad")
                return
            print("CUÁNTICOS · TÚNELES: efecto túnel cuántico")
            return
        
        print("FENÓMENO FÍSICO FUNDAMENTAL NO ESPECIFICADO")
        return
    
    # CUARTO NIVEL: FENÓMENOS QUÍMICOS
    r = pedir_si_no("Q3: ¿Es un FENÓMENO QUÍMICO?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es una REACCIÓN?")
        if r == "s":
            print("QUÍMICOS · REACCIONES: síntesis, descomposición, sustitución, combustión")
            return
        r = pedir_si_no("Q4: ¿Es un EQUILIBRIO/INTERACCIÓN?")
        if r == "s":
            print("QUÍMICOS · EQUILIBRIOS: químico, ácido-base, redox, solubilidad")
            return
        r = pedir_si_no("Q4: ¿Tiene que ver con ESTADOS dispersos?")
        if r == "s":
            print("QUÍMICOS · ESTADOS: coloide, suspensión, emulsión, solución")
            return
        print("QUÍMICOS · PROPIEDADES: pH, conductividad, reactividad, catálisis")
        return
    
    # QUINTO NIVEL: FENÓMENOS HUMANOS/SOCIALES (opcional)
    r = pedir_si_no("Q3: ¿Es un FENÓMENO SOCIAL o HUMANO?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Se refiere a GLOBALIZACIÓN?")
        if r == "s":
            print("SOCIALES · GLOBALIZACIÓN: económica, cultural, tecnológica")
            return
        r = pedir_si_no("Q4: ¿Se refiere a MIGRACIÓN?")
        if r == "s":
            print("SOCIALES · MIGRACIÓN: humana, animal, patrones")
            return
        r = pedir_si_no("Q4: ¿Se refiere a TENDENCIAS?")
        if r == "s":
            print("SOCIALES · TENDENCIAS: moda, pensamiento, comportamiento colectivo")
            return
        print("SOCIALES · REVOLUCIONES: industrial, tecnológica, social")
        return
    
    print("FENÓMENO/ENERGÍA NO CLASIFICADO")


def rama_objeto():
    """Rama para objetos inanimados"""
    print("\n--- CATEGORÍA: OBJETOS INANIMADOS ---")
    
    r = pedir_si_no("Q3: ¿Es NATURAL (no fabricado)?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es MINERAL?")
        if r == "s":
            print("OBJETOS MINERALES: rocas, cristales, gemas, metales, minerales")
        else:
            r = pedir_si_no("Q4: ¿Es de origen VEGETAL?")
            if r == "s":
                print("OBJETOS VEGETALES: madera, frutas, semillas, flores, hojas")
            else:
                print("OBJETOS ANIMALES: huesos, conchas, cuernos, pieles, plumas")
        return
    
    r = pedir_si_no("Q3: ¿Es ARTIFICIAL (fabricado)?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es HERRAMIENTA o UTENSILIO?")
        if r == "s":
            print("HERRAMIENTAS: martillo, destornillador, cuchillo, llave, pinza")
        else:
            r = pedir_si_no("Q4: ¿Es DISPOSITIVO ELECTRÓNICO?")
            if r == "s":
                print("ELECTRÓNICOS: teléfono, computadora, televisor, radio, tablet")
            else:
                r = pedir_si_no("Q4: ¿Es MUEBLE?")
                if r == "s":
                    print("MUEBLES: silla, mesa, cama, armario, estante")
                else:
                    r = pedir_si_no("Q4: ¿Es VEHÍCULO?")
                    if r == "s":
                        print("VEHÍCULOS: auto, bicicleta, avión, barco, tren")
                    else:
                        print("OBJETOS ARTIFICIALES: ropa, juguetes, libros, instrumentos")
        return
    
    print("OBJETO NO CLASIFICADO")

#------------------------------------------- SUB-RAMAS PRINCIPALES ------------------------------------------#
def animales():
    """Sub-rama para animales"""
    print("\n--- SUBCATEGORÍA: ANIMALES ---")
    
    r = pedir_si_no("Q4: ¿Es DOMÉSTICO?")
    if r == "s":
        r = pedir_si_no("Q5: ¿Es MAMÍFERO?")
        if r == "s":
            r = pedir_si_no("Q6: ¿Es PEQUEÑO?")
            if r == "s":
                r = pedir_si_no("Q7: ¿Hace CHILLIDOS?")
                if r == "s":
                    print("ROEDORES DOMÉSTICOS: hámster, ratón, gerbo, cobaya")
                else:
                    print("MAMÍFEROS PEQUEÑOS: conejo, hurón, erizo")
            else:
                r = pedir_si_no("Q6: ¿LADRA o MAÚLLA?")
                if r == "s":
                    print("MASCOTAS COMUNES: perro, gato")
                else:
                    r = pedir_si_no("Q7: ¿Es de GRANJA?")
                    if r == "s":
                        r = pedir_si_no("Q8: ¿Produce LANA?")
                        if r == "s":
                            print("ANIMALES DE LANAR: oveja, alpaca, llama")
                        else:
                            print("ANIMALES LECHEROS: vaca, cabra, búfala")
                    else:
                        r = pedir_si_no("Q7: ¿RELINCHA?")
                        if r == "s":
                            print("EQUINOS: caballo, pony, burro, mula")
                        else:
                            print("ANIMALES DE CORRAL: cerdo, pavo, gallina")
            return
        
        r = pedir_si_no("Q5: ¿Es AVE?")
        if r == "s":
            r = pedir_si_no("Q6: ¿CANTA?")
            if r == "s":
                print("AVES CANORAS: canario, periquito, jilguero, diamante")
            else:
                print("AVES DE CORRAL: gallina, pato, ganso, pavo")
            return
        
        r = pedir_si_no("Q5: ¿Es ACUÁTICO?")
        if r == "s":
            print("ANIMALES ACUÁTICOS DOMÉSTICOS: peces, tortugas acuáticas")
            return
        
        r = pedir_si_no("Q5: ¿Es REPTIL/ANFIBIO?")
        if r == "s":
            print("REPTILES/ANFIBIOS DOMÉSTICOS: tortugas, iguanas, ranas, salamandras")
            return
        
        print("ANIMAL DOMÉSTICO NO ESPECIFICADO")
        return
    
    else:
        # Animales salvajes
        r = pedir_si_no("Q4: ¿Es MAMÍFERO?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Es CARNÍVORO?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Es GRANDE?")
                if r == "s":
                    print("GRANDES DEPREDADORES: león, tigre, oso, lobo, pantera")
                else:
                    print("PEQUEÑOS DEPREDADORS: zorro, lince, hurón, comadreja")
            else:
                r = pedir_si_no("Q5: ¿Es HERBÍVORO?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Es MUY GRANDE?")
                    if r == "s":
                        print("GRANDES HERBÍVOROS: elefante, jirafa, rinoceronte, hipopótamo")
                    else:
                        print("HERBÍVOROS MEDIANOS: ciervo, cebra, antílope, caballo salvaje")
                else:
                    print("OMNÍVOROS: oso, mapache, cerdo salvaje, mono")
            return
        
        r = pedir_si_no("Q4: ¿Es AVE?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Es RAPAZ?")
            if r == "s":
                print("AVES RAPACES: águila, halcón, búho, buitre, cernícalo")
            else:
                r = pedir_si_no("Q5: ¿Es ACUÁTICA?")
                if r == "s":
                    print("AVES ACUÁTICAS: pato, cisne, gaviota, pelícano, pingüino")
                else:
                    print("AVES TERRESTRES: paloma, gorrión, cuervo, colibrí, gallina salvaje")
            return
        
        r = pedir_si_no("Q4: ¿Es REPTIL?")
        if r == "s":
            print("REPTILES: serpientes, lagartos, cocodrilos, tortugas, tuátaras")
            return
        
        r = pedir_si_no("Q4: ¿Es PEZ?")
        if r == "s":
            print("PECES: tiburón, atún, salmón, pez payaso, anguila")
            return
        
        r = pedir_si_no("Q4: ¿Es INSECTO/ARÁCNIDO?")
        if r == "s":
            print("ARTRÓPODOS: mariposa, abeja, araña, escorpión, cangrejo")
            return
        
        print("ANIMAL SALVAJE NO ESPECIFICADO")

def main():
    print("Piensa en lo que sea y lo adivinaré en (hasta) 20 preguntas.\nResponde solo 's' o 'n'.\n")

    # ESTRUCTURA CORREGIDA - Primera pregunta mejorada
    r = pedir_si_no("Q1: ¿Es algo FÍSICO que puedes percibir con los sentidos?")
    
    if r == "s":
        # Es físico - ahora preguntamos qué tipo de cosa física
        r = pedir_si_no("Q2: ¿Es un SER VIVO?")
        if r == "s":
            rama_seres_vivos()
            return
            
        r = pedir_si_no("Q2: ¿Es un LUGAR o CONSTRUCCIÓN?")
        if r == "s":
            rama_lugares()
            return
            
        r = pedir_si_no("Q2: ¿Es una PERSONA o PERSONAJE?")
        if r == "s":
            rama_persona()
            return

        r = pedir_si_no("Q2: ¿Es un FENÓMENO FÍSICO observable?")
        if r == "s":
            rama_fenomeno()
            return
            
        r = pedir_si_no("Q2: ¿Es un OBJETO INANIMADO?")
        if r == "s":
            rama_objeto()
            return
            
        print("No se pudo clasificar el concepto físico")
        
    else:
        # No es físico - debe ser abstracto o concepto intangible
        r = pedir_si_no("Q2: ¿Es un CONCEPTO ABSTRACTO o INTANGIBLE?")
        if r == "s":
            rama_abstracto()
            return
            
        print("No se pudo clasificar el concepto no físico")

if __name__ == "__main__":
    main()