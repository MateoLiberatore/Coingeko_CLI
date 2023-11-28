from coingeko_api import CoinGeko_single_day, triple_crypto_call
from coingeko_db import load_data
from coingeko_plots import generate_plots
from coingeko_queries import avg_monthly_price, avg_rebound_values
from price_trend import price_trend
from risk_evaluation import risk_evaluation
import logging

#handler for the .log file
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='logs.log',
                    filemode='a')

#handler to show messages in the console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(console)

logging.info('Please, before continuing create a postgres docker container to store the data (ports:5434:5432)')

# Menu options
menu_options = {
    '1': 'CoinGeko Single Day',
    '2': 'Triple Crypto Call',
    '3': 'Load Data',
    '4': 'Generate Plots',
    '5': 'Average Monthly Price',
    '6': 'Average Rebound Values',
    '7': 'Price Trends',
    '8': 'Risk Evaluation',
    '9': 'Exit'
}


menu_functions = {
    '1': CoinGeko_single_day,
    '2': triple_crypto_call,
    '3': lambda: load_data('/home/mateo/Desktop/MUTT/mutt/src/multi_crypto_report.xlsx'),
    '4': generate_plots,
    '5': avg_monthly_price,
    '6': avg_rebound_values,
    '7': price_trend,
    '8': risk_evaluation,
    '9': exit  # This will exit the program
}

# Display the menu
while True:
    logging.info("Menu:")
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    choice = input("Enter your choice: ")

    if choice in menu_functions:
        if choice == '0':
            break  
        else:
           
            menu_functions[choice]()
    else:
        logging.info("Invalid choice. Please try again.")
