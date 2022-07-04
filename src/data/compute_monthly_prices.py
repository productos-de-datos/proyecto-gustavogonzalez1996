""" Crea un achivo con los precios promedios consolidados por mes y año.
"""
import pandas as pd
def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional

    """
    route_try = True
    try:
        datos= pd.read_csv("./data_lake/cleansed/precios-horarios.csv")
    except FileNotFoundError:
        route_try = False
        datos= pd.read_csv("../../data_lake/cleansed/precios-horarios.csv")
    datos["year-month"] = datos["fecha"].map(lambda x: str(x)[0:7])

    datos = datos.groupby('year-month', as_index=False).mean()
    datos = datos[['year-month','precio']]
    datos = datos.rename(columns= {'year-month': 'fecha'})
    datos["fecha"] =  datos["fecha"].map(lambda x: x + str("-01"))
    route = ("./data_lake/business/precios-mensuales.csv" if route_try
            else "../../data_lake/business/precios-mensuales.csv")
    datos.to_csv(route, index=False)

if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
