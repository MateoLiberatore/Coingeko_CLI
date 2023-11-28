from sqlalchemy.sql import text
from sqlalchemy import create_engine
import logging
import pandas as pd


def price_trend():
    postgres_db = 'coingeko'
    postgres_user = 'admin'
    postgres_password = 'admin'
    postgres_host = 'localhost'
    postgres_port = '5434'


    conn_str = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    engine = create_engine(conn_str)


    with engine.connect() as conn:

        query_coin_data = text('SELECT * FROM coin_data')
        result = conn.execute(query_coin_data)


        df = pd.DataFrame(result.fetchall(), columns=result.keys())


    trend_values = []
    variance_values = []
    for i in range(len(df)):
        if i < 7:
            trend_values.append(0)
            variance_values.append(0)
        else:
        # Calculate trend as the difference between T0 and T-1
            trend = df.loc[i, 'price'] - df.loc[i-1, 'price']
            trend_values.append(trend)

        # Calculate variance for the previous 7 days
            variance = df.loc[i-6:i, 'price'].var()
            variance_values.append(variance)


    df['trend'] = trend_values
    df['variance'] = variance_values

    logging.info(df)

    output_file_path = 'price_trend.xlsx'
    df.to_excel(output_file_path, index=False)

    logging.info('DataFrame saved to Excel file.')

