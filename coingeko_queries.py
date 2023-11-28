import logging
import pandas as pd
from sqlalchemy import create_engine

def avg_monthly_price():

    postgres_db = 'coingeko'  
    postgres_user = 'admin'    
    postgres_password = 'admin'  
    postgres_host = 'localhost'
    postgres_port = '5434'


    conn_str = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    engine = create_engine(conn_str)

    query = """
    SELECT
        coin,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month,
        AVG(price) AS average_price
    FROM
        coin_data
    GROUP BY
        coin,
        year,
        month
    ORDER BY
        coin,
        year,
        month
    """

    df = pd.read_sql(query, engine)

    engine.dispose()

    logging.info(df)

def avg_rebound_values():
    postgres_db = 'coingeko'
    postgres_user = 'admin'
    postgres_password = 'admin'
    postgres_host = 'localhost'
    postgres_port = '5434'

    
    conn_str = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    engine = create_engine(conn_str)

    query = """
    SELECT
        coin,
        date,
        price   
    FROM
        coin_data
    """

    df = pd.read_sql(query, engine)

    engine.dispose()

    df['price_difference'] = df.groupby('coin')['price'].diff()

    df['decreased_days'] = df['price_difference'].lt(0).astype(int).groupby(df['coin']).cumsum()
    filtered_df = df[df['decreased_days'] >= 3]

    positive_price_diff = filtered_df[filtered_df['price_difference'] > 0]

    avg_increase_per_coin = positive_price_diff.groupby('coin')['price_difference'].mean()

    logging.info(avg_increase_per_coin) 