def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
    """
    # Importe pandas
    # Importe pickle
    # Importe numpy
    # Importe LinearRegression
    # Importe train_test_split
    # Importe mean_squared_error
    import pandas as pd
    import pickle
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import RandomForestRegressor

    # Lea el archivo `precios-diarios` y asignelo al DataFrame `df`
    df = pd.read_csv("data_lake/business/features/precios-diarios.csv", encoding = 'utf-8', sep=',')

    # Asigne a la variable los valores de la columna `fecha`
    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y%m%d')
    X_fecha = np.array(df['fecha']).reshape(-1,1)

    # Asigne a la variable los valores de la columna `precio`
    y_precio = np.array(df['precio']).reshape(-1,1)

    # Divida los datos de entrenamiento y prueba. La semilla del generador de números
    # aleatorios es 123456. El tamaño de la muestra de entrenamiento es del 80%
    (X_train, X_test, y_train, y_test,) = train_test_split(X_fecha, y_precio, test_size=0.2, random_state=123456,)

    # Cree una instancia del modelo de regresión lineal
    clf = RandomForestRegressor(n_estimators=100, max_features='sqrt', n_jobs=-1, oob_score = True, random_state = 123456)
    
    # Entrene el clasificador usando X_train y y_train
    clf.fit(X_train,y_train)

    pickle.dump(clf, open('src/models/precios-diarios.pickle', 'wb'))

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()