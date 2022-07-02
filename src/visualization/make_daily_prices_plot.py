"""
Módulo de creación del gráfico de precios diarios.
-------------------------------------------------------------------------------


"""

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('data_lake/business/precios-diarios.csv', index_col=0, parse_dates=True)
 
    plt.figure(figsize=(14, 5))
    plt.plot(df)
    plt.xlabel('Fecha')
    plt.ylabel('Precio promedio diario')
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

make_daily_prices_plot()