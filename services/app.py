from flask import Flask

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config')

@app.route('/')
def main():
    return "Hello, World!"