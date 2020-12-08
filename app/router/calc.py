from flask import Blueprint

router = Blueprint('calc', __name__)


@router.route('/add/<int:x>/<int:y>', methods=['GET'])
def add(x, y):
    ans = x + y
    rs = '%f + % f = %f' % (x, y, ans)
    return rs
