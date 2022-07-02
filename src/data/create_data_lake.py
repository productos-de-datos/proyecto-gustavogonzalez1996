"""
Módulo de creación de carpetas.
-------------------------------------------------------------------------------


Cree el data lake con sus capas
Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
las siguientes subcarpetas:
    .
    |
     ___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
          ___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/
    
test_
>>> os.path.isdir("data_lake/business/reports/figures")
True
"""
import os
from os import mkdir

def create_data_lake():
    mkdir("data_lake")
    mkdir("data_lake/landing")
    mkdir("data_lake/raw")
    mkdir("data_lake/cleansed")
    mkdir("data_lake/business")
    mkdir("data_lake/business/reports")
    mkdir("data_lake/business/reports/figures")
    mkdir("data_lake/business/features")
    mkdir("data_lake/business/forecasts")
    #raise NotImplementedError("Implementar esta función")

def test_01():
    assert os.path.isdir("data_lake") is True
    assert os.path.isdir("data_lake/business/reports") is True
    assert os.path.isdir("data_lake/business/reports/figures") is True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    create_data_lake()