
# Design Document – Pokémon Scouting API

## 1. Overview

The Pokémon Scouting API is designed as a modular, maintainable Flask application that fetches Pokémon data from an external API, processes it, and persists it locally.

The system emphasizes:
- Separation of concerns
- Reusability
- Testability
- Minimal configuration for future scouting tasks

---

## 2. Architecture

The application follows a layered architecture:

Routes → Services → Repository → Database

yaml
Copiar código

### Layers

- **Routes**: Handle HTTP requests and responses
- **Client**: Communicates with external APIs (PokéAPI)
- **Processor**: Sanitizes and normalizes external data
- **Repository**: Encapsulates database access
- **Models**: Define database schema

---

## 3. Key Design Decisions

### 3.1 Separation of Concerns

Each responsibility is isolated:

| Component | Responsibility |
|---------|----------------|
| `routes.py` | HTTP logic |
| `client.py` | External API calls |
| `processor.py` | Data transformation |
| `repository.py` | Database operations |
| `models.py` | ORM definitions |

This allows independent testing and future replacement of components.

---

### 3.2 Reusability for Future Scouting

The scouting logic does **not depend on hardcoded Pokémon**.

```python
Config.DEFAULT_POKEMON
```
By changing configuration only, the same scouting pipeline can be reused for:
* New Pokémon sets
* Different environments
* Scheduled or automated scouting

### 3.3 Repository Pattern
Database access is abstracted behind a repository:

```python
PokemonRepository.get_all()
PokemonRepository.create()
PokemonRepository.delete_by_name()
```

Benefits:
* Cleaner routes
* Easier testing
* Database implementation can change without impacting routes

### 3.4 External API Isolation
All PokéAPI communication is handled by a dedicated client.

Benefits:
* Centralized error handling
* Easier mocking in tests
* Future API replacement is localized

## 4. Testing Strategy
* Uses pytest
* Tests run against an in-memory SQLite database
* Covers:
  * Empty state 
  * Create 
  * Read 
  * Delete 
  * Error cases 
  * Each test is isolated and repeatable.

## 5. Error Handling
* Duplicate Pokémon are detected before insertion
* Non-existing Pokémon deletions return proper HTTP status codes
* External API failures can be handled at the client layer

## 6. Scalability & Extensibility
The current design supports:
* Adding new scouting sources
* Changing databases
* Adding background jobs
* Introducing async processing
Minimal refactoring would be required.

## 7. Trade-offs
* SQLite chosen for simplicity
* Synchronous requests for clarity
* No authentication for MVP scope
These decisions favor readability and speed of development.

## 8. Conclusion
The Pokémon Scouting API is designed to be simple, modular, and extensible.
Its architecture supports future growth while remaining easy to test and maintain.