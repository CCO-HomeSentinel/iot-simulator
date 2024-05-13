import requests
import dotenv
import os
from .file import transformar_dict_em_json_file, destruir_arquivo

dotenv.load_dotenv()

API_GATEWAY_HOST = os.getenv('API_GATEWAY_HOST')
API_GATEWAY_STAGE = os.getenv('API_GATEWAY_STAGE')
API_GATEWAY_S3_BUCKET = os.getenv('API_GATEWAY_S3_BUCKET')

OPEN_WEATHER_API_URL = os.getenv('OPEN_WEATHER_API_URL')
OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
OPEN_WEATHER_CIDADE = os.getenv('OPEN_WEATHER_CIDADE')

def enviar_json(json):
    filename, path = transformar_dict_em_json_file(json)
    url = f"https://{API_GATEWAY_HOST}/{API_GATEWAY_STAGE}/{API_GATEWAY_S3_BUCKET}/{filename}"

    with open(path, 'rb') as file:
        payload = file.read()

        response = requests.request(
            "PUT",
            url=url,
            data=payload
        )

    if response.status_code != 200:
        #TODO - Logar erro
        return False 

    else:
        destruir_arquivo(path)
        return True
    
def receber_clima(valor_anterior):
    url = f"{OPEN_WEATHER_API_URL}?q={OPEN_WEATHER_CIDADE}&appid={OPEN_WEATHER_API_KEY}&lang=pt_br"

    try:
        req = requests.get(url)
        req_dic = req.json()
        temperatura = req_dic['main']['temp']
    except:
        #TODO - Logar erro
        return valor_anterior

    return round(temperatura, 2)