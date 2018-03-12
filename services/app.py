from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config')

# Create the db object to handle module related operations
db = SQLAlchemy(app)

from controllers import *

# Preloads useful objects into the flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Order': Order, 'Product': Product, 'Customer': Customer}