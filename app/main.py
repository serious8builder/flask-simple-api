import os

from flask import Flask
from .router import health, calc
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)


@app.route('/ok')
def hi():
    return 'OK'


app.register_blueprint(health.router, url_prefix='/')
app.register_blueprint(calc.router, url_prefix='/calc')
