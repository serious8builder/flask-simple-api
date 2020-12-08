from datetime import datetime

from flask import Blueprint, request

router = Blueprint('health', __name__)


@router.route('/', methods=['GET'])
def check_health():
    fmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now().strftime(fmt)
    client_host = request.remote_addr
    data = {'message': 'OK', 'now': now, 'ip': client_host}
    content = '<br>'.join('%s : %s' % (key, value) for key, value in data.items())
    return content
