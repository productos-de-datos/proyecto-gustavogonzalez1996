"""
Módulo de limpieza de datos.
-------------------------------------------------------------------------------

    Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.

"""

import pandas as pd
import glob
import os

def clean_data():
    
    # merging the files
    files_joined = os.path.join('data_lake/raw/', "*.csv")

    # Return a list of all joined files
    list_files = glob.glob(files_joined)

    # Merge files by joining all files
    Unionarchivos = pd.concat(map(pd.read_csv, list_files), ignore_index=True)

    Unionarchivos['fecha'] = pd.to_datetime(Unionarchivos['fecha'], format="%Y/%m/%d")

    buscarnulos_media = Unionarchivos.where(Unionarchivos.notna(), Unionarchivos.mean(axis=1, numeric_only=True), axis=0)
 
    eliminar_duplicados = buscarnulos_media.drop_duplicates(['fecha'], keep='first')

    convertirfilas_columnas = pd.melt(eliminar_duplicados, id_vars="fecha")
    ordenar_valores= convertirfilas_columnas.sort_values(by = ['fecha', 'variable'])
    ordenar_valores.rename(columns={'variable': 'hora', 
                           'value': 'precio'}, inplace=True)

    ordenar_valores.to_csv('data_lake/cleansed/precios-horarios.csv', encoding='utf-8', index=False)

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":

    import doctest
    doctest.testmod()

    clean_data()