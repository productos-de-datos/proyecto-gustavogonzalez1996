"""
Módulo de computación de precios diarios.
-------------------------------------------------------------------------------



"""

def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    import pandas as pd

    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format="%Y/%m/%d")
    df = df.set_index('fecha')

    df = df.resample('D').mean()
    df = df.reset_index()
    df = df.iloc[:, [0, 2]]

    df.to_csv('data_lake/business/precios-diarios.csv', encoding='utf-8', index=False)

    # raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

compute_daily_prices()