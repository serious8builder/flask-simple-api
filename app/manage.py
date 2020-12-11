import click

from .main import app


@click.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=5000)
@click.option('--debug/--no-debug', default=False)
def run(host, port, debug):
    print('>>> {} {} {}'.format(host, port, debug))
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run()
