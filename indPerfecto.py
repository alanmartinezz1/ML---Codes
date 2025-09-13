import random

TAM_POBLACION = 100       # número de cromosomas
ARREGLO = 20       # número de genes
PROB_MUTACION = 0.10      # 10% por gen
VALOR = 9        # valor objetivo por gen

def generar_poblacion(tam, long):
    poblacion = []
    for i in range(tam):
        cromosoma = [random.randint(1, VALOR) for _ in range(long)]
        poblacion.append({"genes": cromosoma, "origin": i})
    return poblacion

def formar_parejas_estratificadas(poblacion, num_parejas):
    # Calcular fitness para cada individuo
    poblacion_con_fitness = []
    for ind in poblacion:
        fit = fitness(ind["genes"])
        poblacion_con_fitness.append((ind, fit))
    
    # Ordenar por fitness
    poblacion_con_fitness.sort(key=lambda x: x[1], reverse=True)
    
    # Crear grupos estratificados
    tam_elite = len(poblacion) // 5  # 20% elite
    tam_medio = len(poblacion) // 2  # 40% medio
    
    grupo_elite = [ind for ind, fit in poblacion_con_fitness[:tam_elite]]
    grupo_medio = [ind for ind, fit in poblacion_con_fitness[tam_elite:tam_elite + tam_medio]]
    grupo_bajo = [ind for ind, fit in poblacion_con_fitness[tam_elite + tam_medio:]]
    
    parejas = []
    parejas_formadas = 0
    
    # Estrategia de emparejamiento: Elite x Medio, Medio x Bajo, Medio x Medio
    while parejas_formadas < num_parejas:
        # 40% Elite x Medio
        if parejas_formadas < num_parejas * 0.4 and grupo_elite and grupo_medio:
            p1 = random.choice(grupo_elite)
            p2 = random.choice(grupo_medio)
            if p1["origin"] != p2["origin"]:
                parejas.append((p1, p2))
                parejas_formadas += 1
        
        # 35% Medio x Bajo
        elif parejas_formadas < num_parejas * 0.75 and grupo_medio and grupo_bajo:
            p1 = random.choice(grupo_medio)
            p2 = random.choice(grupo_bajo)
            if p1["origin"] != p2["origin"]:
                parejas.append((p1, p2))
                parejas_formadas += 1
        
        # 25% Medio x Medio (diversidad)
        elif grupo_medio and len(grupo_medio) > 1:
            padres_medio = random.sample(grupo_medio, 2)
            p1, p2 = padres_medio[0], padres_medio[1]
            if p1["origin"] != p2["origin"]:
                parejas.append((p1, p2))
                parejas_formadas += 1
        else:
            # Fallback: cualquier pareja válida
            todos = grupo_elite + grupo_medio + grupo_bajo
            if len(todos) >= 2:
                padres = random.sample(todos, 2)
                p1, p2 = padres[0], padres[1]
                if p1["origin"] != p2["origin"]:
                    parejas.append((p1, p2))
                    parejas_formadas += 1
            else:
                break
    
    return parejas

def crossover_mejorado(p1, p2):
    hijo1 = []
    hijo2 = []
    
    for i, (g1, g2) in enumerate(zip(p1["genes"], p2["genes"])):
        # Si ambos genes son 9, mantenerlos
        if g1 == VALOR and g2 == VALOR:
            hijo1.append(VALOR)
            hijo2.append(VALOR)
        # Si uno es 9, favorecerlo
        elif g1 == VALOR:
            hijo1.append(VALOR)
            hijo2.append(max(g2, random.randint(7, VALOR)))
        elif g2 == VALOR:
            hijo1.append(max(g1, random.randint(7, VALOR)))
            hijo2.append(VALOR)
        else:
            # Crossover normal con sesgo hacia valores altos
            prom = (g1 + g2) / 2
            if prom.is_integer():
                val = int(prom)
                hijo1.append(val)
                hijo2.append(val)
            else:
                abajo = int(prom)
                arriba = int(prom) + 1
                # Sesgo hacia valores más altos
                if arriba <= VALOR:
                    if random.random() < 0.7:  # 70% probabilidad de elegir el mayor
                        hijo1.append(arriba)
                        hijo2.append(abajo)
                    else:
                        hijo1.append(abajo)
                        hijo2.append(arriba)
                else:
                    hijo1.append(abajo)
                    hijo2.append(abajo)
    
    return hijo1, hijo2

def mutar_hibrida(cromosoma):
    """Mutación híbrida: genes con 9 mutan aleatoriamente, otros con sesgo hacia valores altos"""
    cromosoma_mutado = cromosoma[:]
    for i in range(len(cromosoma_mutado)):
        if random.random() < PROB_MUTACION:  # 10% probabilidad para todos los genes
            gen_actual = cromosoma_mutado[i]
            
            if gen_actual == VALOR:
                # Respeta restricción: genes con 9 mutan completamente aleatorio
                cromosoma_mutado[i] = random.randint(1, VALOR)
            else:
                # Optimiza: otros genes con sesgo hacia valores altos
                cromosoma_mutado[i] = random.choices(
                    population=list(range(1, VALOR + 1)),
                    weights=[1, 1, 1, 2, 2, 3, 4, 5, 6],
                    k=1
                )[0]
    
    return cromosoma_mutado

def es_objetivo(cromosoma):
    return all(g == VALOR for g in cromosoma)

def fitness(cromosoma):
    return sum(1 for g in cromosoma if g == VALOR)

def seleccion_torneo(poblacion, tam_torneo=3):
    """Selección por torneo para evitar elitismo directo"""
    seleccionados = []
    
    for _ in range(len(poblacion)):
        # Seleccionar candidatos aleatorios para el torneo
        candidatos = random.sample(poblacion, min(tam_torneo, len(poblacion)))
        # Elegir el mejor del torneo
        ganador = max(candidatos, key=lambda x: fitness(x["genes"]))
        seleccionados.append(ganador)
    
    return seleccionados

def evolucionar():
    poblacion = generar_poblacion(TAM_POBLACION, ARREGLO)
    generacion = 0
    num_parejas = TAM_POBLACION // 2
    
    # Estadísticas para monitoreo
    mejor_fitness_anterior = 0
    generaciones_sin_mejora = 0

    while True:
        print(f"\n=== Generación {generacion} ===")
        
        # Calcular estadísticas
        fitness_poblacion = [fitness(ind["genes"]) for ind in poblacion]
        mejor_fitness = max(fitness_poblacion)
        fitness_promedio = sum(fitness_poblacion) / len(fitness_poblacion)
        
        print(f"Mejor fitness: {mejor_fitness}/{ARREGLO}")
        print(f"Fitness promedio: {fitness_promedio:.2f}")
        
        # Mostrar algunos ejemplos
        poblacion_ordenada = sorted(poblacion, key=lambda x: fitness(x["genes"]), reverse=True)
        print("Top 3 cromosomas:")
        for i in range(min(3, len(poblacion_ordenada))):
            print(f"  {poblacion_ordenada[i]['genes']} (fitness: {fitness(poblacion_ordenada[i]['genes'])})")

        # Verificar si encontramos el objetivo
        for ind in poblacion:
            if es_objetivo(ind["genes"]):
                print(f"\n¡Cromosoma objetivo encontrado en generación {generacion}!")
                print(ind["genes"])
                return

        # Verificar estancamiento
        if mejor_fitness <= mejor_fitness_anterior:
            generaciones_sin_mejora += 1
        else:
            generaciones_sin_mejora = 0
            mejor_fitness_anterior = mejor_fitness

        # Formar parejas con estrategia estratificada
        parejas = formar_parejas_estratificadas(poblacion, num_parejas)
        
        # Generar descendencia
        hijos = []
        for p1, p2 in parejas:
            h1_genes, h2_genes = crossover_mejorado(p1, p2)
            h1 = {"genes": mutar_hibrida(h1_genes), "origin": p1["origin"]}
            h2 = {"genes": mutar_hibrida(h2_genes), "origin": p2["origin"]}
            hijos.extend([h1, h2])

        # Selección de supervivientes usando torneo (evita elitismo directo)
        poblacion_combinada = poblacion + hijos
        
        # Asegurar diversidad: mantener algunos individuos aleatorios
        poblacion_torneo = seleccion_torneo(poblacion_combinada, tam_torneo=3)
        
        # Tomar los mejores pero con algo de aleatoriedad
        poblacion = poblacion_torneo[:TAM_POBLACION]
        
        # Inyectar diversidad si hay estancamiento
        if generaciones_sin_mejora > 10:
            print("Inyectando diversidad...")
            num_nuevos = TAM_POBLACION // 10  # 10% de población nueva
            nuevos_individuos = generar_poblacion(num_nuevos, ARREGLO)
            poblacion = poblacion[:-num_nuevos] + nuevos_individuos
            generaciones_sin_mejora = 0
        
        generacion += 1

# Ejecutar el algoritmo
evolucionar()