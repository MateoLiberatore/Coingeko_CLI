# Coingeko_CLI
Crypto console app, coin data, reports, predictions, comparisons and plots

# This App 
In this console application I'm searching to build a complete tool kit for crypto data consuming the API provided by the website of CoinGeko.
The functionalities I am currently building are:

# API Calls:
In the coingeki_apy.py we have multiple functions created to take diferent data of te CoinGeko API, single day information of a specific day, 
a period of time or a multiple call using previous functions in order to create a report, this report can be used in this aplication not only 
to have a file with the data, but also to save information in a postgres db.  (:construction: currently fixing file issues  :construction:)

# Database:
In order to save this reports, in te coingeko_db.py somewhere other than in xlsx or csv files, we use docker to create a Postgres db to solve a particular issue with the data,
we can not ask por a period of time longer than six months to the API, so by making a few API calls we can have extended periods of time saved in our db.
(:construction: pending: Implement an .yml, a .env file to hide sensible information  :construction:)

