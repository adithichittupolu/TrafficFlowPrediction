import pandas as pd

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['hour'] = df['date_time'].dt.hour
    df['dayofweek'] = df['date_time'].dt.dayofweek
    df['month'] = df['date_time'].dt.month
    df = df[['hour', 'dayofweek', 'month', 'temp', 'rain_1h', 'snow_1h', 'traffic_volume']]
    df = df.dropna()
    return df
