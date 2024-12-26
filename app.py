import streamlit as st
import pandas as pd
from simulate_timeseries import generate_timeseries, simulate_market_conditions, simulate_multi_scenarios, save_to_csv
import plotly.graph_objects as go

st.title('Simulación de Datos de Series Temporales para Trading')

start_date = st.text_input('Fecha de inicio (YYYY-MM-DD HH:MM:SS)', '2023-01-01 00:00:00')
end_date = st.text_input('Fecha de fin (YYYY-MM-DD HH:MM:SS)', '2023-01-02 00:00:00')
filename = st.text_input('Nombre del archivo para guardar los datos', 'data.csv')
scenarios_str = st.text_input('Escenarios de mercado (e.g. "range, uptrend, downtrend")', 'range, uptrend')

if st.button('Generar Datos'):
    df = generate_timeseries(start_date, end_date)
    df = simulate_multi_scenarios(df, scenarios_str)
    save_to_csv(df, filename)
    st.success(f'Datos guardados en {filename}')
    st.dataframe(df.head())

    # Crear dataframe OHLC con resample (ej. cada 5 minutos)
    df_ohlc = df.resample('5T', on='datetime').agg({
        'ask': ['first', 'max', 'min', 'last']
    }).dropna()
    df_ohlc.columns = ['open', 'high', 'low', 'close']

    # Generar gráfico de velas
    fig = go.Figure(data=[go.Candlestick(
        x=df_ohlc.index,
        open=df_ohlc['open'],
        high=df_ohlc['high'],
        low=df_ohlc['low'],
        close=df_ohlc['close'])])
    st.plotly_chart(fig)
