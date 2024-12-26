import pandas as pd
import numpy as np
import datetime
import random

def generate_timeseries(start_date, end_date, freq='s'):  # Cambiar 'S' por 's'
    date_range = pd.date_range(start=start_date, end=end_date, freq=freq)
    data = {
        'datetime': date_range,
        'ask': np.random.rand(len(date_range)) * 100,
        'bid': np.random.rand(len(date_range)) * 100,
        'volume': np.random.randint(1, 1000, size=len(date_range))
    }
    df = pd.DataFrame(data)
    return df

def simulate_market_conditions(df, market_scenario='range'):
    df['ask'] = df['ask'].rolling(window=10, min_periods=1).mean() + np.random.randn(len(df)) * 2
    df['bid'] = df['bid'].rolling(window=10, min_periods=1).mean() + np.random.randn(len(df)) * 2
    if market_scenario == 'uptrend':
        df['ask'] += np.arange(len(df)) * 0.01
        df['bid'] += np.arange(len(df)) * 0.01
    elif market_scenario == 'downtrend':
        df['ask'] -= np.arange(len(df)) * 0.01
        df['bid'] -= np.arange(len(df)) * 0.01
    return df

def simulate_multi_scenarios(df, scenarios_str):
    scenarios = [s.strip() for s in scenarios_str.split(',')]
    n = len(df)
    start_idx = 0
    for i, scenario in enumerate(scenarios):
        # Calcular tamaño de la porción de manera aleatoria
        remaining = n - start_idx - (len(scenarios) - i - 1)
        chunk_size = random.randint(1, remaining) if remaining > 0 else 0
        end_idx = start_idx + chunk_size

        # Extraer la porción correspondiente y aplicar la lógica de mercado
        df_chunk = df.iloc[start_idx:end_idx].copy()
        df_chunk['ask'] = df_chunk['ask'].rolling(window=10, min_periods=1).mean() + np.random.randn(len(df_chunk)) * 2
        df_chunk['bid'] = df_chunk['bid'].rolling(window=10, min_periods=1).mean() + np.random.randn(len(df_chunk)) * 2
        if scenario == 'uptrend':
            df_chunk['ask'] += np.arange(len(df_chunk)) * 0.01
            df_chunk['bid'] += np.arange(len(df_chunk)) * 0.01
        elif scenario == 'downtrend':
            df_chunk['ask'] -= np.arange(len(df_chunk)) * 0.01
            df_chunk['bid'] -= np.arange(len(df_chunk)) * 0.01
        # Asignar la porción procesada de nuevo
        df.iloc[start_idx:end_idx] = df_chunk
        start_idx = end_idx
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    start_date = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
    end_date = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")
    filename = input("Enter filename to save the data (e.g., data.csv): ")
    scenarios_str = input("Enter market scenarios (e.g., uptrend, range, downtrend): ")

    df = generate_timeseries(start_date, end_date)
    df = simulate_multi_scenarios(df, scenarios_str)
    save_to_csv(df, filename)
    print(f"Data saved to {filename}")
