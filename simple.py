import os

import click
from datetime import datetime

from flask import Flask, request

from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)

@app.route('/ok')
def hi():
    return 'OK'


@app.route('/', methods=['GET'])
def check_health():
    app_name = os.getenv('appname')
    fmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now().strftime(fmt)
    client_host = request.remote_addr
    data = {'app': app_name, 'message': 'OK', 'now': now, 'ip': client_host}
    content = '<br>'.join('%s : %s' % (key, value) for key, value in data.items())
    return content


@click.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=5000)
@click.option('--debug/--no-debug', default=False)
def run(host, port, debug):
    print('>>> {} {} {}'.format(host, port, debug))
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run()
