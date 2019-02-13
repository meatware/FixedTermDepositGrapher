start:
	docker-compose up -d

synch:
	#https://stackoverflow.com/questions/45723891/how-to-rsync-from-a-host-computer-to-docker-container-using-docker-cp
	docker cp . /workspace

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

