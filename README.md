# Coingeko_CLI
Crypto console app, coin data, reports, predictions, comparisons and plots

# :round_pushpin: This App 
In this console application I'm searching to build a complete tool kit for crypto data consuming the API provided by the website of CoinGeko.
The functionalities I am currently building are:

# :round_pushpin: API Calls:
In the coingeki_apy.py we have multiple functions created to take diferent data of te CoinGeko API, single day information of a specific day, 
a period of time or a multiple call using previous functions in order to create a report, this report can be used in this aplication not only 
to have a file with the data, but also to save information in a postgres db.  
  :construction: currently fixing file issues  :construction:

# :round_pushpin: Database:
In order to save this reports, in te coingeko_db.py somewhere other than in xlsx or csv files, we use docker to create a Postgres db to solve a particular issue with the data,
we can not ask por a period of time longer than six months to the API, so by making a few API calls we can have extended periods of time saved in our db.
  :construction: pending: Implement an .yml, and a .env file to hide sensible information  :construction:

# :round_pushpin: Plots:
In the coingeko_plots.py module we have a modified function from the API module to get the last 30 days information of some coins and plot their respective values.
  :construction: Pending: Create more interactions with the API to get diferent time extensions information and build interactions with the database :construction:

# :round_pushpin: QUERIES:
Coingeko_queries is a module created to have gneral information about the data stored in the database.
  :construction: Create more queries and a implement it in the CLI :construction:

# :round_pushpin: Price Trend:
The price_trend.py prediction module can calculate the future value of a specific coin based in the past week values.
  :construction: Pending: Implement diferent time extension predictions to have more accurate data :construction:

# :round_pushpin: Risk Evaluation:
risk_evaluation.py is a module capable of evaluate the risk of a crypto currency based in the variations of the crypto currencies values stored in the database.
  :construction: Pending: Implement the creation of a detailed report :construction:

#:round_pushpin: :construction: Main.py :construction: (currently not a CLI here)
Here I have a CLI builded with click, needed to consume all the functionalities of the app.
Lot to fix here since is the first time for me building an CLI
  :construction: Need to implement again how to use the functionalities created in the other modules
  :construction: Need to know how to implement commands to execute the functionalities without parameters


