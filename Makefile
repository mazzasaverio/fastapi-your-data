#!/usr/bin/make

include .env



define SERVERS_JSON
{
	"Servers": {
		"1": {
			"Name": "fastapi-alembic",
			"Group": "Servers",
			"Host": "$(DB_HOST)",
			"Port": 5432,
			"MaintenanceDB": "postgres",
			"Username": "$(DB_USER)",
			"SSLMode": "prefer",
			"PassFile": "/tmp/pgpassfile"
		}
	}
}
endef
export SERVERS_JSON


run-pgadmin:
	echo "$$SERVERS_JSON" > ./pgadmin/servers.json && \
	docker volume create pgadmin_data && \
	docker compose -f pgadmin.yml up --force-recreate
	
load-server-pgadmin:
	docker exec -it pgadmin python /pgadmin4/setup.py --load-servers servers.json

clean-pgadmin:
	docker volume rm pgadmin_data


formatter:
	cd backend/app && \
	poetry run black app