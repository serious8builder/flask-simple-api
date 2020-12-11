import os
from datetime import datetime

from flask import Blueprint, request

router = Blueprint('health', __name__)


@router.route('/', methods=['GET'])
def check_health():
    app_name = os.getenv('appname')
    fmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now().strftime(fmt)
    client_host = request.remote_addr
    data = {'app': app_name, 'message': 'OK', 'now': now, 'ip': client_host}
    content = '<br>'.join('%s : %s' % (key, value) for key, value in data.items())
    return content
