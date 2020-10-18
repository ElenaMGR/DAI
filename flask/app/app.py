#./app/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.error('Prueba de logging')
    return 'Hello, World!'