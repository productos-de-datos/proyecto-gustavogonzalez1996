""" Crea un achivo con los precios promedios consolidados por dia.
"""
import pandas as pd
def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    route_try = True
    try:
        datos = pd.read_csv("./data_lake/cleansed/precios-horarios.csv")
    except FileNotFoundError:
        route_try = False
        datos= pd.read_csv("../../data_lake/cleansed/precios-horarios.csv")
    datos= datos.groupby('fecha', as_index=False).mean()
    datos= datos[['fecha','precio']]
    route = ("./data_lake/business/precios-diarios.csv" if route_try
            else "../../data_lake/business/precios-diarios.csv")
    datos.to_csv(route, index=False)

if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
