SHELL=/bin/bash

dev.all: dev.build dev.up

dev.build:
	@docker-compose -f docker-compose.dev.yml build

dev.up.d:
	@docker-compose -f docker-compose.dev.yml up -d

dev.up:
	@docker-compose -f docker-compose.dev.yml up

dev.down:
	@docker-compose -f docker-compose.dev.yml down --remove-orphans

dev.restart:
	@docker-compose -f docker-compose.dev.yml restart

dev.logs:
	@docker-compose -f docker-compose.dev.yml logs -f

dcshell:
	@docker exec -it tnc_task-dc01 /bin/bash

dshell:
	@docker exec -it tnc_task-dc01 python manage.py shell

ipshell:
	@docker exec -it tnc_task-dc01 python manage.py shell -i ipython

dcattach:
	@docker attach tnc_task-dc01

migrate:
	@docker exec -it tnc_task-dc01 python manage.py makemigrations
	@docker exec -it tnc_task-dc01 python manage.py migrate

collectstatic:
	@docker exec -it tnc_task-dc01 python manage.py collectstatic

test:
	@docker exec -it tnc_task-dc01 python manage.py test

psql:
	@docker exec -it anybook-pc01 psql -U postgres

rediscli:
	@docker exec -it anybook-rc01 redis-cli -h redis
