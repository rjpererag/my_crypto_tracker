CREATE extension if NOT EXISTS "uuid-ossp";

DROP TABLE if EXISTS symbols CASCADE;
CREATE table symbols(
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	name text NOT NULL,
	symbol text NOT NULL
);


DROP TABLE if EXISTS exchange CASCADE;
CREATE TABLE exchange(
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	name text NOT NULL,
	country text
);


DROP TABLE if EXISTS tickers CASCADE;
CREATE TABLE tickers(
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	symbols_id UUID NOT NULL,
	exchange_id UUID NOT NULL,
	ticker text NOT NULL,

	CONSTRAINT fk_symbols_id FOREIGN KEY (symbols_id) REFERENCES symbols(id) ON DELETE CASCADE,
	constraint fk_exchange_id FOREIGN KEY (exchange_id) REFERENCES exchange(id) ON DELETE CASCADE
);


DROP TABLE if EXISTS prices CASCADE;
CREATE TABLE prices(
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	ticker_id UUID NOT NULL,
	price NUMERIC NOT NULL,
	timestamp TIMESTAMP NOT NULL,

	CONSTRAINT fk_ticker_id FOREIGN KEY (ticker_id) REFERENCES tickers(id) ON DELETE CASCADE
);
