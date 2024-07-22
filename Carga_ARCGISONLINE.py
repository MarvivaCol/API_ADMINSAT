import requests
import json

# Parámetros de autenticación de ArcGIS
username = 'gis.colombia_mv'
password = 'Marviva2022#1'

# Obtener token de autenticación de ArcGIS
def get_token(username, password):
    token_url = 'https://www.arcgis.com/sharing/rest/generateToken'
    params = {
        'f': 'json',
        'username': username,
        'password': password,
        'referer': 'https://www.arcgis.com'
    }
    response = requests.post(token_url, data=params)
    response_json = response.json()
    if 'token' in response_json:
        return response_json['token']
    else:
        print("Error al obtener el token:", response_json)
        exit()

token = get_token(username, password)
print(f"Token obtenido: {token}")

# ID del ítem existente
item_id = '71a9955bd81c410186b6914c408dafb9'

# URL del servicio de ArcGIS Online donde actualizarás los datos
update_url = f'https://www.arcgis.com/sharing/rest/content/users/{username}/items/{item_id}/update'

# Actualizar archivo GeoJSON en ArcGIS Online
files = {'file': open('ubicaciones.geojson', 'rb')}  # Reemplaza con la ruta a tu archivo GeoJSON local
params = {
    'f': 'json',
    'token': token
}
response = requests.post(update_url, files=files, data=params)
response_data = response.json()

# Verifica si la actualización fue exitosa
if 'success' in response_data and response_data['success']:
    print(f"Archivo actualizado exitosamente. ID del ítem: {item_id}")
else:
    print("Error al actualizar el archivo:", response_data)
    exit()
