from django.shortcuts import render

# Create your views here.

# polls/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import time

BOT_TOKEN = "8589119095:AAH9jfcUTOKxXJM2-zSy6_wf6Vexi23Igw4"

@csrf_exempt
def telegram_webhook(request):
    data = json.loads(request.body)

    chat_id = data["message"]["chat"]["id"]
    mensaje = data["message"]["text"]

    respuesta = procesar_mensaje(mensaje)

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": respuesta
        }
    )

    return JsonResponse({"ok": True})



from google import genai

def procesar_mensaje(mensaje):
#Usa gemini api para procesar el texto.
    client = genai.Client(api_key="AQ.Ab8RN6JeHg1wdHUKnfTvrlNIVo-6q8jo99DLLPYAmgYU2qBk6w")

    start = time.perf_counter()

    sys_info = "System info: Da la respuesta en español con una redacción corta o simple con un formato plano. La información tiene que ser acerca de duda de tramites de documentos de guanajuato de cualquier dependencia. "

    mensaje = sys_info + mensaje

    modelo = "gemini-3-flash-preview"
    #modelo = "gemini-2.5-flash"
    response = client.models.generate_content(
                model = modelo,
                contents=mensaje,
            )

    end = time.perf_counter()

    print(f"Execution time: {end - start} seconds")

    return response.text
