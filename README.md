# MY Crypto APP

### .ENV Example
    #DATABASE
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    POSTGRES_PASSWORD=mypassword
    
    #RABBITMQ
    RABBITMQ_HOST=rabbitmq
    RABBITMQ_QUEUE_NAME=my_queue
    RABBITMQ_EXCHANGE_NAME=""
    RABBITMQ_ROUTING_KEY=my_queue
    
    #TRACKER SETTINGS
    TRACKER_SAVE_CACHED_DATA=False
    TRACKER_WAITING_TIME=10

    # FRONTEND SETTINGS
    API_HOST=http://api:5001


### APIs Calls Tests
    curl http://localhost:5001/symbols
    curl http://localhost:5001/exchanges
    curl http://localhost:5001/tickers/bitcoin/binance
    curl http://localhost:5001/price-history-minutes/120%20minute/BTCUSDT
