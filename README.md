# GenZ Roast Flask App

A fun web application that generates playful, GenZ-style roasts. Built with Flask, Docker, and Gunicorn for easy deployment and scalability.

## Features
- Generate random GenZ roasts
- RESTful API endpoints
- Responsive web UI
- Error pages (404, 500)
- Dockerized for easy deployment
- Gunicorn configuration for production

## Project Structure
```
genz_roast_flask-app/
├── Dockerfile
├── gunicorn_conf.py
├── requirements.txt
├── wsgi.py
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── roast.py
│   ├── blueprints/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── main/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── 404.html
│       ├── 500.html
│       ├── base.html
│       └── index.html
│   └── tests/
│       └── test_smoke.py
```

## Getting Started

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
	```sh
	git clone https://github.com/sayanC04/roast-flask-app.git
	cd roast-flask-app/genz_roast_flask-app
	```
2. Install dependencies:
	```sh
	pip install -r requirements.txt
	```
3. Run the app:
	```sh
	flask run
	```

### Running with Docker
1. Build the Docker image:
	```sh
	docker build -t genz-roast-app .
	```
2. Run the container:
	```sh
	docker run -p 5000:5000 genz-roast-app
	```

### Running with Gunicorn (Production)
```sh
	gunicorn -c gunicorn_conf.py wsgi:app
```

## API Endpoints
- `/api/roast` : Get a random roast (JSON)
- `/` : Main web UI

## Testing
Run smoke tests:
```sh
pytest tests/test_smoke.py
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
