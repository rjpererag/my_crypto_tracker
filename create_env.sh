#!/bin/bash

# Check if .env file already exists
if [ -f ".env" ]; then
    echo ".env file already exists. Skipping creation."
    exit 0
fi

echo "Creating .env file with default values..."

cat << EOF > .env
# DATABASE
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

EOF
echo ".env file created successfully."