# Proyecto CRYPTO 📈🚀

## Objetivo 👈
El objetivo de este proyecto es construir un pipeline de datos que consuma información histórica de precios de criptomonedas desde la API de CoinGecko, almacenar los datos en archivos CSV y una base de datos PostgreSQL, y realizar predicciones de precios usando regresión lineal.

## Requerimientos Funcionales 🔎

### Primera Etapa: Extracción de Datos
- Consumir la API de CoinGecko para obtener los datos históricos de precios de las criptomonedas:
  - **Bitcoin (BTC)**: `https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365`
  - **Ethereum (ETH)**: `https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=365`
  - **Cardano (ADA)**: `https://api.coingecko.com/api/v3/coins/cardano/market_chart?vs_currency=usd&days=365`

### Segunda Etapa: Transformación de Datos
- Convertir los datos extraídos en DataFrames de pandas, donde los timestamps se convierten a formato de fecha.
- Los precios históricos se almacenan en las columnas `timestamp` y `price` para cada criptomoneda.

### Tercera Etapa: Carga de Datos
- Guardar los DataFrames resultantes en archivos CSV.
- Almacenar los datos transformados en una base de datos PostgreSQL.

### Cuarta Etapa: Predicción de Precios
- Usar regresión lineal para predecir los precios de las criptomonedas para los siguientes 365 días.
- Visualizar las predicciones junto con los datos históricos de precios en gráficos.

## Requerimientos Técnicos 🔧

- **Python 3.12.6**: El código debe ser compatible con la versión Python 3.12.6.
- **API CoinGecko**: Los datos de precios se obtienen desde el endpoint público de CoinGecko.
- **PostgreSQL**: La base de datos usada para almacenar los datos debe ser PostgreSQL.
- **SQLAlchemy**: La conexión a la base de datos debe implementarse utilizando SQLAlchemy.
- **.env**: El archivo `.env` debe contener los datos de conexión a la base de datos PostgreSQL.
- **Logging**: El programa debe registrar su ejecución usando la librería `logging`, generando archivos de log diarios.
- **Entorno Virtual**: Utilizar `venv` para crear un entorno virtual y guardar las dependencias en `requirements.txt`.
- **Gráficos**: Los gráficos deben visualizar las predicciones de precios y guardarse en formato PNG.

## Bases de Datos 📚
- **Conexión a la Base de Datos**:
  - Los datos extraídos y transformados deben almacenarse en una base de datos PostgreSQL.
  - Las tablas creadas deben corresponder a las criptomonedas: **btc**, **eth**, y **ada**.
  - La conexión se realiza mediante un SQLAlchemy engine, cuyas credenciales se obtienen desde variables de entorno.

## Ejecución del Proyecto 🛠

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/crypto.git
   ```

2. Crear y activar el entorno virtual:
    ```
    python -m venv venv

    # En Linux/Unix:
    source venv/bin/activate 

    # En Windows:
    venv\\Scripts\\activate
    ```

3. Instalar dependencias:
    ```
    pip install -r requirements.txt
    ```

4. Configurar el archivo .env con las credenciales de la base de datos PostgreSQL:
    ```
    DATABASE_USER=usuario
    DATABASE_PASSWORD=contraseña
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    DATABASE_NAME=crypto_db
    ```

5. Ejecutar el pipeline:
    ```
    python main.py
    ```
## Estructura del Proyecto 📁
```
crypto/
│
├── data/                       # Directorio de datos (CSV, logs, gráficos)
├── main.py                     # Script principal
├── functions.py                # Funciones de extracción, transformación, carga y predicción
├── connection.py               # Función para la conexión a PostgreSQL
├── .env                        # Archivo de configuración de variables de entorno
├── requirements.txt            # Dependencias del proyecto
└── README.md    
```