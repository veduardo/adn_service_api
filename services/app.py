from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config')

# Create the db object to handle module related operations
db = SQLAlchemy(app)

# Note: In order to create the database, drop to the flask shell,
# import the db object and run SQLAlchemy's create_all() method:
# $ flask shell
# >>> from app import db
# >>> db.create_all()

from controllers import *