start:
	bash ./.makefile/start.sh

clean:
	bash ./.makefile/clean.sh

logs:
	docker-compose logs -f

stop:
	docker-compose stop

# init_db:
# 	bash ./.makefile/init_db.sh

enter:
	docker exec -it ftd_app bash

exec:
	docker-compose exec -T myapp $(COMMAND)

FLASK_PORT=3000
FLASK_HOST=0.0.0.0

serve:
	docker-compose exec app env FLASK_APP=launcher.py flask run --port $(FLASK_PORT) --host $(FLASK_HOST)

# flask migration through cli
init_migrate:
	docker-compose exec app env flask db init

migrate:
	docker-compose exec app env flask db migrate

upgrade:
	docker-compose exec app env flask db upgrade

downgrade:
	docker-compose exec app env flask db downgrade

pycodestyle:
	docker-compose exec -T authorizer pycodestyle /workspace/ --exclude=.serverless,node_modules

# tests
test:
	docker-compose exec -T authorizer pytest
