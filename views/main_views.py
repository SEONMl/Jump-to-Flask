from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from app.models import Question

bp=Blueprint('main', __name__, url_prefix='/')
#             블루프린트별칭, 모듈명, 접두어


@bp.route('/hello/')
def hell_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
# redirect(URL) - URL로 페이지를 이동
# url_for(라우팅 함수명) - 라우팅 함수에 매핑되어 있는 URL을 리턴