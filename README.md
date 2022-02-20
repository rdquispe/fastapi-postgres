# Movies 

### Features

- Database Connection Using SQLAlchemy
- FastAPI Server
- Unit Testing with PyTest
- Basic CRUD for Movies


### Dependencies

- Python 3.9+
- Pipenv

### Tests

```sh
pytest
```

### Environment


```sh
pipenv shell
```


- Setting up environment variables

| Key          | Value                                   |
|--------------|-----------------------------------------|
| DATABASE_URL | postgresql://user:password@host:port/db |


- To run the project

```sh
uvicorn main:app --reload  
```
