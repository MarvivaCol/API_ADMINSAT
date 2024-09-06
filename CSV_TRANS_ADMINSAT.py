import geojson
import pandas as pd
import os
from git import Repo

# Ruta del archivo GeoJSON y del archivo CSV
archivo_geojson = "ubicaciones.geojson"
archivo_csv = "ubicaciones_convertido.csv"

# Verificar si el archivo GeoJSON existe
if os.path.exists(archivo_geojson):
    # Leer el archivo GeoJSON
    with open(archivo_geojson, "r") as archivo:
        geojson_data = geojson.load(archivo)
    
    # Lista para almacenar las propiedades
    propiedades_list = []
    
    # Iterar sobre las características del GeoJSON y extraer las propiedades
    for feature in geojson_data["features"]:
        propiedades = feature["properties"]
        # Agregar las coordenadas de latitud y longitud
        coordenadas = feature["geometry"]["coordinates"]
        propiedades["longitud"] = coordenadas[0]
        propiedades["latitud"] = coordenadas[1]
        propiedades_list.append(propiedades)
    
    # Crear un DataFrame de pandas con las propiedades
    df = pd.DataFrame(propiedades_list)
    
    # Guardar los datos en un archivo CSV
    df.to_csv(archivo_csv, index=False)
    
    print(f"Archivo CSV '{archivo_csv}' creado correctamente.")
    
    # Ruta del directorio del repositorio
    repo_dir = os.path.abspath(os.path.dirname(__file__))  # Directorio donde está este script
    repo = Repo(repo_dir)
    
    # Agregar el archivo CSV al repositorio
    repo.git.add(archivo_csv)
    
    # Hacer commit de los cambios
    repo.index.commit('Añadido archivo CSV convertido desde GeoJSON')
    
    # Empujar los cambios al repositorio remoto
    origin = repo.remote(name='origin')
    origin.push()
    
    print("Archivo CSV subido a GitHub correctamente.")
else:
    print(f"El archivo {archivo_geojson} no existe.")
