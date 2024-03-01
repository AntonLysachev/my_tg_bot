install:
	poetry install --no-root

start:
	poetry run python bot/bot.py

dev:
	poetry run flask --app bot:app --debug run --port 8000
