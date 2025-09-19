import json
import re
import random
from pathlib import Path
from typing import Dict, Optional, List
from difflib import get_close_matches

INTENTS_FILE = "intents.json"
correcciones_rapidas = {
    "zi": "sí",
    "si": "sí",
    "sip": "sí",
    "okey": "ok",
    "s": "sí",
    "sii": "sí",
    "n": "no",
    "nop": "no",
}

class HotelChatBot:
    def __init__(self):
        self.intents = []
        self.state: Optional[str] = None
        self.context: Dict = {}
        self.load_intents()
        self.lista_palabras = self.cargar_palabras_clave(self.intents)

    def load_intents(self):
        if not Path(INTENTS_FILE).exists():
            print(f"No encontré {INTENTS_FILE}")
            return
        raw = json.load(open(INTENTS_FILE, encoding="utf-8"))
        self.intents = raw.get("intents", [])

    def corregir_texto(self, texto: str, lista_palabras: List[str]) -> str:
        palabras = texto.split()
        palabras_corregidas = []

        for palabra in palabras:
            # Primero revisar el diccionario de correcciones rápidas
            if palabra.lower() in correcciones_rapidas:
                palabras_corregidas.append(correcciones_rapidas[palabra.lower()])
                continue

            # Luego aplicar get_close_matches
            match = get_close_matches(palabra.lower(), lista_palabras, n=1, cutoff=0.8)
            if match:
                palabras_corregidas.append(match[0])
            else:
                palabras_corregidas.append(palabra)
        
        return " ".join(palabras_corregidas)

    def cargar_palabras_clave(self, intents) -> List[str]:
        palabras = []
        for intent in intents:
            for pattern in intent.get("patterns", []):
                # Solo añadimos palabras "normales", no regex con []
                if not re.search(r"[\[\]\(\)\|]", pattern):
                    palabras.extend(pattern.lower().split())
        return list(set(palabras))

    # In the HotelChatBot class, modify the match_intent method:

    def match_intent(self, text: str) -> Optional[Dict]:
        matched_intents = []

        for intent in self.intents:
            for pattern in intent.get("patterns", []):
                if re.search(pattern, text, re.IGNORECASE):
                    matched_intents.append(intent)
                    break

        # Prioritize problem-related intents
        priority_tags = ["problema_habitacion", "emergencia_medica", "objetos_perdidos", "asistencia_general"]

        for tag in priority_tags:
            for intent in matched_intents:
                if intent["tag"] == tag:
                    return intent

        # Return the first match if no priority intent found
        return matched_intents[0] if matched_intents else None

    def es_negativa(self, texto: str) -> bool:
        """Detecta si el usuario quiere cancelar o negar algo"""
        negativas = [
            r'\b(no|nada|ya\s+no|no\s+quiero|no\s+deseo|cancelar|salir|mejor\s+no|ni\s+modo|d[eé]jalo|ol[vb]i[d]?a(lo)?|ol[vb]i[d]?a(lo)?|ol[vb]i[d]?alo)\b',
            r'^(nop|nel|nope)$'
        ]

        for pattern in negativas:
            if re.search(pattern, texto.lower()):
                return True
        return False

    def es_fecha_valida(self, texto: str) -> bool:
        """Valida si el texto contiene información de fechas válida"""
        # Patrones para detectar fechas
        patrones_fecha = [
            r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',       # 15/01/2024
            r'\d{1,2}\s+de\s+\w+',                  # 15 de enero
            r'(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)',
            r'(lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo)',
            r'(ma[ñn]ana|pasado\s+ma[ñn]ana|pr[oó]ximo|siguiente)',
            r'(hoy|ayer)',
            r'\d{1,2}\s*al\s*\d{1,2}',
            r'del\s+\d{1,2}\s+al\s+\d{1,2}',
        ]
  
        for patron in patrones_fecha:
            if re.search(patron, texto.lower()):
                return True
        return False

    def handle_special_states(self, user_input: str) -> bool:
        normalized_input = user_input.strip().lower()

        if self.state == "esperando_nombre":
            if self.es_negativa(user_input):
                print("Bot: Está bien, no es necesario que me digas tu nombre. ¿En qué más puedo ayudarte?")
                self.state = None
                return True
            
            name = user_input.strip().title()
            self.context["user_name"] = name
            print(f"Bot: ¡Mucho gusto, {name}!")
            self.state = None
            return True

        if self.state == "esperando_fechas":
            # Verificar si el usuario quiere cancelar
            if self.es_negativa(user_input):
                print("Bot: Entendido, cancelamos la consulta de disponibilidad. ¿Hay algo más en lo que pueda ayudarte?")
                self.state = None
                return True
            
            # Verificar si la respuesta contiene información de fechas
            if not self.es_fecha_valida(user_input):
                print("Bot: No reconozco esas fechas. Por favor, especifica fechas como:")
                print("- '15 de enero al 20 de enero'")
                print("- '15/01/2024 al 20/01/2024'")
                print("- 'próximo fin de semana'")
                print("- O escribe 'no' si prefieres cancelar")
                return True
            
            self.context["fechas_solicitadas"] = user_input
            print(f"Bot: Consultando disponibilidad para {user_input}...")
            print("\nBot: Disponibilidad encontrada:")
            print("Habitación Estándar: $1,200/noche")
            print("Habitación Superior: $1,800/noche")
            print("Suite Junior: $2,500/noche")
            print("Suite Presidencial: $4,000/noche")
            print("\nBot: ¿Te interesa alguna de estas opciones?")
            self.state = "esperando_seleccion_habitacion"
            return True

        if self.state == "esperando_seleccion_habitacion":
            if self.es_negativa(user_input):
                print("Bot: Entendido, no procederemos con la reserva. ¿Hay algo más en lo que pueda ayudarte?")
                self.state = None
                return True
            
            # Verificar si es una respuesta afirmativa general
            if re.search(r"(sí|si|ok|vale|claro|perfecto|genial|excelente)", normalized_input):
                print("Bot: ¡Perfecto! ¿Cuál tipo de habitación te interesa?")
                print("- Estándar ($1,200/noche)")
                print("- Superior ($1,800/noche)")
                print("- Suite Junior ($2,500/noche)")
                print("- Suite Presidencial ($4,000/noche)")
                return True
                
            if re.search(r"est[aá]ndar|b[aá]sica", normalized_input):
                self.context["habitacion"] = "Estándar"
                print("Bot: ¡Excelente elección! La estándar incluye cama queen, TV y WiFi.")
            elif re.search(r"superior", normalized_input):
                self.context["habitacion"] = "Superior"
                print("Bot: ¡Perfecta selección! La superior incluye cama king, minibar y balcón.")
            elif re.search(r"suite|junior", normalized_input):
                self.context["habitacion"] = "Suite Junior"
                print("Bot: ¡Magnífica opción! Incluye jacuzzi, sala y desayuno.")
            elif re.search(r"presidencial", normalized_input):
                self.context["habitacion"] = "Suite Presidencial"
                print("Bot: ¡La mejor opción! Incluye mayordomo, terraza privada y comidas incluidas.")
            else:
                print("Bot: No reconozco esa opción. Por favor especifica:")
                print("- 'estándar' o 'básica'")
                print("- 'superior'")
                print("- 'suite junior'")
                print("- 'presidencial'")
                print("- O 'no' para cancelar")
                return True

            print("\nBot: ¿Deseas proceder con la reserva? (sí/no)")
            self.state = "esperando_confirmacion_reserva"
            return True

        if self.state == "esperando_confirmacion_reserva":
            if re.search(r"(sí|si|claro|reservar|confirmar|adelante|proceder)", normalized_input):
                code = f"HTL{random.randint(1000,9999)}"
                print("\nBot: ¡Reserva confirmada!")
                print(f"Código: {code}")
                print(f"Habitación: {self.context.get('habitacion','N/A')}")
                print(f"Fechas: {self.context.get('fechas_solicitadas','N/A')}")
                self.context["reserva"] = code
            elif self.es_negativa(user_input):
                print("Bot: Entendido, no se realizó la reserva. ¿Hay algo más en lo que pueda ayudarte?")
            else:
                print("Bot: Por favor responde 'sí' para confirmar la reserva o 'no' para cancelar.")
                return True
            self.state = None
            return True

        if self.state == "esperando_numero_habitacion":
            if self.es_negativa(user_input):
                print("Bot: Entendido, cancelamos el reporte. ¿Hay algo más en lo que pueda ayudarte?")
                self.state = None
                return True
                
            num = re.search(r'\d+', normalized_input)
            if num:
                print(f"Bot: Reporte registrado para habitación {num.group()}.")
                print("Bot: Mantenimiento llegará en 15 minutos.")
            else:
                print("Bot: Proporciona un número de habitación válido (ejemplo: '105', 'habitación 205')")
                print("Bot: O escribe 'no' para cancelar")
                return True
            self.state = None
            return True


        if self.state == "cancel_reservacion":
            if self.es_negativa(user_input):
                print("Bot: Entendido. ¿Hay algo más en lo que pueda ayudarte?")
                self.state = None
                return True
                
            num = re.search(r'\d+', normalized_input)
            if num:
                print(f"Bot: Reservación cancelada.")
                print("Bot: Que tenga un buen día.")
            else:
                print("Bot: Proporciona un número de habitación válido (ejemplo: '105', 'habitación 205')")
                print("Bot: O escribe 'no' para cancelar")
                return True
            self.state = None
            return True

        if self.state == "emergency_room":
            if self.es_negativa(user_input):
                print("Bot: Entendido. ¿Hay algo más en lo que pueda ayudarte?")
                self.state = None
                return True
                
            num = re.search(r'\d+', normalized_input)
            if num:
                print(f"Bot: Servicios de emergencia en camino.")
            else:
                print("Bot: Proporciona un número de habitación válido (ejemplo: '105', 'habitación 205')")
                print("Bot: O escribe 'no' para cancelar")
                return True
            self.state = None
            return True

        if self.state == "esperando_objeto_perdido":
            if self.es_negativa(user_input):
                print("Bot: Entendido, cancelamos el reporte. ¿Hay algo más en lo que pueda ayudarte?")
                self.state = None
                return True
                
            self.context["objeto"] = user_input
            print(f"Bot: Registré tu reporte de objeto perdido: {user_input}")
            print("Bot: Nuestro personal revisará y te contactará. ¿Me das un teléfono de contacto?")
            self.state = "esperando_telefono_contacto"
            return True

        if self.state == "esperando_telefono_contacto":
            if self.es_negativa(user_input):
                print("Bot: Entendido. Registramos tu reporte pero no podremos contactarte.")
                self.state = None
                return True
                
            phone = re.search(r'[\d\-\(\)\+\s]+', normalized_input)
            if phone and len(re.sub(r'\D', '', phone.group())) >= 10:
                print("Bot: Solicitud registrada con éxito. Te llamaremos si encontramos tu objeto.")
                self.context["telefono"] = phone.group()
            else:
                print("Bot: Ingresa un número de teléfono válido (10 dígitos mínimo)")
                print("Bot: Ejemplo: '55-1234-5678' o escribe 'no' para omitir")
                return True
            self.state = None
            return True

        if self.state == "esperando_info_extra_spa":
            options = self.context.get("info_extra_options_spa", [])

            # Detectar salida
            if re.search(r"\b(salir|ya\s*no|terminar|cancelar)\b", normalized_input):
                print("Bot: Perfecto, salimos del menú de información extra.")
                self.state = None
                return True

            choice = None

            # 1. Revisar si el usuario respondió con un número
            num = re.search(r'\d+', normalized_input)
            if num:
                idx = int(num.group()) - 1
                if 0 <= idx < len(options):
                    choice = options[idx]

            # 2. Revisar si coincide con el texto de alguna opción (ignorando acentos)
            if not choice:
                def normalize(text):
                    text = text.lower()
                    text = re.sub(r'[áàäâ]', 'a', text)
                    text = re.sub(r'[éèëê]', 'e', text)
                    text = re.sub(r'[íìïî]', 'i', text)
                    text = re.sub(r'[óòöô]', 'o', text)
                    text = re.sub(r'[úùüû]', 'u', text)
                    text = re.sub(r'[ñ]', 'n', text)
                    return text

                user_norm = normalize(normalized_input)
                for opt in options:
                    if re.search(normalize(opt), user_norm):
                        choice = opt
                        break

            if choice:
                print(f"Bot: Claro, aquí tienes más información sobre '{choice}':")
                # Respuestas personalizadas
                if "horarios" in choice.lower():
                    print("- Horarios disponibles: Lunes a Domingo, 9:00 - 21:00")
                elif "parejas" in choice.lower():
                    print("- Paquete para parejas: masaje relajante + cena romántica, $2,500")
                elif "faciales" in choice.lower():
                    print("- Tratamientos faciales especializados: hidratante, anti-edad, purificante")
                elif "descuentos" in choice.lower():
                    print("- Descuento del 15% al reservar 3 sesiones o más")
                else:
                    print("- Información no disponible por el momento.")

                # Volver a mostrar menú
                print("\nBot: ¿Quieres saber de otra opción? (escribe el número, la palabra o 'salir' para terminar)")
                for i, opt in enumerate(options, 1):
                    print(f"   {i}. {opt}")
                return True

            else:
                print("Bot: No entendí tu elección. Responde con el número, la palabra de la opción o 'salir'.")
                return True



        if self.state == "esperando_info_extra":
            intent_nuevo = self.match_intent(user_input)
            if intent_nuevo and intent_nuevo["tag"] != "tipos_habitacion":
                #print("Bot: Perfecto, cambiando de tema...")
                self.state = None
                self.respond(user_input)  # Procesar la nueva intención
                return True
            options = self.context.get("info_extra_options", [])

            # Detectar salida
            if re.search(r"\b(salir|ya\s*no|terminar|cancelar)\b", normalized_input):
                print("Bot: Perfecto, salimos del menú de información extra.")
                self.state = None
                return True

            choice = None

            # 1. Revisar si el usuario respondió con un número
            num = re.search(r'\d+', normalized_input)
            if num:
                idx = int(num.group()) - 1
                if 0 <= idx < len(options):
                    choice = options[idx]

            # 2. Revisar si coincide con el texto de alguna opción
            if not choice:
                for opt in options:
                    if re.search(opt.lower(), normalized_input):
                        choice = opt
                        break

            if choice:
                print(f"Bot: Claro, aquí tienes más información sobre '{choice}':")
                # Respuestas personalizadas
                if "amenidades" in choice.lower():
                    print("- Todas las habitaciones incluyen WiFi, TV y aire acondicionado.")
                elif "fotos" in choice.lower():
                    print("- Puedes ver fotos en nuestra galería online: hotelparaiso.com/fotos")
                elif "servicios exclusivos" in choice.lower():
                    print("- Tenemos spa, gimnasio 24h y transportación al aeropuerto.")
                elif "paquetes familiares" in choice.lower():
                    print("- Paquete familiar: 2 adultos + 2 niños, con desayuno incluido.")
                else:
                    print("- Información no disponible por el momento.")

                # Volvemos a mostrar menú
                print("\nBot: ¿Quieres saber de otra opción? (escribe el número, la palabra o 'salir' para terminar)")
                for i, opt in enumerate(options, 1):
                    print(f"   {i}. {opt}")
                return True

            else:
                print("Bot: No entendí tu elección. Responde con el número, la palabra de la opción o 'salir'.")
                return True
        
        if self.state == "esperando_modificacion_reserva":
            if self.es_negativa(user_input):
                print("Bot: Entendido, no haremos cambios. ¿Necesitas algo más?")
                self.state = None
                return True

            # Lógica simple para simular cambios
            if "fechas" in user_input.lower():
                print("Bot: Para cambiar las fechas, necesitaría cancelarla y crear una nueva. ¿Procedemos?")
            elif "noche" in user_input.lower():
                print("Bot: ¡Claro! He añadido una noche extra a tu reserva. El nuevo total se ajustará.")
            else:
                print(f"Bot: Entendido. He dejado una nota en tu reserva '{self.context['reserva']}' sobre: '{user_input}'.")
            
            print("Bot: ¿Hay algo más que pueda hacer por ti?")
            self.state = None # Limpiamos el estado
            return True

        if self.state == "confirmar_cancelacion":
            if re.search(r"(sí|si|claro|cancelar|confirmar)", user_input.lower()):
                print(f"Bot: Tu reserva {self.context['reserva']} ha sido cancelada.")
                # Eliminamos la reserva del contexto
                del self.context['reserva']
            else:
                print("Bot: De acuerdo, tu reserva no ha sido cancelada.")
            
            self.state = None
            return True
        return False

    def handle_followup(self, followup_data: Dict):
        if not followup_data:
            return
        ftype = followup_data.get("type")
        if ftype == "ask_name":
            print("Bot: ¿Cómo te llamas? (o escribe 'no' si prefieres no decirme)")
            self.state = "esperando_nombre"
        elif ftype == "ask_dates":
            print("Bot: ¿Para qué fechas deseas consultar la disponibilidad?")
            print("Bot: (puedes escribir 'no' para cancelar)")
            self.state = "esperando_fechas"
        elif ftype == "ask_room_number":
            print("Bot: ¿Cuál es tu número de habitación?")
            self.state = "esperando_numero_habitacion"
        elif ftype == "ask_room_number_cancel":
            print("Bot: ¿Cuál es tu número de habitación?")
            self.state = "cancel_reservacion"
        elif ftype == "ask_room_emergency":
            print("Bot: ¿Cuál es tu número de habitación?")
            self.state = "emergency_room"
        elif ftype == "ask_lost_item":
            print("Bot: ¿Qué objeto perdiste?")
            self.state = "esperando_objeto_perdido"
        elif ftype == "offer_more_info_spa":
            options = followup_data.get("options", [])
            if options:
                print("Bot: ¿Quieres más información sobre:")
                for i, opt in enumerate(options, 1):
                    print(f"   {i}. {opt}")
                self.state = "esperando_info_extra_spa"
                self.context["info_extra_options_spa"] = options
        elif ftype == "offer_more_info":
            options = followup_data.get("options", [])
            if options:
                print("Bot: ¿Quieres más información sobre:")
                for i, opt in enumerate(options, 1):
                    print(f"   {i}. {opt}")
                self.state = "esperando_info_extra"
                self.context["info_extra_options"] = options

    def respond(self, user_input: str):
        # Corrección de texto antes de procesar
        user_input = self.corregir_texto(user_input, self.lista_palabras)

        if self.handle_special_states(user_input):
            return

        intent = self.match_intent(user_input)

        # Interceptamos intents específicos si ya hay una reserva en el contexto
        if intent and "reserva" in self.context:
            tag = intent.get("tag")
            
            if tag == "gestion_reserva":
                codigo_reserva = self.context["reserva"]
                print(f"Bot: Veo que tienes una reserva activa con el código: {codigo_reserva}.")
                print("Bot: ¿Qué te gustaría hacer? (ej: cambiar fechas, añadir una noche)")
                self.state = "esperando_modificacion_reserva"
                return

            if tag == "politica_cancelacion":
                codigo_reserva = self.context["reserva"]
                print(f"Bot: ¿Deseas cancelar tu reserva con el código {codigo_reserva}?")
                print("Bot: Recuerda la política: cancelación gratuita hasta 48 horas antes.")
                self.state = "confirmar_cancelacion"
                return

        if intent:
            resp = random.choice(intent.get("responses", []))
            print(f"Bot: {resp}")
            if "followup" in intent:
                self.handle_followup(intent["followup"])
        else:
            print("Bot: No entendí tu solicitud. ¿Podrías reformularla?")

    def run(self):
        print("Bot: ¡Bienvenido al Hotel Paraíso!")

        while True:
            user = input("Tú: ").strip()
            if not user:
                continue
            if user.lower() in ["adiós","bye","gracias","eso es todo","salir","hasta luego","exit","quit"]:
                print("Bot: ¡Gracias por tu tiempo! Hasta pronto.")
                break
            self.respond(user)

if __name__ == "__main__":
    bot = HotelChatBot()
    bot.run()