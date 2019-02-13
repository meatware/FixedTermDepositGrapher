start:
	docker-compose up -d

logs:
	docker-compose logs -f

stop:
	docker-compose stop

init_db:
	bash ./.makefile/init_db.sh

exec:
	docker-compose exec -T myapp $(COMMAND)


pycodestyle:
	docker-compose exec -T authorizer pycodestyle /workspace/ --exclude=.serverless,node_modules


test:
	docker-compose exec -T authorizer pytest

