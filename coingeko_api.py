import requests, logging,json
from datetime import datetime as dt
import pandas as pd


def date_entry():
    while True:
        date_input = input('Enter a valid date (YYYY-MM-DD): ')
        try:
            dt.strptime(date_input, '%Y-%m-%d')
            return str(date_input)
        except ValueError:
            print('Invalid date format. Please enter a date in the format YYYY-MM-DD.')
         

def CoinGeko_single_day():
    logging.info('Enter a crypto name: ')
    coin_name = input()
    date = date_entry()

    # Construct the correct date format as per the API requirements
    formatted_date = dt.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')

    base_url = 'https://api.coingecko.com/api/v3/coins/{id}/history?date={date}'
    url = base_url.format(id=coin_name, date=formatted_date)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        api_date = data.get('market_data', {}).get('current_price', {}).get('date')

        df = pd.DataFrame([data])
        df['API_Date'] = api_date

        xlsx_filename = f'{coin_name}_{formatted_date}.xlsx'  # Adjusted filename
        df.to_excel(xlsx_filename, index=False)

        logging.info('Data saved to Excel successfully.')
    else:
        logging.warning(f'Error in the request: status code: {response.status_code}')


def crypto_data(coin_id, start_date, end_date):
    vs_currency = "usd"
    days = (dt.strptime(end_date, '%Y-%m-%d') - dt.strptime(start_date, '%Y-%m-%d')).days
    interval = "daily"
    precision = "4"

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days={days}&interval={interval}&precision={precision}"

    response = requests.get(url)

    if response.status_code == 200:
        crypto_data = response.json()
        prices = crypto_data.get("prices", [])

        data_list = []

        for price in prices:
            timestamp, price_value = price
            data_dict = {
                "crypto_name": coin_id,
                "timestamp": pd.to_datetime(timestamp, unit='ms'),
                "price": price_value,
                "json": json.dumps(crypto_data) # Rest of the data in json format column
            }
            data_list.append(data_dict)

        crypto_df = pd.DataFrame(data_list) # DataFrame

        crypto_df_filtered = crypto_df[(crypto_df['timestamp'] >= pd.to_datetime(start_date)) &
                                       (crypto_df['timestamp'] <= pd.to_datetime(end_date))]

        return crypto_df_filtered

def triple_crypto_call():

    logging.info('Enter a start date: ')
    start = date_entry()
    logging.info('Enter an end date: ')
    end = date_entry()

    # Ensure start is before end
    start, end = min(start, end), max(start, end)

 
    df_bitcoin = crypto_data('bitcoin', start, end)
    df_ethereum = crypto_data('ethereum', start, end)
    df_cardano = crypto_data('cardano', start, end)

    # Combining dataframes
    combined_df = pd.concat([df_bitcoin, df_ethereum, df_cardano], ignore_index=True)

    # Final excel with the complete report of the selected date
    exit_file = "multi_crypto_report.xlsx"
    combined_df.to_excel(exit_file, index=False)