# SQLite with SQLAlchemy in Flask - CRUD Operations

This project is a simple example of performing CRUD (Create, Read, Update, Delete) operations using SQLite database and SQLAlchemy in a Flask application. It demonstrates how to set up a basic Flask web application, create a SQLite database, and perform various database operations using SQLAlchemy.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- [Pipenv](https://pipenv.pypa.io/en/latest/) for managing virtual environments.
- Basic understanding of Flask and SQLAlchemy.


## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/sqlite-sqlalchemy-flask-crud.git
cd sqlite-sqlalchemy-flask-crud
```

2. Create a virtual environment and install project dependencies using Pipenv:

```bash
pipenv install
```

3. Activate the virtual environment:

```bash
pipenv shell
```

4. Run the application:

```bash
python app.py
```

The Flask application will start on `http://127.0.0.1:5000/`.

## Usage

You can use this project as a starting point for building your own Flask applications with SQLite and SQLAlchemy. The `app.py` file sets up the Flask app, and you can modify the routes in the `routes` folder to suit your needs.

The provided `Employee` model in `models/employee.py` is a simple example. You can expand and customize it as necessary for your specific application.

## API Endpoints

The following API endpoints are available:

- **GET /employees**: Retrieve a list of all employees.
- **GET /employee/{id}**: Retrieve information about a specific employee.
- **POST /employee**: Create a new employee.
- **PUT /employee/{id}**: Update information for a specific employee.
- **DELETE /employee/{id}**: Delete a specific employee.

Please refer to the individual route files in the `routes` directory for more details on how these operations are implemented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. You are free to use and modify this code as needed for your projects.