"""
Crea nuevas caracteristicas para predecir el precio diario de electricidad.
Las caracteristicas agregadas son: dia, mes, ano, tipo_dia, festivo, fin_semana
"""
import pandas as pd
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
    datos = pd.read_csv("./data_lake/business/precios-diarios.csv")
    datos["fecha"] = pd.to_datetime(datos["fecha"])
    datos["anio"] = datos["fecha"].dt.year
    datos["mes"] = datos["fecha"].dt.month
    datos["dia_mes"] = datos["fecha"].dt.day
    datos["tipo_dia"] = datos["fecha"].dt.weekday
    datos["fin_semana"] = (datos["tipo_dia"]>=5).astype(int)

    datos.to_csv("./data_lake/business/features/precios_diarios.csv", index=False)


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
