from flask import Blueprint

bp = Blueprint('index', __name__, url_prefix='/') # 블루프린트 생성

@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'