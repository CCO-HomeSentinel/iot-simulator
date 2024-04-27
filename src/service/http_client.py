import requests
import dotenv
import os
from .file import transformar_dict_em_json_file, destruir_arquivo

dotenv.load_dotenv()

def enviar_json(json):
    filename, path = transformar_dict_em_json_file(json)
    url = f"https://{os.getenv('API_GATEWAY_HOST')}/{os.getenv('API_GATEWAY_STAGE')}/{os.getenv('API_GATEWAY_S3_BUCKET')}/{filename}"

    with open(path, 'rb') as file:
        payload = file.read()

        response = requests.request(
            "PUT",
            url=url,
            data=payload
        )

    if response.status_code != 200:
        print(response.text) 

        exit()
    else:
        destruir_arquivo(path)
        return True