import re
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima

def chatbot ():
    print("*** Chatbot v1.0.0 Iniciando")
    print("Hola, Esteban, puedo ayudarte a obtener precios de acciones y clima de cualquier ciudad del mundo.")
    print("¿Qué quieres saber hoy?")

    # Ciclo infinito para mantener activo el chatbot

    while True:
        try:
            user_input = input("-->").strip()
            if not user_input:
                continue

            # Validar una petición de saida
            if user_input.lower() in ["salir"]:
                print("¡Hasta luego!")
                break

            # Reglas para detectar intención de preguntas por acciones

            stock_match = re.search(r"(?:precio|stock|acción|accion)\s+(?:de|la|de las\s+)(\w+)", user_input, re.IGNORECASE)

            # Reglas para detectar intención de preguntas por clima
            weather_match = re.search(r"(?:clima|tiempo|temperatura)\s+(?:en|de)\s+(\w+)", user_input, re.IGNORECASE)

            # Caso 1: El usuario pregunta por acciones

            if stock_match:
                # Debemos esperar si el usuario indica alguna acción
                price = obtener_precio_accion(user_input)
                if price:
                    print(f">> El precio actual es: {price}")
                else:
                    print("Chatbot: No pude obtener el precio, ¿podrías indicar otra acción?")
                
            # Caso 2: el usuario pregunta por el clima
            elif weather_match:
                temp = obtener_clima(user_input)
                if temp:
                    print(f">> {temp}")
                else:
                    print("Chatbot: No pude obtener la temperatura, ¿podrísa intentar otra ciudad?")

            # Caso 3: El usuario no ejecuta alguna petición

            else:
                    print("Chatbot: No entendí tu petición, ¿podrías replantearla?")

        except KeyboardInterrupt:
            # Comando de salida Ctrl + C | Cmd + C
            print("\nChatbot: ¡Hasta luego! Fue un palcer ayudarte :)")

        except Exception as e:
            print(f"Chatbot: Ocurrió un error inesperado {e}")


if __name__ == "__main__":
    chatbot()