jfernandogg: genera un archivo README.md para github sobre este proyecto

Workspace: Recopilando información del área de trabajo

# Simulador de Series Temporales para Trading

Este proyecto implementa un simulador de series temporales financieras con diferentes escenarios de mercado, utilizando Python y Streamlit para la visualización.

## 🚀 Características

- Generación de series temporales con datos de ask, bid y volumen
- Simulación de diferentes condiciones de mercado:
  - Tendencia alcista (uptrend)
  - Tendencia bajista (downtrend)
  - Rango (range)
- Interfaz web interactiva con Streamlit
- Visualización de gráficos de velas (candlesticks)
- Exportación de datos a CSV

## 📋 Requisitos

```txt
pandas>=1.5.0
numpy>=1.21.0
streamlit>=1.20.0
plotly>=5.13.0
pytest>=7.0.0
pytest-cov>=4.0.0
```

## 🛠️ Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
```sh
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```
3. Instalar dependencias:
```sh
pip install -r requirements.txt
```

## 💻 Uso

### Interfaz Web
Para iniciar la aplicación web:
```sh
streamlit run app.py
```

### Línea de Comandos
Para ejecutar el simulador desde la línea de comandos:
```sh
python simulate_timeseries.py
```

## 🧪 Tests

Para ejecutar las pruebas:
```sh
pytest test_simulate_timeseries.py
```

## 🔧 Funcionalidades Principales

- 

generate_timeseries()

: Genera series temporales sintéticas
- 

simulate_market_conditions()

: Simula diferentes condiciones de mercado
- 

simulate_multi_scenarios()

: Combina múltiples escenarios en una serie temporal

## 📝 Ejemplo

```python
from simulate_timeseries import generate_timeseries, simulate_multi_scenarios

# Generar datos
df = generate_timeseries("2023-01-01 00:00:00", "2023-01-01 00:00:10")
# Simular escenarios
df = simulate_multi_scenarios(df, "range, uptrend, downtrend")
```

## 📊 Visualización

La interfaz web permite:
- Configurar fechas de inicio y fin
- Seleccionar escenarios de mercado
- Visualizar gráficos de velas
- Exportar datos a CSV

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

jfernandogg: esta excelente generalo con todas las secciones

Workspace: Recopilando información del área de trabajo

# Simulador de Series Temporales para Trading 📊

Este proyecto implementa un simulador de series temporales financieras que genera datos sintéticos para diferentes escenarios de mercado, utilizando Python y Streamlit para visualización.

## 📌 Características Principales

- Generación de series temporales con datos de ask, bid y volumen
- Simulación de condiciones de mercado:
  - Tendencia alcista
  - Tendencia bajista 
  - Rango lateral
- Interfaz web interactiva
- Visualización con gráficos de velas (candlesticks)
- Exportación de datos a CSV

## 🔧 Estructura del Proyecto

```
├── app.py                      # Interfaz web con Streamlit
├── simulate_timeseries.py      # Lógica principal de simulación
├── test_simulate_timeseries.py # Tests unitarios
└── requirements.txt            # Dependencias del proyecto
```

## 🔍 Funciones Principales

- 

generate_timeseries()

: Genera series temporales básicas
- 

simulate_market_conditions()

: Simula escenarios específicos
- 

simulate_multi_scenarios()

: Combina múltiples escenarios
- 

save_to_csv()

: Exporta datos a CSV

## ⚙️ Requisitos

```txt
pandas>=1.5.0
numpy>=1.21.0
streamlit>=1.20.0
plotly>=5.13.0
pytest>=7.0.0
pytest-cov>=4.0.0
```

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/usuario/trading-timeseries-simulator.git
cd trading-timeseries-simulator
```

2. Crear entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Interfaz Web
Ejecutar la aplicación web:
```bash
streamlit run app.py
```

### Línea de Comandos
Ejecutar el simulador directamente:
```bash
python simulate_timeseries.py
```

## 🧪 Tests

Ejecutar pruebas unitarias:
```bash
pytest test_simulate_timeseries.py
```

## 📝 Ejemplo de Uso

```python
from simulate_timeseries import generate_timeseries, simulate_multi_scenarios

# Generar datos
df = generate_timeseries("2023-01-01 00:00:00", "2023-01-01 00:00:10")

# Simular escenarios múltiples
df = simulate_multi_scenarios(df, "range, uptrend, downtrend")

# Guardar resultados
df.to_csv("data.csv", index=False)
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## 👥 Autores

- Juan Fernando Gallego Gomez - [GitHub](https://github.com/jfernandogg)

## 📧 Contacto

Email - juan.gallego@gmail.com
Project Link: [https://github.com/jfernandogg/trading-timeseries-simulator](https://github.com/jfernandogg/trading-timeseries-simulator)