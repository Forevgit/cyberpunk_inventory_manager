
# Cyberpunk Inventory Management System

## Overview

The **Cyberpunk Inventory Management System** is a RESTful API built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It allows for the management of inventory items in a cyberpunk-themed game, including CRUD (Create, Read, Update, Delete) operations on game items like weapons, cybernetic enhancements, and gadgets.

## Features

- **CRUD Operations**: Manage inventory items with create, read, update, and delete operations.
- **Authentication**: Secure endpoints with JWT-based authentication, allowing only authenticated users to access the CRUD functionalities.
- **Pagination**: Support for paginated retrieval of inventory items.
- **Dockerized Setup**: Easy deployment with **Docker** using `docker-compose`.

## Project Structure

```
app/
├── auth/                      # Authentication-related files
│   ├── auth_config.py
│   ├── dependencies.py
│   ├── models.py
│   ├── password_service.py
│   ├── routers.py
│   ├── schemas.py
│   ├── service.py
│   └── token_service.py
├── inventory/                 # Inventory management files
│   ├── dependencies.py
│   ├── inventory_data_service.py
│   ├── models.py
│   ├── routers.py
│   ├── schemas.py
│   └── service.py
├── tests/                     # Unit tests
│   ├── conftest.py
│   └── test_inventory.py
├── .env                       # Environment variables
├── alembic.ini                # Alembic configuration for database migrations
├── database.py                # Database connection setup
├── docker-compose.yml         # Docker Compose configuration
├── Dockerfile                 # Dockerfile for building the FastAPI app
├── main.py                    # Entry point for the FastAPI application
├── pytest.ini                 # Pytest configuration
└── requirements.txt           # Python dependencies
```

## Getting Started

### Prerequisites

- **Docker** and **Docker Compose**

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Forevgit/cyberpunk_inventory_manager.git
   cd cyberpunk_inventory_manager
   ```

2. **Setting Up a Virtual Environment (Optional)**
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate(on macOS)

   ```

3**Set up the environment:**

   Create a `.env` file in the root directory with your environment variables (check .env.example):

   ```env
   DB_USER=DB_USER
   DB_PASSWORD=DB_PASSWORD
   DB_HOST=DB_HOST
   DB_PORT=DB_PORT
   DB_NAME=DB_NAME

   SECRET_KEY=SECRET_KEY

   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

### Running the Application

**Note:** This project is designed to run **exclusively through Docker**.

To start the application:

```bash
docker-compose up --build
```

This will:

- Build the FastAPI application and set up a PostgreSQL database.
- Run database migrations.
- Start the API at `http://localhost:8000`.

### Running Migrations

   To ensure the database schema is up-to-date, run the migrations with the following command:

```bash
   docker exec -it <container_name> alembic upgrade head
```

### Running Tests

To run tests within the Docker environment:

```bash
docker exec -it <container_name> pytest
```

Replace `<container_name>` with the name of your running FastAPI container.

## API Endpoints

- **POST** `/auth/register`: Register a new user.
- **POST** `/auth/login`: Login and receive a JWT token.
- **POST** `/inventory/`: Create a new inventory item.
- **GET** `/inventory/`: Get a list of inventory items (supports pagination).
- **GET** `/inventory/{id}`: Get a single item by its ID.
- **PUT** `/inventory/{id}`: Update an existing inventory item.
- **DELETE** `/inventory/{id}`: Delete an inventory item.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- **FastAPI** - For its simplicity and performance.
- **SQLAlchemy** - For easy database interactions.
- **Docker** - For making deployment straightforward.
