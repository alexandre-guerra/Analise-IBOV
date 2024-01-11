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

    # Retorna as bibliotecas importadas para serem acessíveis no notebook
    return pd, np, plt, go, seasonal_decompose, MinMaxScaler, mean_squared_error, train_test_split, warnings, stats

def preparing_df():
    pd, _, _, _, _, _, _, _, _, _ = import_libraries()
    df = pd.read_csv('./Ibovespa.csv')
    df['Data'] = df['Data'].str.replace('.', '-')
    df['Data'] = pd.to_datetime(df['Data'], format='%d-%m-%Y')
    df = df[['Data', 'Último']]
    df.columns = ['ds', 'y']
    df.sort_values(by='ds', ascending=True, inplace=True)
    df.set_index('ds', inplace=True)
    return df
