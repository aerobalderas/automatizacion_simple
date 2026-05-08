from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion

def test_chatbot():
    print("--- Iniciando Chatbot 0.1.0 ---")

    print("\n[Prueba] Precio de acción de Microsoft")
    msft_price = obtener_precio_accion(None, "Microsoft")
    print(f"Resultado: {msft_price}")

    