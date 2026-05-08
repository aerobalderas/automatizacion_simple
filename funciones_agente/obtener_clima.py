import requests

def obtener_clima(user_imput):

    city = user_imput.lower().replace("clima", "").replace("temperatura", "").replace("en", "").replace("de", "").strip()

    try:

        response = requests.get(f"https://wttr.in/{city}?format=%t", timeout=10)

        if response.status_code == 200:
            return response.text.strip()
        
        else:
            return "No pude obtener el clima."

    except Exception as e:
        return f"Error de red, por favor revisa tu conexión {e}"

