# Pokémon Scouting API

A Flask-based REST API designed to **scout, store, and manage Pokémon data** using the public PokéAPI.  
The application is built with **reusability, testability, and future scalability** in mind.

---

## Features

- Scout Pokémon data from the PokéAPI
- Store sanitized Pokémon data in a database
- List, add, and delete Pokémon
- Designed for **future scouting tasks** with minimal configuration changes
- Fully tested using `pytest`
- Interactive API documentation via **Swagger (OpenAPI)**

---

## Tech Stack

- **Python 3**
- **Flask**
- **Flask SQLAlchemy**
- **SQLite**
- **Pytest**
- **Swagger / OpenAPI**

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pokemon-scouting.git
cd pokemon-scouting
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python run.py
```

The API will be available at:
```bash
http://localhost:5000
```

## API Documentation (Swagger)
This project includes interactive API documentation using Swagger UI.
Once the app is running, open:
```bash
http://localhost:5000/docs
```
With Swagger you can:
* Explore all endpoints
* View request/response schemas
* Test endpoints directly from the browser


## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/scout` | Scout and store default Pokémon |
| GET | `/pokemon` | List all stored Pokémon |
| POST | `/pokemon` | Add a Pokémon manually |
| DELETE | `/pokemon/{name}` | Delete a Pokémon by name |

### Usage Examples (curl)
#### 1. Scout default Pokémon: 
Fetches and stores the Pokémon defined in Config.DEFAULT_POKEMON (This allows new scouting tasks to be configured without modifying business logic)
```text
curl -X POST http://localhost:5000/scout
```

#### 2. List all stored Pokémon: 
```text
curl http://localhost:5000/pokemon
```

#### 3. Add a Pokémon manually: 
```text
curl -X POST http://localhost:5000/pokemon \
  -H "Content-Type: application/json" \
  -d '{"name": "bulbasaur"}'
```

#### 4. Delete a Pokémon by name: 
```text
curl -X DELETE http://localhost:5000/pokemon/pikachu
```

## Database

This project uses SQLite for local development.

- The database file (`pokemon.db`) is **not committed to the repository**
- It is created automatically the first time the app runs
- By default, it will be generated inside the `instance/` folder

No manual database setup is required.

## Running tests
All tests are written using pytest.
```text
pytest -v
```
The test suite covers:
* Empty database behavior
* Adding Pokémon
* Listing Pokémon
* Deleting Pokémon
* Error handling for non-existing Pokémon

**Sidenote:** When running tests, the application uses an in-memory SQLite database,
so no local files are created.

## Project structure
```text
PokemonScouting/
├── app/
│   ├── services/
│   │   ├── __init__.py
│   │   └── repository.py
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   └── routes.py
│
├── static/
│   └── swagger.json
│
├── docs/
│   └── DESIGN.md
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_pokemon_routes.py
│
├── instance/
│   └── pokemon.db
│
├── requirements.txt
├── README.md
└── run.py
```

## Design Philosophy
* Separation of concerns (routes, services, persistence)
* Config-driven behavior
* Easily extensible for new scouting requirements
* Test-first mindset
* See DESIGN.md for architectural decisions

## Author
Teresa Jiménez - Backend / Python Developer

## License
This project is for educational and technical assessment purposes.