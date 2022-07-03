"""
Módulo de entrenamiento del modelo.
-------------------------------------------------------------------------------
"""
"""Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de pronóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
"""

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import joblib
import os

import pandas as pd
def train_daily_model():

    df = pd.read_csv("./data_lake/business/features/precios_diarios.csv")

    df = df.drop(columns=["fecha"])

    y = df["precio"].array
    X = df.drop(columns=["precio"])
    X_train, X_Rem, y_true_train, y_Rem = train_test_split(X, y, test_size=0.25, random_state=123)
    X_valid, X_test, y_valid, y_true_test = train_test_split(X_Rem,
                                                         y_Rem,
                                                         test_size=0.3
                                                         ,random_state=123)

    X_test["y"] = y_true_test 
    X_test.to_csv('src/models/datosforecast.csv')
    model = MLPRegressor(max_iter= 150,
        activation='relu', 
        solver= 'sgd', 
        learning_rate_init= 0.001) 

    model = MLPRegressor() 
   
    param_grid = [
          {
              "hidden_layer_sizes": [(1,),(2,),(3,),(4,),(5,)], 
              "random_state": [1000, 1001, 1002, 1003, 1004, 1005]
              
          }
    ]

    grid_search = GridSearchCV(estimator = model, 
                          param_grid=param_grid, cv=5) 

    dataTrain = grid_search.fit(X_train, y_true_train)

    parent_dir = "src/models"
    cwd = os.getcwd()
    path_parent_dir = os.path.join(cwd, parent_dir)

    joblib.dump(dataTrain, path_parent_dir + '/precios-diarios.pkl')


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()