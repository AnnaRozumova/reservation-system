.PHONY: install run shell clean

# Create a virtual environment and install dependencies
install:
	pipenv install --dev

# Activate the virtual environment shell
shell:
	pipenv shell

# Run the application
run:
	pipenv run python manage.py runserver

# Run tests
test:
	pipenv run pytest

# Clean up the virtual environment
clean:
	pipenv --rm
