import requests
import pandas as pd

#mi key personal
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjYXJtZW4uZmVybmFuZGV6LnByb0BnbWFpbC5jb20iLCJqdGkiOiI2YTJhYTY0Zi00NDg0LTRhZjEtYjkxMi1kZmMwM2YwMjNmM2QiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTc1MjUwMzA1MSwidXNlcklkIjoiNmEyYWE2NGYtNDQ4NC00YWYxLWI5MTItZGZjMDNmMDIzZjNkIiwicm9sZSI6IiJ9.3OYTda2_9xW4gr9E1WHnoHTOdVaOp3ePHeeA-IONiUU'


#definición de la función genérica
def get_aemet_data(id_estacion, start_date, end_date):
    base_url = (
        f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/"
        f"fechaini/{start_date}T00%3A00%3A00UTC/fechafin/{end_date}T23%3A59%3A59UTC/estacion/{id_estacion}"
    )
    params = {'api_key': API_KEY}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        url_datos = response.json()['datos']
        data_response = requests.get(url_datos)
        if data_response.status_code == 200:
            df = pd.read_json(data_response.content)
            return df
        else:
        print(f"Error en datos: status code {data_response.status_code}")
    else:
    print(f"Error en petición inicial: status code {response.status_code}")
       
    return None

#Petición a un año de la estación de Sevilla
df = get_aemet_data('5786I', '2022-01-01', '2022-12-31')
if df is not None:
    df.to_csv('data/raw/andalucia/sevilla_2022.csv', index=False)
