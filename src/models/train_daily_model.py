"""
Módulo de entrenamiento del modelo.
-------------------------------------------------------------------------------
"""
"""Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de pronóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
import pickle as pkl

def load_data():
    df = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    data = df["precio"]
    return data
    
            # Se remueve la tendencia
def tendencia_removida():
    data = load_data()
    data_d1 = [data[t] - data[t - 1] for t in range(1, len(data))]
    return data_d1

def comp_ciclica_removida():
    data_d1 = tendencia_removida()
    data_d1d12 = [data_d1[t] - data_d1[t - 12] for t in range(12, len(data_d1))]
    return data_d1d12

def valores_escalados():
    data_d1d12 = comp_ciclica_removida()
    scaler = MinMaxScaler()
    data_d1d12_scaled = scaler.fit_transform(np.array(data_d1d12).reshape(-1, 1))
    data_d1d12_scaled = [u[0] for u in data_d1d12_scaled] # el largo de los datos escalados es 9404
    return data_d1d12_scaled
    
def matriz_regresores():
    data_d1d12_scaled = valores_escalados()
    P = 13
    X = []
    for t in range(P - 1, len(data_d1d12_scaled) - 1):
        X.append([data_d1d12_scaled[t - n] for n in range(P)])
    d = data_d1d12_scaled[P:] # el largo de X y d es 9391
    return X

def save_model(model):

    with open("src/models/precios-diarios.pickle", "wb") as file:
        pkl.dump(model, file, pkl.HIGHEST_PROTOCOL)

def train_daily_model():
    X = matriz_regresores()
    data_d1d12_scaled = valores_escalados()
    H = 4  # Se escoge arbitrariamente
    np.random.seed(123456)
    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.002,
        max_iter=100000,
    )
    model = mlp.fit(X[0:8441], data_d1d12_scaled[0:8441]) # 9391 - 950 = 8441. 9391 es el largo de X 
                                                          #  y 950 es aproximadamente el 10% de los datos
    save_model(model)
train_daily_model()
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

#train_daily_model()