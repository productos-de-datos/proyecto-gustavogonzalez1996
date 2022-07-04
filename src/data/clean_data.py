""" Limpia y transforma los archivos para consolidarlos y finalmente procesarlos
"""
import pandas as pd
def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv,
    cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.

    """
    horas = {'0': '00', '1':'01', '2':'02', '3':'03',
     '4': '04', '5':'05', '6':'06', '7':'07', '8':'08', '9': '09'}
    try:
        datos = pd.read_csv("./data_lake/raw/1995.csv")
    except FileNotFoundError:
        datos= pd.read_csv("../../data_lake/raw/1995.csv")

    datos = datos.rename(columns=horas)
    datos = pd.melt(datos, id_vars= ["Fecha"], value_vars = [str(hour) if hour >=10
    else '0'+ str(hour) for hour in range(0,24)])

    for i in range(1996,2022):
        route_try = True
        try:
            datos1 = pd.read_csv("./data_lake/raw/" + str(i) + ".csv")
        except FileNotFoundError:
            route_try = False
            datos1 = pd.read_csv("../../data_lake/raw/" + str(i) + ".csv")
        datos1 = datos1.rename(columns=horas)
        datos1 = pd.melt(datos1, id_vars= ["Fecha"], value_vars = [str(hour) if hour >=10
        else '0'+ str(hour) for hour in range(0,24)])
        datos = pd.concat([datos,datos1])

    datos =  datos.rename(columns={"Fecha": "fecha", "variable": "hora", "value": "precio"})
    route = ("./data_lake/cleansed/precios-horarios.csv" if route_try
            else "../../data_lake/cleansed/precios-horarios.csv")
    datos.to_csv(route, index=False)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
