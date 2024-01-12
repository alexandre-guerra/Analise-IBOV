def import_libraries():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go

    from statsmodels.tsa.seasonal import seasonal_decompose
    from scipy import stats

    # Para machine learning
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split

    import warnings
    warnings.filterwarnings('ignore')

    from statsmodels.tsa.stattools import adfuller

    # Retorna as bibliotecas importadas para serem acessíveis no notebook
    return pd, np, plt, go, seasonal_decompose, MinMaxScaler, mean_squared_error, train_test_split, warnings, stats, adfuller

def preparing_df():
    pd, _, _, _, _, _, _, _, _, _, _ = import_libraries()
    df = pd.read_csv('./Ibovespa.csv')
    df['Data'] = df['Data'].str.replace('.', '-')
    df['Data'] = pd.to_datetime(df['Data'], format='%d-%m-%Y')
    df = df[['Data', 'Último']]
    df.columns = ['ds', 'y']
    df.sort_values(by='ds', ascending=True, inplace=True)
    df.set_index('ds', inplace=True)
    return df


def test_stationarity(timeseries):
    pd, _, plt, _, _, _, _, _, _, _, adfuller = import_libraries()

    movingAverage = timeseries.rolling(window=12).mean()
    movingSTD = timeseries.rolling(window=12).std()

    plt.figure(figsize=(15,6))
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(movingAverage, color='red', label='Rolling Mean')
    std = plt.plot(movingSTD, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    print('Results of Dickey Fuller Test:')
    dftest = adfuller(timeseries['y'], autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

    if (dfoutput[1] < 0.05):
        print('Conclusão: A série é Estacionária.')
    else:
        print('Conclusão: A série NÂO é Estacionária.')
