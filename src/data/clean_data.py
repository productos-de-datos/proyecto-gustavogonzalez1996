"""Lea con la libreria glob todos los CSV en la carpeta data_lake/raw/ los une con append y finalmente los convierte
a pandas, elimina las filas vacias y posteriormente con la funcion de pandas melt organiza los datos
con columnas fecha, hora y precio. organiza su formato, filtra desde 1997 a 2021 y exporta en csv el archivo procesado en data_lake/cleansed/
"""


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.
    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:
    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional
    Este archivo contiene toda la información del 1997 a 2021.
    """
    import pandas as pd
    import glob
    import numpy as np

    ruta=glob.glob(r'data_lake/raw/*.csv')

    lista=[]

    for archivo in ruta:
        df=pd.read_csv(archivo,index_col=None,header=0)
        lista.append(df)
    
    archivo_completo=pd.concat(lista,axis=0,ignore_index=True)

    archivo_completo=archivo_completo[archivo_completo["Fecha"].notnull()]
    archivo_completo=pd.melt(archivo_completo,id_vars=['Fecha'],var_name='hora', value_name='precio')
    archivo_completo['hora']=np.where(pd.to_numeric(archivo_completo['hora']) <= 9,pd.concat(["0"+archivo_completo['hora']]),archivo_completo['hora'])
    archivo_completo["Fecha"] = pd.to_datetime(archivo_completo["Fecha"]).dt.strftime('%Y-%m-%d')
    date1="2017-01-01"
    date2 = "2021-12-31"
    month_list = [i.strftime('%Y-%m-%d') for i in pd.date_range(start=date1, end=date2)]
    archivo_completo=archivo_completo[archivo_completo.Fecha.isin(month_list)]
    archivo_completo=archivo_completo.rename(columns={"Fecha":"fecha"})
    archivo_completo.to_csv("data_lake/cleansed/precios-horarios.csv",index=False, header=True)

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()