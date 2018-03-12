## Adn Service API Project

The goal of this project is to create a RESTful Flask application with 4 endpoints:

Endpoint 1: health check (GET)

- GET http://service/health

Endpoint 2: add new order (POST application/json):

- POST http://service/order

Endpoint 3: return existing orders based on customer_id (GET)

- GET http://service/order/<customer_id>

Endpoint 4: return the top 3 most bought products (GET)

- GET http://service/products/top



## Useful Notes:

### Flask CLI Utilities
In order to use common Flask CLI utilities such as `flask run` and `flask shell`, make sure the FLASK_APP env variable is set:

```
$ export FLASK_APP=~/Projects/adn_api/services/run.py
```

### Creating the database
In order to create the database, just drop to the `flask shell` ~~import the db object~~<sup>1</sup> and run SQLAlchemy's create_all() method:

```
$ flask shell
>>> from app import db
>>> db.create_all()
```

[1] `>>> from app import db`. This step is optional thanks to the @app.shell_context_processor in app.py.