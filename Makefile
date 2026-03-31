clean:	## Очистить .pyc-файлы и __pycache__
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

collectstatic:	## Собрать статические файлы (production)
	uv run manage.py collectstatic --settings=core.settings.production

createsuperuser:	## Создать суперпользователя (development)
	uv run manage.py createsuperuser --settings=core.settings.development

createsuperuser-prod:	## Создать суперпользователя (production)
	uv run manage.py createsuperuser --settings=core.settings.production

fixtures:	## Загрузить фикстуры subject.json (development)
	uv run manage.py loaddata fixtures/subject.json --settings=core.settings.development

fixtures-prod:	## Загрузить фикстуры subject.json (production)
	uv run manage.py loaddata fixtures/subject.json --settings=core.settings.production

get-fixtures:	## Сохранить данные Subject в fixtures/subject.json (development)
	uv run manage.py dumpdata common.Subject --indent 4 > fixtures/subject.json --settings=core.settings.development

get-fixtures-prod:	## Сохранить данные Subject в fixtures/subject.json (production)
	uv run manage.py dumpdata common.Subject --indent 4 > fixtures/subject.json --settings=core.settings.production

help:	## Показать список доступных команд
	@echo ""
	@echo "Доступные команды:"
	@awk 'BEGIN {FS = ":.*##"; printf ""} /^[a-zA-Z_-]+:.*##/ {printf " \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""

migrate:	## Применить миграции (development)
	uv run manage.py makemigrations --settings=core.settings.development
	uv run manage.py migrate --settings=core.settings.development

migrate-prod:	## Применить миграции (production)
	uv run manage.py makemigrations --settings=core.settings.production
	uv run manage.py migrate --settings=core.settings.production

run:	## Запустить сервер (development)
	uv run python manage.py runserver 0.0.0.0:8050 --settings=core.settings.development

run-prod:	## Запустить сервер (production)
	uv run manage.py runserver --settings=core.settings.production

shell:	## Открыть Django shell (development)
	uv run manage.py shell --settings=core.settings.development

shell-prod:	## Открыть Django shell (production)
	uv run manage.py shell --settings=core.settings.production

test:	## Запустить тесты (development)
	uv run manage.py test --settings=core.settings.development

test-prod:	## Запустить тесты (production)
	uv run manage.py test --settings=core.settings.production

to-req: ## Генерация requirements.txt из pyproject.toml
	python -c "import toml; f = open('pyproject.toml', 'r'); data = toml.load(f); print('\n'.join(data['project']['dependencies']))" > requirements.txt
