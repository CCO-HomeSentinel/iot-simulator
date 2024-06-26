import requests
import dotenv
import os
import sys
from .file import transformar_dict_em_json_file, destruir_arquivo

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.logger import logger

dotenv.load_dotenv()

API_GATEWAY_HOST = os.getenv("API_GATEWAY_HOST")
API_GATEWAY_STAGE = os.getenv("API_GATEWAY_STAGE")
API_GATEWAY_S3_BUCKET = os.getenv("API_GATEWAY_S3_BUCKET")

OPEN_WEATHER_API_URL = os.getenv("OPEN_WEATHER_API_URL")
OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
OPEN_WEATHER_CIDADE = os.getenv("OPEN_WEATHER_CIDADE")

URL = f"{OPEN_WEATHER_API_URL}?q={OPEN_WEATHER_CIDADE}&appid={OPEN_WEATHER_API_KEY}&lang=pt_br"


def enviar_json(json):
    filename, path = transformar_dict_em_json_file(json)
    url = f"https://{API_GATEWAY_HOST}/{API_GATEWAY_STAGE}/{API_GATEWAY_S3_BUCKET}/{filename}"

    with open(path, "rb") as file:
        payload = file.read()

        response = requests.request("PUT", url=url, data=payload)

    destruir_arquivo(path)
    if response.status_code != 200:
        logger.log(
                "error", f"Erro ao se comunicar com o API GATEWAY: {{ status: {response.status_code}, content: {response.content} }}"
            )
        return False

    return True


def receber_clima(valor_anterior):
    response = requests.get(URL)

    if response.status_code != 200:
        logger.log(
            "error", f"Erro ao se comunicar com a api OPEN WEATHER: {{ status: {response.status_code}, content: {response.content} }}"
        )

        return valor_anterior

    req_dic = response.json()
    temperatura = req_dic["main"]["temp"]

    return round(temperatura, 2)
