import os
import logging
import random

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
    error = request.args.get('e')

    raise_error_by_params(error)

    data = gatter_basic_data()
    content = '<br>'.join('%s : %s' % (key, value) for key, value in data.items())
    return content


def raise_error_by_params(error):
    if error is not None:
        error = 1.0 if error == '' else int(error) * 0.01
        if error > random.random():
            raise Exception('Some Exception')

def gatter_basic_data():
    app_name = os.getenv('appname')
    fmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now().strftime(fmt)
    client_host = request.remote_addr
    data = {'app': app_name,
            'message': 'OK',
            'now': now,
            'ip': client_host}
    return data

@click.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=5000)
@click.option('--debug/--no-debug', default=False)
def run(host, port, debug):
    print('>>> {} {} {}'.format(host, port, debug))
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run()
