"""
Módulo pipeline.
-------------------------------------------------------------------------------

Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.

"""
import luigi
from luigi import Task, LocalTarget

class Descargar_archivos(Task):

    def output(self):
        return LocalTarget('data_lake/landing/archivo.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open("w") as outfile:
            ingest_data()

class Transformar_archivos(Task):

    def requires(self):
        return Descargar_archivos()
    
    def output(self):
        return LocalTarget('data_lake/raw/archivo.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open("w") as outfile:
            transform_data()

class Tabla_U_Precios(Task):
    
    def requires(self):
        return Transformar_archivos()
    
    def output(self):
        return LocalTarget('data_lake/cleansed/archivo.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open("w") as outfile:
            clean_data()

class Precio_P_Diario(Task):
    
    def requires(self):
        return Tabla_U_Precios()
    
    def output(self):
        return LocalTarget('data_lake/business/archivo.txt')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open("w") as outfile:
            compute_daily_prices()

class Precio_P_Mensual(Task):
    
    def requires(self):
        return Precio_P_Diario()
    
    def output(self):
        return LocalTarget('data_lake/business/archivo.txt')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open("w") as outfile:
            compute_monthly_prices()


if __name__ == "__main__":
    luigi.run(["Precio_P_Mensual", "--local-scheduler"])

    import doctest

    doctest.testmod()