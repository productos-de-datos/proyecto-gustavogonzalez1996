"""
Módulo de pronostico con el modelo entrenado.
-------------------------------------------------------------------------------
"""



def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    from train_daily_model import matriz_regresores
    from train_daily_model import valores_escalados
    from train_daily_model import tendencia_removida
    from train_daily_model import load_data
    from train_daily_model import comp_ciclica_removida
    from sklearn.preprocessing import MinMaxScaler
    import pandas as pd
    import pickle as pkl
    import numpy as np

    def load_model():

        with open("src/models/precios-diarios.pkl", "rb") as file:
            model = pkl.load(file)

        return model

    def pronostico():
        model = load_model()
        X = matriz_regresores()
        # pronostico
        y_d1d12_scaled_m2 = model.predict(X)
        return y_d1d12_scaled_m2

    def desescalar_datos():
        data_d1d12_scaled = valores_escalados()
        data_d1 = tendencia_removida()
        data_d1d12 = comp_ciclica_removida()
        data = load_data()
        P = 13
        scaler = MinMaxScaler()
        y_d1d12_scaled_m2 = pronostico()

        obj = scaler.fit(np.array(data_d1d12).reshape(-1, 1))

        y_d1d12_scaled_m2 = data_d1d12_scaled[0:P] + y_d1d12_scaled_m2.tolist()

        y_d1d12_m2 = obj.inverse_transform([[u] for u in y_d1d12_scaled_m2])
        y_d1d12_m2 = [u[0] for u in y_d1d12_m2.tolist()]

        y_d1_m2 = [y_d1d12_m2[t] + data_d1[t] for t in range(len(y_d1d12_m2))]
        y_d1_m2 = data_d1[0:12] + y_d1_m2

        y_m2 = [y_d1_m2[t] + data[t] for t in range(len(y_d1_m2))]

        y_m2 = [data[0]] + y_m2

        return y_m2 

    # union datos reales y pronostico
    def save_pronostico():
        y_m2 = desescalar_datos()
        df_2 = pd.DataFrame(y_m2) 
        df_1 = pd.read_csv('data_lake/business/features/precios-diarios.csv')
        df = pd.concat([df_1, df_2], axis=1)
        df.columns = ["fecha", "precio_real", "pronostico_precio"]
        df.to_csv('data_lake/business/forecasts/precios-diarios.csv', encoding='utf-8', index=False, header=True)

    save_pronostico()
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
make_forecasts()