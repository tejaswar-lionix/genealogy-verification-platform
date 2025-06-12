build:
	docker build -t genealogy-platform .

test:
	pytest -q

run:
	python manage.py runserver 0.0.0.0:8000
