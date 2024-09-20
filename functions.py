import requests
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

logger = logging.getLogger(__name__)

def extract():
    """
    Extracts historical price data for Bitcoin (BTC), Ethereum (ETH), and Cardano (ADA) 
    from the CoinGecko API for the past 365 days.
    """
    coins = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "ADA": "cardano"
    }
    historical_data = {}

    for symbol, id_ in coins.items():
        url = f"https://api.coingecko.com/api/v3/coins/{id_}/market_chart?vs_currency=usd&days=365"
        logger.info(f"Extracting historical data for {symbol}...")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            historical_data[symbol] = data['prices'] 
            logger.info(f"Data for {symbol} extracted successfully.")
        else:
            logger.error(f"Error getting data for {symbol}: {response.status_code}")

    return historical_data

def transform(data):
    """
    Transforms the historical price data into DataFrames with timestamps converted to datetime.
    """
    logger.info("Transforming data...")
    dataframes = {}

    for symbol, prices in data.items():
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
        dataframes[symbol] = df
        logger.info(f"Data for {symbol}:")
        print(f"\nData for {symbol}:")
        print(df.head())

    logger.info("Data transformed successfully.")
    return dataframes

def load(dataframes, engine):
    """
    Loads transformed data into CSV files and a PostgreSQL database.
    """
    logger.info("Loading data...")

    # Save DataFrames as CSV and to the database
    for key, df in dataframes.items():
        # Save as CSV
        csv_file = f"data\\{key}_data.csv"
        df.to_csv(csv_file, index=False)
        logger.info(f"Data for {key} saved in {csv_file}")

        # Save to the database
        df.to_sql(key.lower(), con=engine, if_exists='replace', index=False)
        logger.info(f"Table {key.lower()} created in the database.")

    logger.info("Data loaded successfully.")

def predict_prices(dataframes):
    """
    Performs linear regression on historical price data to predict future prices for cryptocurrencies 
    and plots the actual and predicted prices.
    """
    plt.figure(figsize=(12, 8))

    for symbol, df in dataframes.items():
        # Prepare the data
        df['days'] = (df['timestamp'] - df['timestamp'].min()).dt.days
        X = df[['days']]
        y = df['price']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict values
        df['predicted_price'] = model.predict(X)

        # Predict the price 365 days into the future
        last_day = df['days'].max()
        future_days = pd.DataFrame({'days': np.arange(1, 366)})  # Days from 1 to 366
        future_prices = model.predict(future_days)

        # Create a new DataFrame for future predictions
        future_df = pd.DataFrame({'days': future_days['days'], 'price': future_prices})
        
        # Plot the actual data points
        plt.scatter(df['days'], df['price'], label=f"{symbol} Actual Prices", alpha=0.6)

        # Plot the regression line
        plt.plot(df['days'], df['predicted_price'], label=f"{symbol} Regression Line", linestyle='--')

    plt.grid(True, linestyle='--', color='gray')

    # Add titles and labels
    plt.title('Cryptocurrency Price Predictions Using Linear Regression')
    plt.xlabel('Days')
    plt.ylabel('Price (USD)')
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig('data\\crypto_regression.png')
    plt.show() 
