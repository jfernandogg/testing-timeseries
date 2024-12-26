import pytest
import pandas as pd
from simulate_timeseries import generate_timeseries, simulate_market_conditions, simulate_multi_scenarios

def test_generate_timeseries():
    df = generate_timeseries("2023-01-01 00:00:00", "2023-01-01 00:00:05")
    assert len(df) == 6
    assert all(col in df.columns for col in ["datetime", "ask", "bid", "volume"])

def test_simulate_market_conditions_uptrend():
    df = generate_timeseries("2023-01-01 00:00:00", "2023-01-01 00:00:10")
    df_sim = simulate_market_conditions(df, market_scenario='uptrend')
    mid_point = len(df_sim) // 2
    first_half_mean = df_sim['ask'].iloc[:mid_point].mean()
    second_half_mean = df_sim['ask'].iloc[mid_point:].mean()
    # Verificar que el promedio de la segunda mitad sea mayor, lo cual indica una tendencia alcista
    assert second_half_mean > first_half_mean

def test_simulate_multi_scenarios():
    df = generate_timeseries("2023-01-01 00:00:00", "2023-01-01 00:00:10")
    df_multi = simulate_multi_scenarios(df, "range, uptrend, downtrend")
    assert len(df_multi) == len(df)
    # Verificar que no existan valores NaN extremos tras las simulaciones
    assert not df_multi.isnull().any().any()
