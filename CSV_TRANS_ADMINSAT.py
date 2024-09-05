import geojson
import pandas as pd
import requests

# URL del archivo GeoJSON en tu repositorio de GitHub
url = 'https://raw.githubusercontent.com/MarvivaCol/API_ADMINSAT/main/ubicaciones.geojson'

# Descargar el archivo GeoJSON
response = requests.get(url)
geojson_data = geojson.loads(response.content)

# Extraer las características (features)
features = geojson_data['features']

# Crear listas para almacenar los datos
properties_list = []
coordinates_list = []

# Iterar sobre las características y extraer propiedades y coordenadas
for feature in features:
    properties_list.append(feature['properties'])
    coordinates_list.append(feature['geometry']['coordinates'])

# Crear un DataFrame de pandas con las propiedades
df = pd.DataFrame(properties_list)

# Agregar las coordenadas al DataFrame
df['coordinates'] = coordinates_list

# Guardar como archivo CSV
df.to_csv('ubicaciones_convertido.csv', index=False)

print("Conversión completada. El archivo CSV ha sido guardado.")
