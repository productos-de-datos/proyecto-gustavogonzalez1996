"""
Módulo de preparación de datos para pronóstico.
-------------------------------------------------------------------------------
"""

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
import pandas as pd
def make_features():

    df = pd.read_csv("./data_lake/business/precios-diarios.csv")
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["anio"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month
    df["dia_mes"] = df["fecha"].dt.day
    df["tipo_dia"] = df["fecha"].dt.weekday
    df["fin_semana"] = (df['tipo_dia']>=5).astype(int)

    df.to_csv("./data_lake/business/features/precios_diarios.csv", index=False)


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()