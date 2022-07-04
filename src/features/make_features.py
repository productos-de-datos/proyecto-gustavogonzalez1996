"""
Módulo de preparación de datos para pronóstico.
-------------------------------------------------------------------------------
"""

import doctest
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
    rutainput='data_lake/business/precios-diarios.csv'
    rutaouput="data_lake/business/features/precios-diarios.csv"
    df_caract=pd.read_csv(rutainput,index_col=None,header=0)
    df_caract["fecha"]=pd.to_datetime(df_caract["fecha"]).dt.strftime('%Y-%m-%d')
    df_caract.to_csv(rutaouput,index=False,header=True)
    return True
if __name__=="__main__":
    make_features()
    doctest.testmod()