import logging
from datetime import datetime
from connection import get_db_engine
from functions import extract, transform, load, predict_prices

date_str = datetime.now().strftime('%Y-%m-%d')

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(f"data\\crypto_{date_str}.log"), logging.StreamHandler()])


def main():
    data = extract()
    if data:
        transformed_data = transform(data)
        engine = get_db_engine()
        load(transformed_data, engine)
        predict_prices(transformed_data)


if __name__ == "__main__":
    main()
