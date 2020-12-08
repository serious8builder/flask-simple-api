from flask import Flask
from .router import health, calc

app = Flask(__name__)


@app.route('/ok')
def hi():
    return 'OK'


app.register_blueprint(health.router, url_prefix='/health')
app.register_blueprint(calc.router, url_prefix='/calc')

