
# IoT Sensor Data Application
![Slide4](https://github.com/CCO-HomeSentinel/iot-simulator/assets/70069239/9ae598a2-36b0-4673-bae2-eff4340c211d)

## Installation

```bash
  pip install -r requirements.txt
```
```bash
  mysql -h <host> -P <port> -u <user> -p < data/migrations/20240517_130400__script.sql  
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

`MYSQL_HOST`

`MYSQL_PORT`

`MYSQL_DATABASE`

`MYSQL_USERNAME`

`MYSQL_PASSWORD`


`API_GATEWAY_HOST`

`API_GATEWAY_STAGE`

`API_GATEWAY_S3_BUCKET`


`USE_IOT_HUB`

`IOT_HUB_CONNECTION_STRING`


`OPEN_WEATHER_ACTIVE`

`OPEN_WEATHER_API_URL`

`OPEN_WEATHER_API_KEY`

`OPEN_WEATHER_CIDADE`

`OPEN_WEATHER_INTERVALO`


`SKIP_INTRO`

`MENU_SIMULADOR`

`MENU_ANALISE`


`INTERVALO_SIMULADOR`

`INTERVALO_ENVIO`


`SENSOR_FUMACA`

`SENSOR_GAS`

`SENSOR_INUNDACAO`

`SENSOR_LUMINOSIDADE`

`SENSOR_MOVIMENTO`

`SENSOR_SOM`

`SENSOR_TEMPERATURA`


`INTERVALO_BACKUP_LOGGER`

`INTERVALO_TENTATIVA_ENVIO_JSON`

`ENABLE_LOGS`



## Authors

- [@IgorRegali](https://www.github.com/IgorRegali)
- [@KauanCavazani](https://www.github.com/KauanCavazani)
- [@kelvinsync](https://www.github.com/kelvinsync)
- [@leovasc5](https://www.github.com/leovasc5)
- [@ViniScardoso](https://www.github.com/ViniScardoso)



Adicione etiquetas de algum lugar, como: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![MIT License](https://img.shields.io/badge/language-python-blue.svg)](https://choosealicense.com/licenses/mit/)

[![MIT License](https://img.shields.io/badge/database-mysql-yellow.svg)](https://choosealicense.com/licenses/mit/)

[![MIT License](https://img.shields.io/badge/cloud-aws-black.svg)](https://choosealicense.com/licenses/mit/)

[![MIT License](https://img.shields.io/badge/cloud-azure-black.svg)](https://choosealicense.com/licenses/mit/)
