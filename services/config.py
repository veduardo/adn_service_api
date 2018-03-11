#
# App config
#

# Enabling the development environment
DEBUG = True

# Define app directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable protection against cross-site request forgery (CSRF)
CSRF_ENABLED = True

# Use a secure key
CSRF_SESSION_KEY = "a243#$*t&*HUIzB"

# Secret key for signing cookies
SECRET_KEY = "asdf56af8*&%$#$dasfhj"

# SQLAlchemy Settings
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "services.sqlite3")
SQLALCHEMY_TRACK_MODIFICATIONS = False