DB_NAME=mydatabase
DB_USER=postgres
DB_HOST=localhost
DB_PORT=5432
DB_PASSWORD=mypassword


.PHONY: db-create
db-create:
	@echo "Creating database $(DB_NAME)..."
	PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d postgres -c "CREATE DATABASE $(DB_NAME);"
	#$(call psql_exec, "CREATE DATABASE $(DB_NAME);")
	@echo "Database $(DB_NAME) created."

### Create tables from schema.sql
#db-schema:
#	@echo "Applying schema..."
#	PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d $(DB_NAME) -f $(AUXILIAR_TABLES_SCHEMA)
#	@echo "Auxiliary tables created successfully."
#	PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d $(DB_NAME) -f $(PRIMARY_TABLE_SCHEMA)
#	@echo "Primary table created successfully."
#
### Drop database
#db-drop:
#	@echo "Dropping database..."
#	PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d postgres -c "DROP DATABASE IF EXISTS $(DB_NAME);"
#
#
### Drop and recreate database
#db-reset:
#	@echo "Resetting database..."
#	#$(call psql_exec, "DROP DATABASE IF EXISTS $(DB_NAME);")
#	$(MAKE) db-drop
#	$(MAKE) db-create
#	$(MAKE) db-schema