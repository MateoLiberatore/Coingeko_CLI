import logging,os,glob
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from coingeko_api import crypto_data
 


def thirty_days_back():

  
    start = datetime.now()
    end = start - timedelta(days=30)

    start, end = min(start, end), max(start, end)

    formatted_start = start.strftime('%Y-%m-%d')
    formatted_end = end.strftime('%Y-%m-%d')

    df_bitcoin = crypto_data('bitcoin', formatted_start, formatted_end)
    df_ethereum = crypto_data('ethereum', formatted_start, formatted_end)
    df_cardano = crypto_data('cardano', formatted_start, formatted_end)

    combined_df = pd.concat([df_bitcoin, df_ethereum, df_cardano], ignore_index=True)
    exit_file_path = os.path.join(os.getcwd(), "plots.xlsx")

    combined_df.to_excel(exit_file_path, index=False)

    return exit_file_path

def find_file(nombre_archivo):
    # Patrón para buscar el archivo por nombre
    patrón = f"**/{nombre_archivo}"

    # Buscar archivos que coincidan con el patrón en el directorio actual
    archivos_encontrados = glob.glob(patrón, recursive=True)

    if archivos_encontrados:
        # Devolver la primera ruta encontrada
        return archivos_encontrados[0]
    else:
        return None


def delete_file(filepath):
    try:
        os.remove(filepath)
        logging.info("Deleted File: %s", filepath)
    except FileNotFoundError:
        logging.info("File not found %s", filepath)
    except PermissionError:
        logging.info("Permission not granted: %s", filepath)
    except Exception as e:
        logging.error("Error: %s", str(e))



def generate_plots():

    thirty_days_back()
    file_name_to_search = "plots.xlsx"  
    file_path = find_file(file_name_to_search)

    if file_path:
        print("Archivo encontrado:", file_path)
        df = pd.read_excel(file_path)

# Filter the data for Bitcoin
        bitcoin_data = df[df['crypto_name'] == 'bitcoin']

        plt.figure(figsize=(10, 6))
        plt.plot(bitcoin_data['timestamp'], bitcoin_data['price'], marker='o', color='b')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Bitcoin Price Over Time')
        plt.xticks(rotation=45)

        plt.savefig('bitcoin_price.pdf')

        plt.tight_layout()
        plt.show()
        logging.info('Bitcoin PDF plot generated')

# Filter the data for Ethereum
        ethereum_data = df[df['crypto_name'] == 'ethereum']

        plt.figure(figsize=(10, 6))
        plt.plot(ethereum_data['timestamp'], ethereum_data['price'], marker='o', color='g')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Ethereum Price Over Time')
        plt.xticks(rotation=45)

        plt.savefig('ethereum_price.pdf')

        plt.tight_layout()
        plt.show()
        logging.info('Ethereum PDF plot generated')


# Filter the data for Cardano
        cardano_data = df[df['crypto_name'] == 'cardano']

        plt.figure(figsize=(10, 6))
        plt.plot(cardano_data['timestamp'], cardano_data['price'], marker='o', color='r')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Cardano Price Over Time')
        plt.xticks(rotation=45)

        plt.savefig('cardano_price.pdf')

        plt.tight_layout()
        plt.show()
        logging.info('Cardano PDF plot generated')

        delete_file(file_path)
    else:
        logging.info("No se encontró el archivo.")