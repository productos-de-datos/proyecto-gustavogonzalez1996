"""
Módulo de transformación de datos.
-------------------------------------------------------------------------------



"""
import pandas as pd

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/.xls a data_lake/raw/.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

    for num in range(1995, 2022):
        if num in range(2016, 2018):
            read_xls = pd.read_excel(f'data_lake/landing/{num}.xls')
            delete_empty_rows = read_xls.dropna(axis=0, thresh=10)
            delete_header = delete_empty_rows.iloc[1:]
            data = delete_header.iloc[:, 0:25]

            data.columns = ["fecha", "00", "01", "02", "03", "04", "05", "06",
            "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23"]

            data["fecha"] = pd.to_datetime(data["fecha"], format="%Y/%m/%d")
            data.to_csv(f'data_lake/raw/{num}.csv', encoding='utf-8', index=False, header=True)
        else:
            read_xlsx = pd.read_excel(f'data_lake/landing/{num}.xlsx')
            delete_empty_rows = read_xlsx.dropna(axis=0, thresh=10)
            delete_header = delete_empty_rows.iloc[1:]
            data = delete_header.iloc[:, 0:25]

            data.columns = ["fecha", "00", "01", "02", "03", "04", "05", "06",
            "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23"]

            data["fecha"] = pd.to_datetime(data["fecha"], format="%Y/%m/%d")
            data.to_csv(f'data_lake/raw/{num}.csv', encoding='utf-8', index=False, header=True)

    #raise NotImplementedError("Implementar esta función")

def test_02():
    assert pd.read_csv('data_lake/raw/1995.csv').columns.tolist() == ["fecha", "00", "01", "02",
                        "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                        "15", "16", "17", "18","19", "20", "21", "22", "23"]
    assert pd.read_csv('data_lake/raw/1995.csv').shape[1] == 25

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    transform_data()