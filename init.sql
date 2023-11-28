BEGIN TRANSACTION;
CREATE TABLE coin_data (
	coin VARCHAR NOT NULL, 
	date DATE NOT NULL, 
	price FLOAT, 
	json JSON, 
	PRIMARY KEY (coin, date)
);
CREATE TABLE coin_month_data (
	coin VARCHAR NOT NULL, 
	year INTEGER NOT NULL, 
	month INTEGER NOT NULL, 
	min_price FLOAT, 
	max_price FLOAT, 
	PRIMARY KEY (coin, year, month)
);
