from sqlalchemy.sql import text
from sqlalchemy import create_engine
import logging




def check_high_risk(price_list):
    consecutive_drop_count = 0

    for i in range(len(price_list) - 1):
        price_change_percentage = (price_list[i + 1] - price_list[i]) / price_list[i] * 100

        # Check for a 50% price drop
        if price_change_percentage <= -50:
            consecutive_drop_count += 1
            if consecutive_drop_count >= 2:
                return True
        else:
            consecutive_drop_count = 0

    return False

def check_medium_risk(price_list):

    for i in range(len(price_list) - 1):
        price_change_percentage = (price_list[i + 1] - price_list[i]) / price_list[i] * 100

        # Check for a 20% price drop
        if price_change_percentage <= -20:
            return True

    return False

def risk_evaluation():

    postgres_db = 'coingeko'
    postgres_user = 'admin'
    postgres_password = 'admin'
    postgres_host = 'localhost'
    postgres_port = '5434'


    conn_str = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    engine = create_engine(conn_str)

    with engine.connect() as conn:# Make connection

        query_coin_data = text('SELECT coin, ARRAY_AGG(price) AS prices FROM coin_data GROUP BY coin')

        result_coin_data = conn.execute(query_coin_data)

        coin_risk_levels = {}
    
        for row in result_coin_data:# Iterate through the result set and determine risk levels for each coin
            coin, prices = row

            if check_high_risk(prices):
                coin_risk_levels.setdefault(coin, set()).add('High Risk')

            elif check_medium_risk(prices):
                coin_risk_levels.setdefault(coin, set()).add('Medium Risk')
            else:
                coin_risk_levels.setdefault(coin, set()).add('Low Risk')

        for coin_id, risk_levels in coin_risk_levels.items():
            logging.info(f'Coin {coin_id} has the following risk levels: {", ".join(risk_levels)}')


