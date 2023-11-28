import logging
import pandas as pd
from sqlalchemy import create_engine, Float, Date
from sqlalchemy.exc import SQLAlchemyError



def load_data(file_path):
    try:
        xlsx_file = file_path

        postgres_db = 'coingeko'
        postgres_user = 'admin'
        postgres_password = 'admin'
        postgres_host = 'localhost'
        postgres_port = '5434'

        conn_str = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
        engine = create_engine(conn_str)  # Make connection

        df = pd.read_excel(xlsx_file)

        df_coin_data = df[['crypto_name', 'timestamp', 'price', 'json']].copy()
        df_coin_data.rename(columns={'crypto_name': 'coin', 'timestamp': 'date'}, inplace=True)
        df_coin_data['date'] = pd.to_datetime(df_coin_data['date'])

        df_coin_data.drop_duplicates(subset=['coin', 'date'], inplace=True)
        df_coin_data.to_sql('coin_data', engine, if_exists='append', index=False, dtype={'price': Float(), 'date': Date()})

        df['year'] = df['timestamp'].dt.year
        df['month'] = df['timestamp'].dt.month

        df_monthly = df.groupby(['crypto_name', 'year', 'month']).agg({'price': ['min', 'max']}).reset_index()
        df_monthly.columns = ['coin', 'year', 'month', 'min_price', 'max_price']

        df_monthly.drop_duplicates(subset=['coin', 'year', 'month'], inplace=True)
        df_monthly.to_sql('coin_month_data', engine, if_exists='append', index=False)

        # Cerrar la conexión
        engine.dispose()

        logging.info("Data loaded successfully.")

    except SQLAlchemyError as e:
        logging.warning("An error occurred while working with the database:", str(e))

    except FileNotFoundError:
        logging.warning("File not found. Please provide a valid file path.")

    except pd.errors.ParserError:
        logging.warning("Error occurred while parsing the Excel file. Please check the file format and structure.")

    except Exception as e:
        logging.warning("An unexpected error occurred:", str(e))

