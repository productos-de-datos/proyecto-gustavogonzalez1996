"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
"""
import requests as req

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    for num in range(1995, 2022):
        if num in range(2016, 2018):
            url = f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{num}.xls?raw=true'
            file = req.get(url, allow_redirects=True)
            open(f'data_lake/landing/{num}.xls', 'wb').write(file.content)
        else:
            url = f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{num}.xlsx?raw=true'
            file = req.get(url, allow_redirects=True)
            open(f'data_lake/landing/{num}.xlsx', 'wb').write(file.content)

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ingest_data()